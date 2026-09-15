"""Checks that the usage documented in README.md actually works.

These tests double as copy-paste examples: they use the registries exactly
as the README describes, nothing more.
"""

from importlib.resources import files
from pathlib import Path

from pyaml_test_lattice import configurations, lattices

LATTICE_KEY = "fodo_1gev_6d.json"
CONFIGURATION_KEY = "pyaml/tango/tango-pyaml/fodo_1gev_6d_pyaml.yaml"


def test_lattice_registry_returns_an_existing_path():
    lattice_file = lattices[LATTICE_KEY]

    assert Path(lattice_file).is_file()


def test_lattice_registry_returns_a_string_path():
    assert isinstance(lattices[LATTICE_KEY], str)


def test_configuration_registry_returns_an_existing_path():
    config_file = configurations[CONFIGURATION_KEY]

    assert Path(config_file).is_file()


def test_configuration_registry_returns_a_string_path():
    assert isinstance(configurations[CONFIGURATION_KEY], str)


def test_lattice_key_is_listed():
    assert LATTICE_KEY in lattices.keys()


def test_configuration_key_is_listed():
    assert CONFIGURATION_KEY in configurations.keys()


def test_printing_a_registry_shows_its_description():
    # A "<filename>.description" file next to a data file is shown when the
    # registry is printed, as documented in the README. Read the sidecar
    # file's actual content instead of hardcoding it, so this test keeps
    # checking that the registry extracts it correctly even if the
    # description text itself changes.
    description_file = files("pyaml_test_lattice") / "data" / "lattice" / f"{LATTICE_KEY}.description"
    expected_description = description_file.read_text(encoding="utf-8").strip()

    assert expected_description in str(lattices)
