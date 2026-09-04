"""Automatic registries for packaged lattice and configuration files."""

from collections.abc import Iterator, KeysView
from importlib.abc import Traversable
from importlib.resources import files
from pprint import pformat


class _Registry:
    """Dictionary-like registry of packaged files.

    Parameters
    ----------
    root : importlib.abc.Traversable
        Directory below which files are discovered recursively.
    """

    def __init__(self, root: Traversable):
        """Create a registry by recursively discovering files below ``root``.

        Parameters
        ----------
        root : importlib.abc.Traversable
            Directory below which files are discovered.
        """
        self._files = {}
        self._descriptions = {}
        self._visit(root)

    def _visit(self, directory: Traversable, prefix: str = "") -> None:
        """Add files in a directory and its subdirectories.

        Parameters
        ----------
        directory : importlib.abc.Traversable
            Directory currently being scanned.
        prefix : str, default: ""
            Relative path accumulated from the registry root.
        """
        for entry in directory.iterdir():
            key = f"{prefix}/{entry.name}" if prefix else entry.name
            if entry.is_file():
                if entry.name.endswith(".description"):
                    continue
                self._files[key] = entry
                description = directory.joinpath(f"{entry.name}.description")
                if description.is_file():
                    self._descriptions[key] = description.read_text(encoding="utf-8").strip()
            elif entry.is_dir():
                self._visit(entry, key)

    def __getitem__(self, key: str) -> str:
        """Return the filesystem path of a packaged resource.

        Parameters
        ----------
        key : str
            Resource path relative to the registry root.

        Returns
        -------
        str
            Filesystem path to the requested packaged resource.
        """
        return str(self._files[key])

    def __iter__(self) -> Iterator[str]:
        """Iterate over registered resource paths.

        Yields
        ------
        str
            Resource path relative to the registry root.
        """
        return iter(self._files)

    def __len__(self) -> int:
        """Return the number of registered files.

        Returns
        -------
        int
            Number of files in the registry.
        """
        return len(self._files)

    def keys(self) -> KeysView[str]:
        """Return the registered resource paths.

        Returns
        -------
        collections.abc.KeysView
            View containing paths relative to the registry root.
        """
        return self._files.keys()

    def __str__(self) -> str:
        """Return the registered resource paths as a pretty-printed list.

        Returns
        -------
        str
            Multiline list representation of paths relative to the registry
            root.
        """
        return repr(self)

    def __repr__(self) -> str:
        """Return registered paths, including any sidecar descriptions."""
        if not self._descriptions:
            return pformat(sorted(self._files))
        entries = (f"{key!r}: {self._descriptions.get(key, '')}" for key in sorted(self._files))
        return "{\n" + ",\n".join(entries) + "\n}"


class Lattices(_Registry):
    """Registry of files in the packaged lattice directory."""


class Configurations(_Registry):
    """Registry of files in the packaged configuration directory."""


_DATA = files("pyaml_test_lattice") / "data"
# Files discovered below the packaged ``data/lattice`` directory.
lattices = Lattices(_DATA / "lattice")
# Files discovered below the packaged ``data/configuration`` directory.
configurations = Configurations(_DATA / "configuration")
