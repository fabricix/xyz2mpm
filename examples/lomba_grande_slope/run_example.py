from xyz2mpm.main import run_xyz2mpm_pipeline

run_xyz2mpm_pipeline(
    initial_xyz="input/surface_before.xyz",
    failure_xyz="input/surface_failure.xyz",
    dx=2.5, dy=2.5, dz=2.5,
    reduction_factor=2,
    safety_factor=1
)
