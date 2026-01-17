"""
Test suite for example scripts.
Ensures all example code executes without errors.
"""

import pytest
import os
import sys
import subprocess
from pathlib import Path

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
EXAMPLES_DIR = PROJECT_ROOT / "examples"

def get_python_files(directory):
    """Recursively find all .py files in a directory."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                python_files.append(os.path.join(root, file))
    return python_files

# Find all example scripts
example_scripts = get_python_files(EXAMPLES_DIR)

@pytest.mark.parametrize("script_path", example_scripts)
def test_example_script_executes(script_path):
    """Test that an example script runs without errors."""
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True,
        timeout=10
    )
    
    assert result.returncode == 0, f"Script failed with error:\n{result.stderr}"

def test_all_modules_have_examples():
    """Verify that each module folder has at least one example."""
    for i in range(1, 14):  # Modules 1-13
        module_dir = EXAMPLES_DIR / f"module_{i:02d}"
        if module_dir.exists():
            py_files = list(module_dir.glob("*.py"))
            assert len(py_files) > 0, f"Module {i:02d} has no example files"
