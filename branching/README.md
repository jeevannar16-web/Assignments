# Git Branching Concepts

A comprehensive guide and demo repository for learning all Git branching concepts.

## What's Included

### Documentation
- **[BRANCHING_CONCEPTS.md](BRANCHING_CONCEPTS.md)** - Complete guide covering 30 branching concepts
- **[BRANCHING_STRATEGIES.md](BRANCHING_STRATEGIES.md)** - Popular branching strategies

### Key Concepts Covered

#### Basic Concepts
| Concept | Description |
|---------|-------------|
| Creating Branches | `git branch`, `git checkout -b` |
| Switching Branches | `git checkout`, `git switch` |
| Viewing Branches | `git branch`, `git branch -a` |
| Branch Naming Conventions | Best practices for naming |
| Merging | Fast-forward, 3-way, squash, octopus |
| Merge Conflicts | How to resolve conflicts |
| Deleting Branches | Safe and force delete |
| Renaming Branches | `git branch -m` |

#### Intermediate Concepts
| Concept | Description |
|---------|-------------|
| Cherry-Pick | Apply specific commits |
| Rebase | Reapply commits on new base |
| Interactive Rebase | Edit, squash, reorder commits |
| Stashing | Temporarily save changes |
| Detached HEAD | HEAD points to commit |
| Orphan Branches | Branches with no parent |

#### Advanced Concepts
| Concept | Description |
|---------|-------------|
| Git Reset | Soft, mixed, hard reset |
| Git Revert | Create undo commits |
| Git Bisect | Find bugs with binary search |
| Git Worktrees | Work on multiple branches |
| Git Reflog | Recover lost commits |
| Sparse Checkout | Partial repository checkout |
| Tags vs Branches | Fixed vs movable pointers |
| Branch Protection Rules | GitHub/GitLab settings |

#### Remote & Tracking
| Concept | Description |
|---------|-------------|
| Remote Branches | Push, pull, fetch |
| Tracking Branches | Link local to remote |
| Branch Comparison | `git diff`, `git log` |

## Quick Start

```bash
# Clone the repository
git clone https://github.com/jeevannar16-web/branching.git

# Check out the guide
cat BRANCHING_CONCEPTS.md

# Try the commands yourself
git branch feature-test
git checkout feature-test
echo "Hello" > test.txt
git add . && git commit -m "Test"
git checkout main
git merge feature-test
git branch -d feature-test
```

## Files Overview
- `first.txt` - Original file with branch demo content
- `two.txt` - Demonstrates merge conflict resolution
- `third.cpp` - Original C++ file
- `feature-login.txt` - Feature branch demo
- `feature-signup.txt` - 3-way merge demo
- `cherry-pick-file1.txt` - Cherry-pick demo
- `rebase-demo.txt` - Rebase demo
- `stash-demo.txt` - Stash demo

## All Git Commands Reference

```bash
# Branch Operations
git branch <name>              # Create branch
git checkout -b <name>         # Create and switch
git switch -c <name>           # Create and switch (new)
git switch <name>              # Switch branch
git branch -m <old> <new>      # Rename branch
git branch -d <name>           # Delete merged branch
git branch -D <name>           # Force delete branch

# Merge Operations
git merge <branch>             # Merge branch
git merge --squash <branch>    # Squash merge
git merge --no-ff <branch>     # Force merge commit

# Commit Operations
git cherry-pick <commit>       # Apply specific commit
git revert <commit>            # Create undo commit
git reset --soft HEAD~1        # Soft reset
git reset --hard HEAD~1        # Hard reset

# Rebase Operations
git rebase <branch>            # Rebase onto branch
git rebase -i HEAD~3           # Interactive rebase

# Stash Operations
git stash                      # Stash changes
git stash pop                  # Apply and remove stash
git stash list                 # List all stashes

# Remote Operations
git push -u origin <branch>    # Push with tracking
git fetch --prune              # Prune remote branches
git pull --rebase origin main  # Pull with rebase

# Advanced Operations
git bisect start               # Start binary search
git worktree add <path> <branch>  # Create worktree
git reflog                     # View reflog
git log --graph --all          # Visual branch history
```

## License
Free to use for learning purposes.
