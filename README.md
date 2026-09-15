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

## Named arrays and tuning tools

The `fodo_1gev_6d` pyAML configurations (`pyaml/tango/tango-pyaml/fodo_1gev_6d_pyaml.yaml`
and `pyaml/tango/pyaml-cs-oa/fodo_1gev_6d_pyaml-oa.yaml`) declare the arrays and tools
used by the pyAML `examples/use_cases` notebooks, under the same canonical names:

| Name | Description |
|------|-------------|
| `QForTune` | Quadrupoles used for tune correction (all `QF_*` and `QD_*`) |
| `HCorr` / `VCorr` | Horizontal / vertical orbit correctors (`COR_*.hcorrector`, `COR_*.vcorrector`) |
| `BPM` | Beam position monitors (`BPM_*`) |
| `BETATRON_TUNE` | Betatron tune monitor |
| `CHROMATICITY_MONITOR` | Chromaticity monitor (RF frequency scan) |
| `DEFAULT_TUNE_CORRECTION` | Tune correction tool → `SR.tune` (uses `pyaml/trm.json`) |
| `DEFAULT_TUNE_RESPONSE_MATRIX` | Tune response matrix tool → `SR.trm` |
| `DEFAULT_ORBIT_CORRECTION` | Orbit correction tool → `SR.orbit` (uses `pyaml/orm.json`) |
| `DEFAULT_ORBIT_RESPONSE_MATRIX` | Orbit response matrix tool → `SR.orm` |
| `DEFAULT_DISPERSION` | Dispersion measurement tool → `SR.dispersion` |

`pyaml/trm.json` and `pyaml/orm.json` are shared by both configurations; they were
measured in design mode (pyAT) and are loaded automatically.

```python
from pyaml.accelerator import Accelerator
from pyaml_test_lattice import configurations

sr = Accelerator.load(configurations["pyaml/tango/pyaml-cs-oa/fodo_1gev_6d_pyaml-oa.yaml"])
SR = sr.design
SR.tune.set([0.19, 0.28], iter=10, wait_time=0.0)
```
