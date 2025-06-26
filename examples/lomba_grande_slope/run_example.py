from xyz2mpm.main import run_xyz2mpm_pipeline

# Run the pipeline using Lomba Grande Slope input surfaces
run_xyz2mpm_pipeline(
    initial_xyz="examples/lomba_grande_slope/input/surface_before.xyz",
    failure_xyz="examples/lomba_grande_slope/input/surface_failure.xyz",
    dx=2.0, dy=2.0, dz=2.0,
    reduction_factor=2,
    safety_factor=0.1
)
