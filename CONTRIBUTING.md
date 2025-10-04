# Contributing to Polish Energy Regulatory Office

Thank you for your interest in contributing to this project! This document outlines the process for contributing using Git Flow branching strategy.

## Git Flow Branching Strategy

This repository follows the Git Flow branching model using standard Git commands (no git-flow CLI tool required).

### Branch Structure

- **main**: Production-ready code, protected from direct commits
- **develop**: Integration branch for features, protected from direct commits
- **feature/**: New features and improvements (branches from develop)
- **bugfix/**: Bug fixes for develop branch
- **hotfix/**: Critical fixes for production (branches from main)
- **release/**: Preparation for new releases (branches from develop)

### Branch Protection Rules

1. **No direct commits** to `main` or `develop` branches
2. **Required status checks**: All CI tests must pass before merging
3. **Required reviews**: At least one approving review required
4. **Up-to-date branches**: Branches must be current before merging

## Git Flow Workflow

### 1. Manual Git Flow Setup

We use Git Flow branching strategy without requiring the git-flow CLI tool. All operations can be done with standard Git commands.

### 2. Working with Features

```bash
# Start a new feature (manually)
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

# Work on your feature
# ... make changes, commit regularly ...

# Push feature branch for code review
git push origin feature/your-feature-name
# Then create PR on GitHub: feature/your-feature-name → develop
```

### 3. Working with Bug Fixes

```bash
# Start a bugfix (manually)
git checkout develop
git pull origin develop
git checkout -b bugfix/fix-description

# Work on your fix
# ... make changes, commit ...

# Push bugfix branch for code review
git push origin bugfix/fix-description
# Then create PR: bugfix/fix-description → develop
```

### 4. Working with Hotfixes

```bash
# Start a hotfix (for critical production issues)
git checkout main
git pull origin main
git checkout -b hotfix/1.0.1

# Fix the critical issue
# ... make changes, commit ...

# Push hotfix branch for code review
git push origin hotfix/1.0.1
# Then create PR: hotfix/1.0.1 → main
# After merging to main, also merge to develop
```

### 5. Working with Releases

```bash
# Start a release
git checkout develop
git pull origin develop
git checkout -b release/1.1.0

# Prepare release (update version, changelog, etc.)
# ... make final adjustments ...

# Push release branch for code review
git push origin release/1.1.0
# Then create PR: release/1.1.0 → main
# After merging to main, also merge back to develop
```

## Standard Git Commands for Git Flow

If you prefer explicit Git commands for each workflow:

### Features

```bash
# Start feature
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name

# Work and commit
git add .
git commit -m "feat: your feature description"

# Push and create PR to develop
git push origin feature/your-feature-name
```

### Bug Fixes

```bash
# Start bugfix
git checkout develop
git pull origin develop
git checkout -b bugfix/issue-description

# Work and commit
git add .
git commit -m "fix: bug description"

# Push and create PR to develop
git push origin bugfix/issue-description
```

### Hotfixes

```bash
# Start hotfix
git checkout main
git pull origin main
git checkout -b hotfix/critical-fix

# Work and commit
git add .
git commit -m "hotfix: critical issue description"

# Push and create PR to main
git push origin hotfix/critical-fix
# After merging to main, also merge to develop
```

## Development Workflow

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office

# Add upstream remote
git remote add upstream https://github.com/WiktorHawrylik/polish-energy-regulatory-office.git
```

### 2. Stay Updated

```bash
# Keep your fork updated
git checkout develop
git pull upstream develop
git push origin develop

git checkout main
git pull upstream main
git push origin main
```

### 3. Make Your Changes

- Write your code
- Add tests for new functionality
- Update documentation if needed
- Ensure all tests pass locally

### 4. Test Your Changes

```bash
# Install development dependencies
pip install -e ".[dev,test]"

# Run tests
pytest

# Run linting
flake8 src tests
black --check src tests
isort --check-only src tests

# Run type checking
mypy src
```

### 5. Commit and Push

```bash
# Add and commit your changes
git add .
git commit -m "feat: add new feature description"

# Push to your fork
git push origin feature/your-feature-name
```

### 6. Create a Pull Request

1. Go to the repository on GitHub
2. Click "New Pull Request"
3. Select your branch and provide a clear description
4. Wait for CI checks to pass
5. Request a review

## Commit Message Convention

We use conventional commits:

- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for adding tests
- `refactor:` for code refactoring
- `ci:` for CI/CD changes

## Code Style

- Follow PEP 8
- Use Black for formatting
- Use isort for import sorting
- Add type hints
- Write docstrings for public functions

## Questions?

If you have questions about contributing, please open an issue for discussion.
