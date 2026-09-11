"""Keeps the supported Python range honest.

Update MIN_PYTHON / MAX_PYTHON together with `requires-python` in
pyproject.toml and the CI matrix in .github/workflows/unit-tests.yml.
"""

import sys

MIN_PYTHON = (3, 10)
MAX_PYTHON = (3, 14)


def test_running_python_version_is_within_the_supported_range():
    assert MIN_PYTHON <= sys.version_info[:2] <= MAX_PYTHON
