Git Branching Strategies
========================

## 1. Feature Branch Strategy
Each feature gets its own branch, merged via pull request.

```
main
  |  \
feature-a  feature-b
```

## 2. Git Flow Strategy
Separate branches for features, releases, and hotfixes.

```
main (production)
  |
develop (integration)
  |  \
feature/login  feature/signup
```

## 3. GitHub Flow Strategy
Simple workflow with feature branches and pull requests.

```
main
  |  \
feat/login  feat/signup
```

## 4. Trunk-Based Development
Short-lived branches, frequent merges to main.

```
main
  |  \
feat/a  feat/b  (short-lived, < 1 day)
```

## Best Practices
- Keep branches short-lived
- Use descriptive branch names
- Delete merged branches
- Use pull requests for code review
- Keep main branch always deployable
- Use feature flags for incomplete features
