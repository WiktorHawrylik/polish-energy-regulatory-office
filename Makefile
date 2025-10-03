.PHONY: help install install-dev test test-all lint format clean docs setup-dev setup-dev-macos

# Default target
help:
	@echo "Available targets:"
	@echo "  setup-dev      - Set up development environment (Linux/Windows)"
	@echo "  setup-dev-macos - Set up development environment with pyenv (macOS)"
	@echo "  install        - Install package in development mode"
	@echo "  install-dev    - Install package with development dependencies"
	@echo "  test           - Run tests"
	@echo "  test-all       - Run tests across all Python versions using tox"
	@echo "  lint           - Run linting checks"
	@echo "  format         - Format code with black and isort"
	@echo "  clean          - Clean build artifacts"
	@echo "  docs           - Build documentation"
	@echo "  pre-commit     - Install pre-commit hooks"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev,test,docs]"

test:
	pytest

test-all:
	tox

lint:
	black --check --diff src tests
	isort --check-only --diff src tests
	flake8 src tests
	mypy src

format:
	black src tests
	isort src tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .tox/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

docs:
	sphinx-build -W -b html docs docs/_build/html

pre-commit:
	pre-commit install

setup-dev:
	./setup_dev.sh

setup-dev-macos:
	./setup_dev_macos.sh

requirements.txt:
	pip-compile pyproject.toml
	pip-compile pyproject.toml
