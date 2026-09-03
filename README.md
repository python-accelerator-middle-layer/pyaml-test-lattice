# pyaml-test-lattice

Lattices and configuration files used for pyAML integration tests and tutorials.

## Usage

The package discovers files automatically from its packaged `data/lattice` and
`data/configuration` directories. Access them through separate registries:

```python
from pyaml_test_lattice import configurations, lattices

lattice_file = lattices["fodo_1gev_6d.json"]
config_file = configurations["pyaml/tango/fodo_1gev_6d_pyaml.yaml"]
```

The files can be read as text:

```python
config_text = config_file.read_text()
lattice_json = lattice_file.read_text()
```

New files placed below either data directory are available automatically using
their path relative to that directory.

Optional descriptions can be added without changing the registry. Place a
file named `<filename>.description` next to any lattice or
configuration file. Its text is displayed when printing the registry:

```text
fodo_1gev_6d.json.description
```

To list the available files and their description, print a registry:

```python
print(configurations)
```
