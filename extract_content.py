#!/usr/bin/env python3
"""
Extract usable content from everweave-export.pdf for game enhancement.
Focuses on narrative descriptions, character interactions, and atmospheric detail.
"""

from pypdf import PdfReader
import json
import re

def extract_dm_narration(text):
    """Extract DM narrative descriptions (remove player responses)"""
    lines = text.split('\n')
    dm_blocks = []
    current_block = []
    
    for line in lines:
        if line.startswith('DM:'):
            if current_block:
                dm_blocks.append(' '.join(current_block))
            current_block = [line.replace('DM:', '').strip()]
        elif line.startswith('Izack:') or line.startswith('Dm '):
            if current_block:
                dm_blocks.append(' '.join(current_block))
                current_block = []
        elif current_block:
            current_block.append(line.strip())
    
    if current_block:
        dm_blocks.append(' '.join(current_block))
    
    return dm_blocks

def categorize_content(text):
    """Categorize content by type"""
    categories = {
        'atmospheric': False,
        'character_dialogue': False,
        'magic_description': False,
        'teaching': False,
        'polly': False
    }
    
    text_lower = text.lower()
    
    # Atmospheric descriptions
    if any(word in text_lower for word in ['breeze', 'shimmer', 'glow', 'light', 'shadow', 'air']):
        categories['atmospheric'] = True
    
    # Character dialogue/interaction
    if any(word in text_lower for word in ['says', 'asks', 'whispers', 'replies']):
        categories['character_dialogue'] = True
    
    # Magic descriptions
    if any(word in text_lower for word in ['magical', 'spell', 'dimensional', 'arcane', 'rune']):
        categories['magic_description'] = True
    
    # Teaching/learning
    if any(word in text_lower for word in ['teach', 'learn', 'lesson', 'understand', 'wisdom']):
        categories['teaching'] = True
    
    # Polly content
    if 'polly' in text_lower or 'familiar' in text_lower:
        categories['polly'] = True
    
    return categories

def extract_forest_content(pdf, start_page=5, end_page=30):
    """Extract forest-related content"""
    forest_content = []
    
    for i in range(start_page, min(end_page, len(pdf.pages))):
        text = pdf.pages[i].extract_text()
        
        if any(term in text.lower() for term in ['forest', 'tree', 'vine', 'leaf', 'green']):
            dm_blocks = extract_dm_narration(text)
            
            for block in dm_blocks:
                if len(block) > 100:  # Substantial content only
                    categories = categorize_content(block)
                    forest_content.append({
                        'page': i + 1,
                        'text': block[:500],  # Limit length
                        'categories': categories
                    })
    
    return forest_content

def extract_teaching_moments(pdf, start_page=40, end_page=110):
    """Extract teaching/Academy content"""
    teaching_content = []
    
    for i in range(start_page, min(end_page, len(pdf.pages))):
        text = pdf.pages[i].extract_text()
        
        if any(term in text.lower() for term in ['teach', 'academy', 'student', 'lesson', 'apprentice']):
            dm_blocks = extract_dm_narration(text)
            
            for block in dm_blocks:
                if len(block) > 100:
                    categories = categorize_content(block)
                    if categories['teaching']:
                        teaching_content.append({
                            'page': i + 1,
                            'text': block[:500],
                            'categories': categories
                        })
    
    return teaching_content

def main():
    print("Loading PDF...")
    pdf = PdfReader('everweave-export.pdf')
    
    print(f"Total pages: {len(pdf.pages)}")
    
    print("\nExtracting forest content...")
    forest = extract_forest_content(pdf)
    print(f"Found {len(forest)} forest passages")
    
    print("\nExtracting teaching content...")
    teaching = extract_teaching_moments(pdf)
    print(f"Found {len(teaching)} teaching passages")
    
    # Save to JSON for easy access
    output = {
        'forest_expedition': forest[:10],  # Top 10 passages
        'teaching_moments': teaching[:10]
    }
    
    with open('extracted_content.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print("\nSaved to extracted_content.json")
    
    # Print samples
    print("\n" + "="*70)
    print("SAMPLE FOREST CONTENT")
    print("="*70)
    if forest:
        print(f"\nPage {forest[0]['page']}:")
        print(forest[0]['text'][:300])
    
    print("\n" + "="*70)
    print("SAMPLE TEACHING CONTENT")
    print("="*70)
    if teaching:
        print(f"\nPage {teaching[0]['page']}:")
        print(teaching[0]['text'][:300])

if __name__ == '__main__':
    main()
