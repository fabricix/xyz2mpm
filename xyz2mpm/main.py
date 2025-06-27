from xyz2mpm.preproc.translate_and_filter import translate_and_filter
from xyz2mpm.preproc.remove_inside_points import filter_points_inside_failure
from xyz2mpm.preproc.merge_surfaces import merge_surface_files
from xyz2mpm.mesh.generate_stl_from_xyz import generate_stl_from_xyz
from xyz2mpm.particles.generate_material_points import generate_material_points_from_xyz
from xyz2mpm.particles.filter_points_below_surface import filter_material_points_below_surface
from xyz2mpm.particles.convert_xyz_to_json import convert_xyz_to_json_particles
import os

def run_xyz2mpm_pipeline(
    initial_xyz,
    failure_xyz,
    dx, dy, dz,
    reduction_factor=1,
    safety_factor=1,
    output_dir=None
):
    if output_dir is None:
        output_dir = os.getcwd()
    os.makedirs(output_dir, exist_ok=True)

    print("Step 1: Translating and filtering input surfaces...")
    surface_initial, surface_failure, _ = translate_and_filter(initial_xyz, failure_xyz)

    print("Step 2: Removing points inside failure boundary...")
    surface_with_hole = filter_points_inside_failure(surface_initial, surface_failure)

    print("Step 3: Merging initial and failure surfaces...")
    combined_surface = merge_surface_files(surface_with_hole, surface_failure)

    print("Step 4: Generating STL mesh...")
    stl_file = os.path.join(output_dir, "mesh.stl")
    generate_stl_from_xyz(combined_surface, reduction_factor, stl_file)

    print(f"STL mesh saved to: {stl_file}")
    print("You may now open and modify the STL in external tools like MeshLab before continuing.")
    input("Press Enter to continue...")

    print("Step 5: Generating material points between surfaces...")
    material_xyz = generate_material_points_from_xyz(surface_initial, surface_failure, dx, dy, dz, safety_factor)

    print("Step 6: Filtering material points below STL surface...")
    filtered_xyz, _ = filter_material_points_below_surface(material_xyz, stl_file)

    print("Step 7: Converting filtered points to JSON...")
    json_particles = convert_xyz_to_json_particles(filtered_xyz, dx, dy, dz)

    print(f"Pipeline completed successfully. Output: {json_particles}")
    return json_particles

if __name__ == "__main__":
    json_output = run_xyz2mpm_pipeline(
        initial_xyz="examples/lomba_grande_slope/input/surface_before.xyz",
        failure_xyz="examples/lomba_grande_slope/input/surface_failure.xyz",
        dx=5.0, dy=5.0, dz=5.0,
        reduction_factor=2,
        safety_factor=1,
        output_dir="examples/lomba_grande_slope/output"
    )
    print(f"Pipeline completed. JSON particles file: {json_output}")
