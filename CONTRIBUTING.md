# Contributing to Polish Energy Regulatory Office

Thank you for your interest in contributing to this project! This document outlines the process for contributing and the branch protection rules in place.

## Branch Protection Rules

This repository uses branch protection to ensure code quality and prevent direct commits to the main branch.

### Protected Branches

- **main**: The primary branch, protected from direct commits
- **develop**: Development branch (if used)

### Rules in Effect

1. **No direct commits to main**: All changes must go through pull requests
2. **Required status checks**: All CI tests must pass before merging
3. **Required reviews**: At least one approving review required
4. **Up-to-date branches**: Branches must be current with main before merging

## Contributing Workflow

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/polish-energy-regulatory-office.git
cd polish-energy-regulatory-office
```

### 2. Create a Feature Branch

```bash
# Create and switch to a new branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/issue-description
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
