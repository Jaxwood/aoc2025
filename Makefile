.PHONY: help install sync test test-v test-cov clean lint format check upgrade lock

# Default target
help:
	@echo "Available commands:"
	@echo "  make install    - Install all dependencies including dev"
	@echo "  make sync       - Sync dependencies from lock file"
	@echo "  make test       - Run tests with pytest"
	@echo "  make test-v     - Run tests with verbose output"
	@echo "  make test-cov   - Run tests with coverage report"
	@echo "  make lint       - Run linting checks"
	@echo "  make format     - Format code"
	@echo "  make check      - Run lint and tests"
	@echo "  make upgrade    - Upgrade all dependencies"
	@echo "  make lock       - Update lock file"
	@echo "  make clean      - Remove cache and build files"

# Install dependencies
install:
	mise install
	uv sync --extra dev

# Sync dependencies from lock file (faster, uses existing lock)
sync:
	uv sync --extra dev

# Run tests
test:
	uv run pytest

# Run tests with verbose output
test-v:
	uv run pytest -v

# Run tests with coverage
test-cov:
	uv run pytest --cov --cov-report=html --cov-report=term

# Lint code (if using ruff)
lint:
	uv run ruff check .

# Format code (if using ruff)
format:
	uv run ruff format .

# Run both linting and tests
check: lint test

# Upgrade all dependencies
upgrade:
	uv lock --upgrade

# Update lock file without upgrading
lock:
	uv lock

# Clean cache and build artifacts
clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf .ruff_cache
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
