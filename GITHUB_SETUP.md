# GitHub Repository Setup

This document outlines how to configure the GitHub repository settings using GitHub CLI (gh).

## Setting Repository Description and Topics

You can configure the repository's description and topics using the following GitHub CLI commands:

```bash
# Set repository description
gh repo edit --description "A demonstration project showing different approaches to getting structured outputs from Ollama using JavaScript and Python implementations"

# Add repository topics/tags
gh repo edit --add-topic ollama --add-topic typescript --add-topic python --add-topic structured-data
```

### Individual Commands

#### Set Description Only

```bash
gh repo edit --description "your description here"
```

#### Add Topics/Tags

```bash
gh repo edit --add-topic topic1 --add-topic topic2
```

#### Remove Topics/Tags

```bash
gh repo edit --remove-topic topic1
```

## Additional Repository Settings

The GitHub CLI also supports configuring other repository settings:

```bash
# Enable features
gh repo edit --enable-issues         # Enable issues
gh repo edit --enable-wiki          # Enable wiki
gh repo edit --enable-discussions   # Enable discussions
gh repo edit --enable-projects      # Enable projects

# Configure pull request settings
gh repo edit --enable-auto-merge              # Enable auto-merge
gh repo edit --allow-update-branch            # Allow updating PR branches
gh repo edit --delete-branch-on-merge         # Auto-delete head branches after merge
gh repo edit --enable-squash-merge           # Enable squash merging
gh repo edit --enable-merge-commit           # Enable merge commits
gh repo edit --enable-rebase-merge           # Enable rebase merging

# Set repository visibility (requires additional confirmation)
gh repo edit --visibility public --accept-visibility-change-consequences
```

For a complete list of available settings, run:

```bash
gh repo edit --help
