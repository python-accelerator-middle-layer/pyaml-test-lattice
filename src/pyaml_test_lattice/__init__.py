"""Paths to the example lattices and configuration files."""

from importlib.resources import files

from ._version import __version__

_DATA = files("pyaml_test_lattice") / "data"

config_dir = _DATA / "configuration"
lattice_dir = _DATA / "lattice"

config_file = config_dir / "fodo_1gev_6d.yaml"
lattice_file = lattice_dir / "fodo_1gev_6d.json"

__all__ = [
    "config_dir",
    "config_file",
    "lattice_dir",
    "lattice_file",
]
