from xyz2mpm.main import run_xyz2mpm_pipeline

run_xyz2mpm_pipeline(
    initial_xyz="input/surface_before.xyz",
    failure_xyz="input/surface_failure.xyz",
    dx=5.0, dy=5.0, dz=5.0,
    reduction_factor=2,
    safety_factor=1
)
