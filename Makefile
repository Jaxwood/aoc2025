.PHONY: help install sync test test-v clean upgrade lock

# Default target
help:
	@echo "Available commands:"
	@echo "  make install    - Install all dependencies including dev"
	@echo "  make sync       - Sync dependencies from lock file"
	@echo "  make test       - Run tests with pytest"
	@echo "  make test-v     - Run tests with verbose output"
	@echo "  make upgrade    - Upgrade all dependencies"
	@echo "  make lock       - Update lock file"
	@echo "  make clean      - Remove cache and build files"

# Install dependencies
install:
	mise install

# Sync dependencies from lock file (faster, uses existing lock)
sync:
	uv sync --extra dev

# Run tests
test:
	uv run pytest

# Run tests with verbose output
test-v:
	uv run pytest -v


# Upgrade all dependencies
upgrade:
	uv lock --upgrade

# Update lock file without upgrading
lock:
	uv lock

# Clean cache and build artifacts
clean:
	rm -rf .pytest_cache
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
