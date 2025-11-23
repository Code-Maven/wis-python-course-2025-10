# GitHub Copilot Instructions for WIS Python Course

This repository contains teaching materials and example code for a 10-week beginner Python programming course at the Weizmann Institute of Science.

## Repository Structure

The codebase is organized by day/lecture in folders named `day02/`, `day03/`, `day04/`, etc. Each folder represents a standalone teaching module with example code for that lecture's topics.

**Each day folder is independent** - there are no cross-day imports or shared code between folders. Code is intentionally duplicated across days (e.g., `shapes.py` appears in both `day02/` and `day04/`) for pedagogical purposes.

## Project Configuration

Starting from `day03/`, each folder uses modern Python project configuration:

- **Package management**: Uses `pyproject.toml` (NOT `setup.py`)
- **Dependency management**: Both `pyproject.toml` and `requirements.txt` may be present for teaching purposes
- **Python version**: Varies by day (`>=3.12` or `>=3.13` in `pyproject.toml`)
- **Testing**: Uses `pytest` (included in `[dependency-groups].dev`)

Example from `day03/pyproject.toml`:
```toml
[project]
name = "day03"
requires-python = ">=3.13"
dependencies = ["python-levenshtein>=0.27.3"]

[dependency-groups]
dev = ["pytest>=9.0.0"]
```

## Code Patterns and Conventions

### Module Organization
Each functional piece of code follows this pattern:
1. **Implementation module** (e.g., `shapes.py`, `words.py`) - contains reusable functions with docstrings
2. **Test module** (e.g., `test_shapes.py`, `test_words.py`) - pytest tests with descriptive names
3. **CLI/main script** (e.g., `triangle_area_cli.py`, `main.py`) - demonstrates usage with user interaction

### Function Documentation
All functions include comprehensive docstrings following this format:
```python
def triangle_area(base, height):
    """
    Calculate the area of a triangle using base and height.
    
    Formula: Area = (base * height) / 2
    
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle
    
    Returns:
        float: The area of the triangle
    """
```

### Import Handling
External dependencies are wrapped with error handling for educational purposes:
```python
try:
    from Bio import Entrez, SeqIO
except ImportError:
    print("Error: Biopython is required but not installed.")
    print("Install it with: pip install biopython")
    sys.exit(1)
```

### Testing with pytest
- Test files are named `test_*.py`
- Test functions are named `test_<descriptive_name>()`
- Each test function includes a docstring explaining what it tests
- Use `assert` for simple comparisons (e.g., `assert compare("hello", "hello") == 0`)

Example test pattern from `day03/test_words.py`:
```python
def test_identical_words_same_case():
    """Test identical words with same case."""
    assert compare("hello", "hello") == 0
```

## CLI Argument Patterns

CLI scripts use `argparse` with educational-friendly patterns:

1. Support both positional and optional arguments for flexibility
2. Include help text and examples in the epilog
3. Add `--version` flag for completeness

Example from `day02/triangle_area_cli.py`:
```python
parser = argparse.ArgumentParser(
    description="Calculate the area of a triangle using base and height",
    epilog="Examples:\n  python triangle_area_cli.py 10 5"
)
parser.add_argument('base', nargs='?', type=float, help='Base of the triangle')
parser.add_argument('--version', action='version', version='Triangle Calculator 1.0')
```

## Scientific Computing Focus

The course teaches Python for scientific data processing:
- Uses bioinformatics libraries (e.g., `Biopython` for NCBI database searches in `day04/`)
- Includes algorithm implementations (e.g., Levenshtein distance in `day03/`)
- Works with biological data formats (e.g., FASTA files in `day04/`)

## Running Tests

From any day folder with tests:
```bash
cd day03/  # or day04/
pytest                           # Run all tests
pytest test_words.py -v          # Verbose output
pytest test_words.py::test_name  # Run specific test
```

## Installation Patterns

Install dependencies for a specific day:
```bash
cd day03/
pip install -e .              # Install project dependencies
pip install -e ".[dev]"       # Install with dev dependencies (pytest)
```

Or use requirements.txt (when present):
```bash
pip install -r requirements.txt
```

## When Adding New Code

1. **New day folders**: Create independent modules - avoid importing from other day folders
2. **New functions**: Include comprehensive docstrings with Args/Returns sections
3. **New modules**: Add corresponding test files with pytest
4. **External dependencies**: Add to `pyproject.toml` dependencies, include import error handling
5. **CLI scripts**: Use argparse with help text and examples

## Course Context

This is teaching material for beginners - prioritize clarity and explicit patterns over brevity. Duplicating code across days is intentional for pedagogical independence.
