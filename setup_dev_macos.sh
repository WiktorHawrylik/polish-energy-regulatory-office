#!/bin/bash
# Development setup script for Polish Energy Regulatory Office library (macOS with pyenv)

set -e

echo "🚀 Setting up Polish Energy Regulatory Office development environment (macOS + pyenv)..."

# Check if Homebrew is installed
if ! command -v brew &> /dev/null; then
    echo "❌ Homebrew is not installed. Please install it first:"
    echo "   /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    exit 1
fi

echo "✅ Homebrew is available"

# Check if pyenv is installed, install if not
if ! command -v pyenv &> /dev/null; then
    echo "📦 Installing pyenv..."
    brew install pyenv
    echo "🔧 Please add the following lines to your ~/.zshrc or ~/.bash_profile:"
    echo "   export PYENV_ROOT=\"\$HOME/.pyenv\""
    echo "   command -v pyenv >/dev/null || export PATH=\"\$PYENV_ROOT/bin:\$PATH\""
    echo "   eval \"\$(pyenv init -)\""
    echo ""
    echo "Then restart your terminal or run: source ~/.zshrc"
    echo "After that, run this script again."
    exit 1
else
    echo "✅ pyenv is installed"
fi

# Check if pyenv-virtualenv is installed, install if not
if ! pyenv commands | grep -q virtualenv; then
    echo "📦 Installing pyenv-virtualenv..."
    brew install pyenv-virtualenv
    echo "🔧 Please add the following line to your ~/.zshrc or ~/.bash_profile:"
    echo "   eval \"\$(pyenv virtualenv-init -)\""
    echo ""
    echo "Then restart your terminal or run: source ~/.zshrc"
    echo "After that, run this script again."
    exit 1
else
    echo "✅ pyenv-virtualenv is installed"
fi

# Define Python version
PYTHON_VERSION="3.9.18"  # Use a specific patch version for consistency
VENV_NAME="pero-3.9"

# Check if Python 3.9 is installed in pyenv, install if not
if ! pyenv versions | grep -q "$PYTHON_VERSION"; then
    echo "📦 Installing Python $PYTHON_VERSION with pyenv..."
    pyenv install $PYTHON_VERSION
else
    echo "✅ Python $PYTHON_VERSION is installed"
fi

# Set pyenv local version for this project
current_local=$(pyenv local 2>/dev/null || echo "none")
if [ "$current_local" != "$PYTHON_VERSION" ]; then
    echo "🔧 Setting pyenv local to $PYTHON_VERSION..."
    pyenv local $PYTHON_VERSION
else
    echo "✅ pyenv local is already set to $PYTHON_VERSION"
fi

# Check if virtual environment exists, create if not
if ! pyenv virtualenvs | grep -q "$VENV_NAME"; then
    echo "📦 Creating pyenv virtualenv $VENV_NAME..."
    pyenv virtualenv $PYTHON_VERSION $VENV_NAME
else
    echo "✅ pyenv virtualenv $VENV_NAME already exists"
fi

# Activate the virtual environment
echo "🔧 Activating pyenv virtualenv $VENV_NAME..."
pyenv shell $VENV_NAME

# Verify Python version
python_version=$(python --version 2>&1 | cut -d' ' -f2)
echo "✅ Using Python version: $python_version"

# Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Install the package in development mode with all dependencies
echo "📚 Installing package in development mode..."
pip install -e ".[dev,test,docs]"

# Install pre-commit hooks
echo "🪝 Installing pre-commit hooks..."
pre-commit install

# Run initial checks
echo "🧪 Running initial checks..."
echo "  - Code formatting check..."
black --check src tests || echo "    ⚠️ Code formatting issues found. Run 'make format' to fix."

echo "  - Import sorting check..."
isort --check-only src tests || echo "    ⚠️ Import sorting issues found. Run 'make format' to fix."

echo "  - Linting check..."
flake8 src tests || echo "    ⚠️ Linting issues found. Review and fix manually."

echo "  - Type checking..."
mypy src || echo "    ⚠️ Type checking issues found. Review and fix manually."

echo "  - Running tests..."
pytest || echo "    ⚠️ Some tests failed. Review and fix manually."

echo ""
echo "🎉 Development environment setup complete!"
echo ""
echo "Environment details:"
echo "  - Python version: $python_version"
echo "  - Virtual environment: $VENV_NAME"
echo "  - pyenv local: $(pyenv local)"
echo ""
echo "Next steps:"
echo "  1. To activate the environment in future sessions: pyenv shell $VENV_NAME"
echo "  2. Start developing!"
echo "  3. Run tests: make test"
echo "  4. Check code quality: make lint"
echo "  5. Format code: make format"
echo ""
echo "Note: The pyenv local setting is saved in .python-version file"
echo "and will be automatically used when you cd into this directory."
echo ""
echo "Happy coding! 🐍"
