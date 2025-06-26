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

## Project Structure

```
xyz2mpm/
├── main.py
├── requirements.txt
├── preproc/
├── mesh/
├── particles/
└── examples/
```
---

## Quickstart

### 1. Clone the repository

```bash
git clone https://github.com/fabricix/xyz2mpm.git
cd xyz2mpm
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Place your input `.xyz` files in `data/input/`

- `surface_before.xyz` — topography before the event  
- `surface_failure.xyz` — failure surface

### 4. Run the pipeline

```bash
python main.py
```

This will generate:
- A filtered and merged surface
- An STL mesh file
- A filtered `.xyz` file of material points
- A `.json` file with MPM-ready particles

---

## Requirements

- Python ≥ 3.8
- Packages: numpy, scipy, pyvista, matplotlib

---

## License

MIT License – see [LICENSE](LICENSE)

---

## Author

Developed by Prof. Dr. Fabricio Fernández – Universidad Católica del Norte