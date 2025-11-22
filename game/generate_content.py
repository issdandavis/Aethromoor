#!/usr/bin/env python3
"""
Content generator for Avalon ChoiceScript scenes using AI connectors.

This script uses the Anthropic API to generate additional game content
that fits the existing narrative style and structure.
"""

import os
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Install with: pip install anthropic")
    sys.exit(1)

try:
    from dotenv import load_dotenv
except ImportError:
    print("Error: python-dotenv package not installed. Install with: pip install python-dotenv")
    sys.exit(1)

load_dotenv(Path(__file__).parent.parent / 'config' / '.env')

ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')

if not ANTHROPIC_API_KEY:
    print("Error: ANTHROPIC_API_KEY not found in config/.env")
    print("Please copy config/.env.example to config/.env and add your API key.")
    sys.exit(1)


def read_existing_scenes():
    """Read all existing scene files to understand the narrative context."""
    scenes_dir = Path(__file__).parent / 'scenes'
    scenes = {}
    for scene_file in scenes_dir.glob('*.txt'):
        scenes[scene_file.stem] = scene_file.read_text()
    return scenes


def generate_scene_content(scene_name, prompt, existing_scenes):
    """Generate new scene content using Anthropic API."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    # Build context from existing scenes
    context = "Here are the existing scenes in the Avalon ChoiceScript game:\n\n"
    for name, content in existing_scenes.items():
        context += f"=== {name}.txt ===\n{content}\n\n"
    
    full_prompt = f"""{context}

Based on the existing scenes above, generate a new ChoiceScript scene called "{scene_name}".

{prompt}

Requirements:
- Use proper ChoiceScript syntax (*choice, *set, *goto, *finish, *goto_scene, etc.)
- Maintain consistency with existing stat names: honor, attunement, mentor, council_trust, oathbound, resonance_mark
- Match the narrative tone and style of the existing scenes
- Include meaningful choices that affect stats or story progression
- Keep the fantasy setting of Avalon and the Spiral of Eternity
- Use the mentor variable appropriately (should be either "Aria" or "Corin")
- Include 2-4 meaningful choices per scene
- Each choice should have consequences (stat changes, flags, or narrative variations)

Generate only the ChoiceScript scene content, no extra commentary."""

    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": full_prompt}
        ]
    )
    
    return message.content[0].text


def save_scene(scene_name, content):
    """Save the generated scene to a file."""
    scenes_dir = Path(__file__).parent / 'scenes'
    scene_path = scenes_dir / f"{scene_name}.txt"
    scene_path.write_text(content)
    print(f"✓ Generated and saved: {scene_path}")


def update_scene_list(scene_name):
    """Add the new scene to the *scene_list in startup.txt."""
    startup_path = Path(__file__).parent / 'scenes' / 'startup.txt'
    content = startup_path.read_text()
    
    # Find the scene_list section
    lines = content.split('\n')
    scene_list_start = None
    scene_list_end = None
    
    for i, line in enumerate(lines):
        if line.strip() == '*scene_list':
            scene_list_start = i
        elif scene_list_start is not None and scene_list_end is None:
            if line and not line.startswith(' ') and not line.startswith('\t'):
                scene_list_end = i
                break
    
    if scene_list_start is not None:
        # Insert before the end of scene_list
        insert_pos = scene_list_end if scene_list_end else len(lines)
        lines.insert(insert_pos, f"  {scene_name}")
        
        startup_path.write_text('\n'.join(lines))
        print(f"✓ Added '{scene_name}' to scene_list in startup.txt")
    else:
        print("Warning: Could not find *scene_list in startup.txt")


def main():
    """Main function to generate new scenes."""
    print("Avalon Content Generator")
    print("=" * 50)
    
    # Read existing scenes for context
    print("\nReading existing scenes...")
    existing_scenes = read_existing_scenes()
    print(f"Found {len(existing_scenes)} existing scenes")
    
    # Define new scenes to generate
    new_scenes = [
        {
            "name": "library_depths",
            "prompt": """Create a scene called 'library_depths' where the player explores deeper into Avalon's ancient library.
            
The scene should:
- Start with atmospheric description of descending into older sections of the archives
- Include choices about how to interact with ancient magical texts
- Have at least one stat check (e.g., attunement >= 55)
- Reference the mentor character in at least one choice
- Include choices that can set or check the resonance_mark flag
- End by transitioning to another scene or finishing"""
        },
        {
            "name": "spiral_meditation",
            "prompt": """Create a scene called 'spiral_meditation' where the player learns to attune themselves to the Spiral of Eternity.
            
The scene should:
- Describe a mystical meditation chamber or training ground
- Include choices about different meditation techniques or approaches
- Heavily focus on attunement stat changes (both positive and negative based on choices)
- Include at least one choice that interacts with council_trust
- Have an option that references whether the player is oathbound
- End with *goto_scene epilogue or another appropriate scene"""
        },
        {
            "name": "warden_trial",
            "prompt": """Create a scene called 'warden_trial' where the player faces a test of combat prowess and tactical thinking.
            
The scene should:
- Begin with the wardens presenting a challenge or trial
- Include choices that test both honor and tactical wisdom
- Have at least one stat check for honor (e.g., honor >= 60)
- Include an option to consult with the mentor about strategy
- Feature choices that can affect the oathbound flag
- End by transitioning to epilogue or council scene"""
        }
    ]
    
    # Generate each scene
    for scene_info in new_scenes:
        print(f"\n{'=' * 50}")
        print(f"Generating: {scene_info['name']}")
        print(f"{'=' * 50}")
        
        try:
            content = generate_scene_content(
                scene_info['name'],
                scene_info['prompt'],
                existing_scenes
            )
            
            save_scene(scene_info['name'], content)
            update_scene_list(scene_info['name'])
            
            # Add to existing scenes for context in subsequent generations
            existing_scenes[scene_info['name']] = content
            
        except Exception as e:
            print(f"✗ Error generating {scene_info['name']}: {e}")
            continue
    
    print(f"\n{'=' * 50}")
    print("Content generation complete!")
    print(f"{'=' * 50}")
    print("\nNext steps:")
    print("1. Review the generated scenes in game/scenes/")
    print("2. Run ./game/sync_scenes.sh to copy them to ChoiceScript")
    print("3. Test the game locally")


if __name__ == '__main__':
    main()
