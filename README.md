# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025), implemented in Python.

## Prerequisites

- [mise](https://mise.jdx.dev/) (manages Python and uv versions)

## Installation

### Install mise (if not already installed)

```bash
# On macOS and Linux
curl https://mise.run | sh

# Or with Homebrew
brew install mise
```

### Setup the project

```bash
# Clone the repository
git clone https://github.com/yourusername/your-project.git
cd your-project

# Install Python and uv via mise (reads from .mise.toml)
mise install

# Verify installation
mise current
```

### Install project dependencies

```bash
# Clone the repository
git clone https://github.com/yourusername/your-project.git
cd your-project

# Install all dependencies (including dev dependencies)
make install

# Or manually with uv
uv sync --extra dev
```

## Usage

```bash
# Run the application
uv run python your_module.py

# Or if you have a script defined in pyproject.toml
uv run your-script-name
```

## Development

### Running Tests

```bash
# Run all tests
make test

# Run tests with verbose output
make test-v

# Run tests with coverage report
make test-cov
```

### Code Quality

```bash
# Format code
make format

# Run linting
make lint

# Run both linting and tests
make check
```

### Managing Dependencies

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Upgrade all dependencies
make upgrade

# Update lock file
make lock
```

### Other Commands

```bash
# See all available make commands
make help

# Clean cache and build artifacts
make clean
```

## Project Structure

```
.
├── pyproject.toml      # Project metadata and dependencies
├── uv.lock            # Locked dependency versions
├── Makefile           # Development commands
├── tests/             # Test files
│   └── test_*.py
├── src/               # Source code
│   └── your_module/
└── README.md          # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`make check`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/your-project](https://github.com/yourusername/your-project)
