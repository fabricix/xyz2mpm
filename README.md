# xyz2mpm

A modular Python pipeline to convert topographic surfaces (in XYZ format) into MPM-compatible particle domains, including STL mesh generation and particle list creation.

## Features

- Translates surfaces to the origin
- Filters invalid or internal points
- Combines surfaces with failure geometry
- Generates STL meshes with optional resolution control
- Produces uniformly distributed material points
- Filters particles below the STL surface
- Exports particles as JSON list for MPM input

## Installation

From the root of the repository (where `setup.py` is located), run:

```bash
pip install -e .
```

## Project Structure

```
xyz2mpm/
├── xyz2mpm/              # Main package
│   ├── main.py
│   ├── __init__.py
│   ├── preproc/
│   ├── mesh/
│   └── particles/
├── examples/
│   └── lomba_grande_slope/
│       ├── input/
│       ├── output/
│       └── run_example.py
├── requirements.txt
├── setup.py
└── README.md
```
---

## Usage

### Option 1: Run an example
```bash
python examples/lomba_grande_slope/run_example.py
```

### Option 2: Use in Python scripts or notebooks
```python
from xyz2mpm.main import run_xyz2mpm_pipeline

run_xyz2mpm_pipeline(
    initial_xyz="input/surface_before.xyz",
    failure_xyz="input/surface_failure.xyz",
    dx=2.0, dy=2.0, dz=2.0,
    reduction_factor=2,
    safety_factor=0.1
)
```

## Requirements

- Python ≥ 3.8
- Packages: numpy, scipy, pyvista, matplotlib

---

## License

MIT License – see [LICENSE](LICENSE)

---

## Author

Developed by Prof. Dr. Fabricio Fernández – Universidad Católica del Norte