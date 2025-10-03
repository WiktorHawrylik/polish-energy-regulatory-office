#!/bin/bash
# Development setup script for Polish Energy Regulatory Office library

set -e

echo "🚀 Setting up Polish Energy Regulatory Office development environment..."

# Check if Python 3.9+ is available
python_version=$(python3 --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
required_version="3.9"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.9+ is required. Found: $python_version"
    exit 1
fi

echo "✅ Python version check passed: $python_version"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

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
echo "Next steps:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Start developing!"
echo "  3. Run tests: make test"
echo "  4. Check code quality: make lint"
echo "  5. Format code: make format"
echo ""
echo "Happy coding! 🐍"
