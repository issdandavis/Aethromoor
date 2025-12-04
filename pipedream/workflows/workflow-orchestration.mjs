import github from "@pipedream/github"
import google_drive from "@pipedream/google_drive"
import dropbox from "@pipedream/dropbox"
import { axios } from "@pipedream/platform"

export default defineComponent({
  name: "Automated Workflow Orchestration",
  description: "Orchestrates automated workflows between GitHub, Google Drive, Dropbox, and Slack for seamless productivity",
  type: "action",
  props: {
    github,
    google_drive,
    dropbox,
    slackWebhook: {
      type: "string",
      label: "Slack Webhook URL",
      description: "Slack webhook URL for sending notifications",
      secret: true,
    },
    repoFullname: {
      propDefinition: [
        github,
        "repoFullname",
      ],
      description: "GitHub repository to monitor for commits and issues",
    },
    backupFolder: {
      type: "string",
      label: "Backup Folder Name",
      description: "Name of the folder to create for backups in cloud storage",
      default: "GitHub-Backups",
    },
    syncBetweenClouds: {
      type: "boolean",
      label: "Sync Between Cloud Storage",
      description: "Enable syncing files between Google Drive and Dropbox",
      default: true,
    },
    enableCommitTracking: {
      type: "boolean",
      label: "Enable Commit Tracking",
      description: "Track and backup new commits automatically",
      default: true,
    },
    enableIssueManagement: {
      type: "boolean",
      label: "Enable Issue Management",
      description: "Automatically manage and track GitHub issues",
      default: true,
    },
  },
  methods: {
    async sendSlackNotification(message, channel = "#general") {
      if (!this.slackWebhook) return;
      
      try {
        await axios(this, {
          method: "POST",
          url: this.slackWebhook,
          data: {
            text: message,
            channel: channel,
            username: "Workflow Orchestrator",
            icon_emoji: ":robot_face:",
          },
        });
      } catch (error) {
        console.error("Failed to send Slack notification:", error);
      }
    },

    async createBackupStructure() {
      const timestamp = new Date().toISOString().split('T')[0];
      
      // Create backup folders in Google Drive
      try {
        const driveFolder = await this.google_drive.createFolder({
          name: `${this.backupFolder}-${timestamp}`,
          fields: "id,name",
        });
        console.log("Created Google Drive backup folder:", driveFolder.name);
        return { driveFolder };
      } catch (error) {
        console.error("Error creating Google Drive folder:", error);
        return {};
      }
    },

    async syncFilesBetweenClouds() {
      if (!this.syncBetweenClouds) return;

      try {
        // List recent files from Google Drive
        const driveFiles = await this.google_drive.listFilesInPage(null, {
          pageSize: 10,
          orderBy: "modifiedTime desc",
          q: "mimeType != 'application/vnd.google-apps.folder'",
        });

        if (driveFiles.files && driveFiles.files.length > 0) {
          for (const file of driveFiles.files.slice(0, 3)) { // Sync only 3 most recent
            try {
              // Download from Google Drive
              const fileContent = await this.google_drive.getFile(file.id, { alt: "media" });
              
              // Upload to Dropbox
              await this.dropbox.uploadFile({
                path: `/synced-files/${file.name}`,
                contents: fileContent,
                mode: "overwrite",
                autorename: true,
              });
              
              console.log(`Synced file: ${file.name}`);
            } catch (syncError) {
              console.error(`Failed to sync file ${file.name}:`, syncError);
            }
          }
        }
      } catch (error) {
        console.error("Error syncing files between clouds:", error);
      }
    },

    async backupRepositoryData() {
      if (!this.enableCommitTracking) return;

      try {
        // Get recent commits
        const commits = await this.github.getCommits({
          repoFullname: this.repoFullname,
          per_page: 5,
        });

        const backupData = {
          repository: this.repoFullname,
          timestamp: new Date().toISOString(),
          commits: commits.map(commit => ({
            sha: commit.sha,
            message: commit.commit.message,
            author: commit.commit.author,
            date: commit.commit.author.date,
          })),
        };

        // Save to Google Drive
        const backupContent = JSON.stringify(backupData, null, 2);
        const fileName = `commit-backup-${Date.now()}.json`;
        
        await this.google_drive.createFile({
          name: fileName,
          mimeType: "application/json",
          file: Buffer.from(backupContent),
        });

        // Also backup to Dropbox
        await this.dropbox.uploadFile({
          path: `/${this.backupFolder}/${fileName}`,
          contents: backupContent,
          mode: "add",
          autorename: true,
        });

        return {
          commits: commits.length,
          backupFile: fileName,
        };
      } catch (error) {
        console.error("Error backing up repository data:", error);
        return { commits: 0 };
      }
    },

    async manageGitHubIssues() {
      if (!this.enableIssueManagement) return;

      try {
        // Get recent issues
        const issues = await this.github.getRepositoryIssues({
          repoFullname: this.repoFullname,
          state: "open",
          per_page: 10,
        });

        const highPriorityIssues = issues.filter(issue => 
          issue.labels.some(label => 
            label.name.toLowerCase().includes('urgent') || 
            label.name.toLowerCase().includes('critical') ||
            label.name.toLowerCase().includes('high priority')
          )
        );

        if (highPriorityIssues.length > 0) {
          const issueList = highPriorityIssues.map(issue => 
            `• #${issue.number}: ${issue.title}`
          ).join('\n');

          await this.sendSlackNotification(
            `🚨 High Priority Issues in ${this.repoFullname}:\n${issueList}`,
            "#alerts"
          );
        }

        // Create issue summary document
        const issueSummary = {
          repository: this.repoFullname,
          timestamp: new Date().toISOString(),
          totalIssues: issues.length,
          highPriorityIssues: highPriorityIssues.length,
          issues: issues.map(issue => ({
            number: issue.number,
            title: issue.title,
            state: issue.state,
            labels: issue.labels.map(l => l.name),
            created_at: issue.created_at,
          })),
        };

        const summaryContent = JSON.stringify(issueSummary, null, 2);
        await this.google_drive.createFile({
          name: `issue-summary-${Date.now()}.json`,
          mimeType: "application/json",
          file: Buffer.from(summaryContent),
        });

        return {
          totalIssues: issues.length,
          highPriorityIssues: highPriorityIssues.length,
        };
      } catch (error) {
        console.error("Error managing GitHub issues:", error);
        return { totalIssues: 0, highPriorityIssues: 0 };
      }
    },

    async orchestrateWorkflows() {
      const results = {
        timestamp: new Date().toISOString(),
        workflows: {},
      };

      // 1. Create backup infrastructure
      const backupStructure = await this.createBackupStructure();
      results.workflows.backupSetup = backupStructure;

      // 2. Backup repository data
      const commitBackup = await this.backupRepositoryData();
      results.workflows.commitBackup = commitBackup;

      // 3. Manage GitHub issues
      const issueManagement = await this.manageGitHubIssues();
      results.workflows.issueManagement = issueManagement;

      // 4. Sync files between clouds
      await this.syncFilesBetweenClouds();
      results.workflows.cloudSync = { completed: true };

      // 5. Send orchestration summary
      const summary = [
        `🤖 *Workflow Orchestration Complete*`,
        `Repository: ${this.repoFullname}`,
        `Commits backed up: ${commitBackup.commits || 0}`,
        `Issues processed: ${issueManagement.totalIssues || 0}`,
        `High priority issues: ${issueManagement.highPriorityIssues || 0}`,
        `Cloud sync: ${this.syncBetweenClouds ? 'Enabled' : 'Disabled'}`,
        `Timestamp: ${results.timestamp}`,
      ].join('\n');

      await this.sendSlackNotification(summary);

      return results;
    },
  },
  async run({ $ }) {
    try {
      // Validate inputs
      if (!this.repoFullname) {
        throw new Error("Repository name is required for workflow orchestration");
      }

      // Initialize orchestration
      await this.sendSlackNotification(
        `🚀 Starting automated workflow orchestration for ${this.repoFullname}...`
      );

      // Execute orchestrated workflows
      const orchestrationResults = await this.orchestrateWorkflows();

      // Export summary for Pipedream UI
      const totalWorkflows = Object.keys(orchestrationResults.workflows).length;
      const successfulWorkflows = Object.values(orchestrationResults.workflows)
        .filter(result => result && (result.completed || result.commits !== undefined || result.totalIssues !== undefined)).length;

      $.export("$summary", 
        `Successfully orchestrated ${successfulWorkflows}/${totalWorkflows} automated workflows for ${this.repoFullname}`
      );

      return {
        success: true,
        repository: this.repoFullname,
        orchestrationResults,
        summary: {
          totalWorkflows,
          successfulWorkflows,
          enabledFeatures: {
            commitTracking: this.enableCommitTracking,
            issueManagement: this.enableIssueManagement,
            cloudSync: this.syncBetweenClouds,
          },
        },
      };

    } catch (error) {
      console.error("Workflow orchestration failed:", error);
      
      await this.sendSlackNotification(
        `❌ Workflow orchestration failed: ${error.message}`
      );

      $.export("$summary", `Workflow orchestration failed: ${error.message}`);
      
      return {
        success: false,
        error: error.message,
        repository: this.repoFullname,
      };
    }
  },
})
