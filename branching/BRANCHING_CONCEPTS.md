# Git Branching Concepts - Complete Guide

## Table of Contents
1. [Creating Branches](#1-creating-branches)
2. [Switching Branches](#2-switching-branches)
3. [Viewing Branches](#3-viewing-branches)
4. [Branch Naming Conventions](#4-branch-naming-conventions)
5. [Merging Branches](#5-merging-branches)
6. [Fast-Forward Merge](#6-fast-forward-merge)
7. [3-Way Merge](#7-3-way-merge)
8. [Squash Merge](#8-squash-merge)
9. [Octopus Merge](#9-octopus-merge)
10. [Merge Conflicts](#10-merge-conflicts)
11. [Deleting Branches](#11-deleting-branches)
12. [Renaming Branches](#12-renaming-branches)
13. [Cherry-Pick](#13-cherry-pick)
14. [Rebase](#14-rebase)
15. [Interactive Rebase](#15-interactive-rebase)
16. [Stashing](#16-stashing)
17. [Detached HEAD](#17-detached-head)
18. [Orphan Branches](#18-orphan-branches)
19. [Remote Branches](#19-remote-branches)
20. [Tracking Branches](#20-tracking-branches)
21. [Branch Comparison](#21-branch-comparison)
22. [Git Reset](#22-git-reset)
23. [Git Revert](#23-git-revert)
24. [Git Bisect](#24-git-bisect)
25. [Git Worktrees](#25-git-worktrees)
26. [Git Reflog](#26-git-reflog)
27. [Git Sparse Checkout](#27-git-sparse-checkout)
28. [Git Tags vs Branches](#28-git-tags-vs-branches)
29. [Branch Protection Rules](#29-branch-protection-rules)
30. [Branching Strategies](#30-branching-strategies)

---

## 1. Creating Branches

A branch is a lightweight movable pointer to a commit.

```bash
# Create a new branch
git branch feature-login

# Create and switch to new branch in one step
git checkout -b feature-signup
# OR (newer Git versions)
git switch -c feature-dashboard

# Create branch from specific commit
git branch feature-hotfix abc1234

# Create branch from another branch
git branch feature-exist feature-login

# Create branch from remote branch
git checkout -b local-branch origin/remote-branch
```

## 2. Switching Branches

```bash
# Switch to existing branch
git checkout feature-login
# OR
git switch feature-login

# Switch back to main
git checkout main
# OR
git switch main

# Switch to last branch
git checkout -

# Create and switch (if branch doesn't exist)
git switch -c new-branch
```

## 3. Viewing Branches

```bash
# List local branches
git branch

# List all branches (local + remote)
git branch -a

# List branches with last commit
git branch -v

# List branches with last commit and upstream info
git branch -vv

# List merged branches
git branch --merged

# List unmerged branches
git branch --no-merged

# List remote branches only
git branch -r

# Filter branches by pattern
git branch --list "feature-*"

# Sort branches by commit date
git branch --sort=-committerdate
```

## 4. Branch Naming Conventions

```bash
# Feature branches
feature/user-authentication
feature/login-page
feature-API-endpoint

# Bug fix branches
bugfix/memory-leak
bugfix/null-pointer
fix/login-error

# Hotfix branches
hotfix/security-vulnerability
hotfix/production-crash

# Release branches
release/v1.0.0
release/2.1.0-beta

# Documentation branches
docs/api-documentation
docs/README-update

# Chore/maintenance branches
chore/dependency-update
chore/ci-cleanup

# Examples with ticket numbers
feature/PROJ-123-add-login
bugfix/PROJ-456-fix-crash
```

## 5. Merging Branches

Merging brings changes from one branch into another.

```bash
# Switch to target branch first
git checkout main

# Merge feature branch into main
git merge feature-login

# Merge without committing (preview changes)
git merge --no-commit feature-login

# Merge with specific strategy
git merge -X theirs feature-login
git merge -X ours feature-login

# Abort a merge
git merge --abort
```

## 6. Fast-Forward Merge

Occurs when the target branch has no new commits since the feature branch was created.

```bash
# Before merge: A-B-C (main) and D-E (feature, branched from B)
# After merge:  A-B-C-D-E (main, fast-forwarded)
git merge feature-branch
# Result: Linear history, no merge commit created

# Force no-fast-forward (create merge commit anyway)
git merge --no-ff feature-branch
```

## 7. 3-Way Merge

Occurs when both branches have diverged with new commits.

```bash
# Before merge: A-B-C-D (main) and A-B-E-F (feature)
# After merge:  A-B-C-D-G (main) --- E-F (feature)
# G = merge commit with two parents
git merge feature-branch
# Result: Merge commit created, non-linear history
```

## 8. Squash Merge

Combines all commits from a branch into a single commit on the target branch.

```bash
# Squash merge (all commits → 1 commit)
git merge --squash feature-login

# Then commit the squashed changes
git commit -m "Add login feature"

# GitHub squash merge (via PR)
# Creates a single commit with all changes
```

## 9. Octopus Merge

Merge multiple branches at once (advanced, used by maintainers).

```bash
# Merge multiple branches simultaneously
git merge branch1 branch2 branch3

# Octopus merge with strategy
git merge -s octopus branch1 branch2 branch3

# Note: Conflicts between branches will cause merge to fail
# Must resolve conflicts between branches first
```

## 10. Merge Conflicts

Conflicts happen when both branches modify the same lines.

```bash
# Git marks conflicts in files:
# <<<<<<< HEAD
# Changes from current branch
# =======
# Changes from incoming branch
# >>>>>>> feature-branch

# Steps to resolve:
# 1. Edit the file to keep desired changes
# 2. Remove conflict markers
# 3. Stage the resolved file
git add <file>
# 4. Complete the merge
git commit

# Use merge tool
git mergetool

# Accept theirs (incoming branch changes)
git checkout --theirs <file>

# Accept ours (current branch changes)
git checkout --ours <file>

# See conflicted files
git diff --name-only --diff-filter=U
```

## 11. Deleting Branches

```bash
# Delete local branch (safe - only if merged)
git branch -d feature-login

# Force delete local branch (even if unmerged)
git branch -D feature-experimental

# Delete multiple branches
git branch -d branch1 branch2 branch3

# Delete remote branch
git push origin --delete feature-login
# OR
git push origin :feature-login

# Delete merged local branches (cleanup)
git branch --merged main | grep -v "main" | xargs git branch -d

# Prune remote-tracking branches
git fetch --prune
```

## 12. Renaming Branches

```bash
# Rename current branch
git branch -m new-name

# Rename specific branch
git branch -m old-name new-name

# Force rename (even if new name exists)
git branch -M old-name new-name

# Rename and push to remote
git branch -m feature-v2
git push origin feature-v2
git push origin --delete feature-v1

# Set upstream after rename
git push -u origin feature-v2
```

## 13. Cherry-Pick

Apply a specific commit from one branch to another without merging everything.

```bash
# Apply a single commit
git checkout main
git cherry-pick abc1234

# Apply multiple commits
git cherry-pick abc1234 def5678

# Apply without committing (stage changes only)
git cherry-pick --no-commit abc1234

# Cherry-pick a range of commits
git cherry-pick abc1234..ghi7890

# Cherry-pick range (inclusive)
git cherry-pick abc1234^..ghi7890

# Cherry-pick merge commit (keep branch history)
git cherry-pick -m 1 <merge-commit-hash>

# Abort cherry-pick
git cherry-pick --abort

# Continue after resolving conflicts
git cherry-pick --continue
```

## 14. Rebase

Reapply commits on top of another base tip. Creates linear history.

```bash
# Rebase current branch onto main
git checkout feature-branch
git rebase main

# Abort rebase
git rebase --abort

# Continue rebase (after resolving conflicts)
git rebase --continue

# Skip current commit during rebase
git rebase --skip

# Rebase onto different branch
git rebase --onto main feature-branch

# Rebase with strategy
git rebase -X theirs main
git rebase -X ours main
```

## 15. Interactive Rebase

Edit, squash, reorder, or drop commits.

```bash
# Interactive rebase (last 3 commits)
git rebase -i HEAD~3

# Interactive rebase from main
git rebase -i main

# Commands in interactive rebase:
# pick   = use commit as-is
# reword = use commit, but edit commit message
# edit   = use commit, but stop for amending
# squash = use commit, but meld into previous commit
# fixup  = like squash, but discard this commit's log message
# drop   = remove commit entirely

# Squash last 3 commits into one
git rebase -i HEAD~3
# Then change 'pick' to 'squash' for commits you want to combine

# Edit a specific commit
git rebase -i abc1234^
# Change 'pick' to 'edit' at the commit you want to modify
```

## 16. Stashing

Temporarily save uncommitted changes to work on something else.

```bash
# Stash current changes
git stash

# Stash with a message
git stash push -m "WIP: login feature"

# Stash including untracked files
git stash -u
git stash --include-untracked

# Stash including ignored files
git stash -a
git stash --all

# List all stashes
git stash list

# Apply most recent stash (keep in stash list)
git stash apply

# Apply and remove most recent stash
git stash pop

# Apply specific stash
git stash apply stash@{2}

# Drop a specific stash
git stash drop stash@{0}

# Clear all stashes
git stash clear

# Show stash diff
git stash show
git stash show -p

# Create branch from stash
git stash branch new-branch stash@{0}
```

## 17. Detached HEAD

HEAD points directly to a commit instead of a branch tip.

```bash
# Enter detached HEAD (checkout a specific commit)
git checkout abc1234

# Enter detached HEAD (checkout a tag)
git checkout v1.0

# Create a branch from detached HEAD
git checkout -b new-branch-from-detached

# Return to a branch
git checkout main

# Warning: Commits in detached HEAD are orphaned
# If you switch away, they may be garbage collected
```

## 18. Orphan Branches

Branches with no parent commit (used for gh-pages, docs).

```bash
# Create orphan branch (no history)
git checkout --orphan gh-pages

# Remove all files from index
git rm -rf .

# Add new content
echo "# Documentation" > index.html
git add index.html
git commit -m "Initial commit for gh-pages"

# Push to remote
git push origin gh-pages

# Common use cases:
# - GitHub Pages (gh-pages branch)
# - Documentation sites
# - Clean project resets
```

## 19. Remote Branches

```bash
# Fetch all remote branches (download but don't merge)
git fetch origin

# Fetch specific remote branch
git fetch origin feature-login

# Show remote branches
git branch -r

# Show all branches (local + remote)
git branch -a

# Push branch to remote
git push origin feature-login

# Set upstream tracking
git push -u origin feature-login

# Push all local branches
git push --all origin

# Push and delete remote branch
git push origin --delete feature-login

# Pull (fetch + merge)
git pull origin main

# Pull with rebase
git pull --rebase origin main

# Prune deleted remote branches
git fetch --prune
```

## 20. Tracking Branches

Local branches that track remote branches.

```bash
# Set tracking for existing branch
git branch --set-upstream-to=origin/feature-login

# Push and set tracking in one step
git push -u origin feature-login

# Show tracking info
git branch -vv

# Remove tracking
git branch --unset-upstream feature-login

# List all tracking branches
git branch -vv | grep "origin/"
```

## 21. Branch Comparison

```bash
# Compare branches
git diff main..feature-login

# Compare branches (show only stats)
git diff --stat main..feature-login

# Compare with branch tip
git diff main...feature-login

# Compare specific files
git diff main..feature-login -- file.txt

# View commit history of a branch
git log feature-login

# View history of branch not in main
git log main..feature-login

# View history of main not in branch
git log feature-login..main

# View commit graph
git log --oneline --graph --all

# View branch timeline
git log --oneline --graph --decorate --all

# Show branches containing a commit
git branch --contains abc1234

# Show branches where commit isHEAD
git branch --points-at HEAD
```

## 22. Git Reset

Move the current branch pointer to a different commit.

```bash
# Soft reset (keep changes in staging area)
git reset --soft abc1234

# Mixed reset (keep changes in working directory, unstage)
git reset --mixed abc1234
git reset abc1234  # default is mixed

# Hard reset (discard all changes)
git reset --hard abc1234

# Reset specific file
git reset abc1234 -- file.txt

# Reset to undo last commit (keep changes)
git reset --soft HEAD~1

# Reset to undo last commit (discard changes)
git reset --hard HEAD~1

# Reset to remote state
git reset --hard origin/main
```

## 23. Git Revert

Create a new commit that undoes changes from a previous commit.

```bash
# Revert a specific commit
git revert abc1234

# Revert without committing (preview)
git revert --no-commit abc1234

# Revert merge commit
git revert -m 1 <merge-commit-hash>

# Revert range of commits
git revert abc1234..def5678

# Revert last commit
git revert HEAD

# Abort revert
git revert --abort
```

## 24. Git Bisect

Binary search to find which commit introduced a bug.

```bash
# Start bisect
git bisect start

# Mark current commit as bad
git bisect bad

# Mark known good commit
git bisect good abc1234

# Git will checkout middle commit
# Test it, then mark as good or bad
git bisect good
# OR
git bisect bad

# Continue until bug is found
# Git will output: "abc1234 is the first bad commit"

# Exit bisect
git bisect reset

# Use automated test script
git bisect run ./test.sh

# Skip current commit
git bisect skip
```

## 25. Git Worktrees

Work on multiple branches simultaneously without switching.

```bash
# Create a new worktree
git worktree add ../branch-worktree feature-login

# Create worktree with new branch
git worktree add -b hotfix ../hotfix-branch main

# List all worktrees
git worktree list

# Remove a worktree
git worktree remove ../branch-worktree

# Prune stale worktree references
git worktree prune

# Move a worktree
git worktree move ../old-path ../new-path
```

## 26. Git Reflog

Record of all HEAD and branch pointer movements.

```bash
# Show reflog for HEAD
git reflog

# Show reflog for specific branch
git reflog show feature-login

# Recover deleted branch
git reflog
# Find the commit hash before deletion
git checkout -b recovered-branch abc1234

# Recover dropped stash
git reflog
# Find stash commit
git stash apply stash@{0}

# Show reflog with date
git reflog --date=iso

# Expire old reflog entries
git reflog expire --expire=30.days

# Run garbage collection (permanent deletion)
git gc --prune=now
```

## 27. Git Sparse Checkout

Work with only specific directories/files.

```bash
# Enable sparse checkout
git sparse-checkout init

# Set directories to include
git sparse-checkout set src/ docs/

# Add more directories
git sparse-checkout add tests/

# List included directories
git sparse-checkout list

# Disable sparse checkout
git sparse-checkout disable

# Show sparse checkout profile
git sparse-checkout list --full-trees
```

## 28. Git Tags vs Branches

```bash
# Tags are fixed pointers (don't move)
# Branches are movable pointers (move with new commits)

# Create lightweight tag
git tag v1.0.0

# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# List tags
git tag
git tag -l "v1.*"

# Push tags to remote
git push origin v1.0.0
git push origin --tags  # push all tags

# Delete tag locally
git tag -d v1.0.0

# Delete tag from remote
git push origin --delete v1.0.0

# Checkout tag (detached HEAD)
git checkout v1.0.0

# Create branch from tag
git checkout -b hotfix v1.0.0
```

## 29. Branch Protection Rules

GitHub/GitLab branch protection settings (configured via web UI).

```bash
# Common protection rules:
# - Require pull request before merging
# - Require status checks to pass
# - Require branch up to date before merging
# - Require signed commits
# - Require linear history
# - Require administrators to follow rules
# - Restrict who can push to matching branches
# - Allow force pushes (disable for main)
# - Allow deletions (disable for main)

# Example: Protected branches
# main - requires PR, 2 reviews, CI passes
# develop - requires PR, 1 review
# release/* - requires PR, no force push
```

## 30. Branching Strategies

### Git Flow
```
main (production)
  |
develop (integration)
  |  \
feature/login  feature/signup
```

### GitHub Flow
```
main
  |  \
feature/login  feature/signup
```

### Trunk-Based Development
```
main (short-lived feature branches)
  |  \
feat/a  feat/b
```

### GitLab Flow
```
main
  |  \
feature/login  feature/signup
  |  \
pre-production  production
```

### Forking Workflow
```
fork (your copy)
  |  \
feature/login  feature/signup
  |
PR → upstream main
```

---

## Quick Reference Commands

| Command | Description |
|---------|-------------|
| `git branch <name>` | Create branch |
| `git checkout -b <name>` | Create and switch |
| `git switch -c <name>` | Create and switch (new) |
| `git switch <name>` | Switch branch |
| `git merge <branch>` | Merge branch |
| `git merge --squash <branch>` | Squash merge |
| `git branch -d <name>` | Delete merged branch |
| `git branch -D <name>` | Force delete branch |
| `git branch -m <old> <new>` | Rename branch |
| `git cherry-pick <commit>` | Apply specific commit |
| `git rebase <branch>` | Rebase onto branch |
| `git rebase -i HEAD~3` | Interactive rebase |
| `git stash` | Stash changes |
| `git stash pop` | Apply and remove stash |
| `git reset --soft HEAD~1` | Soft reset |
| `git reset --hard HEAD~1` | Hard reset |
| `git revert <commit>` | Create undo commit |
| `git bisect start` | Start binary search |
| `git worktree add <path> <branch>` | Create worktree |
| `git reflog` | View reflog |
| `git log --graph --all` | Visual branch history |
| `git push -u origin <branch>` | Push with tracking |
| `git fetch --prune` | Prune remote branches |
