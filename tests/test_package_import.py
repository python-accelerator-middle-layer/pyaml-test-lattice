"""Sanity check that the package can be imported.

This is a regression test for the kind of failure reported against Python
3.14: an import error inside ``pyaml_test_lattice`` (or one of its
submodules) makes this test fail at collection time, on every Python version
the package claims to support.
"""

import pyaml_test_lattice


def test_package_imports_and_has_a_version():
    assert isinstance(pyaml_test_lattice.__version__, str)
    assert pyaml_test_lattice.__version__ != ""
