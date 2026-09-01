# pyaml-test-lattice

Lattices and configuration files used for pyAML integration tests and tutorials.

## Usage

Import the packaged file paths directly:

```python
from pyaml_test_lattice import config_file, lattice_file

print(config_file)
print(lattice_file)
```

The files can be read as text:

```python
config_text = config_file.read_text()
lattice_json = lattice_file.read_text()
```