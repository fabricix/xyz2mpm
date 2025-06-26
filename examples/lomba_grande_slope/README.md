# Lomba Grande Slope Example

This example demonstrates how to run the full `xyz2mpm` pipeline using real topographic data from the Lomba Grande slope.

## Input

Place your input files in the `input/` folder:

- `surface_before.xyz`: Topographic surface before the slope event.
- `surface_failure.xyz`: Failure geometry surface.

## How to Run

Make sure you're in the root of the project and run:

```bash
python examples/lomba_grande_slope/run_example.py
```

## Output

The pipeline will generate:

- A merged XYZ surface.
- An STL mesh file.
- A filtered material points XYZ file.
- A particle list JSON file ready for MPM simulations.
