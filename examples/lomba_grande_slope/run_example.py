from xyz2mpm.main import run_xyz2mpm_pipeline

run_xyz2mpm_pipeline(
    initial_xyz="input/surface_before.xyz",
    failure_xyz="input/surface_failure.xyz",
    dx=2.0, dy=2.0, dz=2.0,
    reduction_factor=2,
    safety_factor=0.1
)
