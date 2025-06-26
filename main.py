# Main pipeline to convert topographic surfaces into MPM-ready particle files

from xyz2mpm.preproc.translate_and_filter import translate_and_filter
from xyz2mpm.preproc.remove_inside_points import filter_points_inside_failure
from xyz2mpm.preproc.merge_surfaces import merge_surface_files
from xyz2mpm.mesh.generate_stl_from_xyz import generate_stl_from_xyz
from xyz2mpm.particles.generate_material_points import generate_material_points_from_xyz
from xyz2mpm.particles.filter_points_below_surface import filter_material_points_below_surface
from xyz2mpm.particles.convert_xyz_to_json import convert_xyz_to_json_particles

def run_xyz2mpm_pipeline(
    initial_xyz,
    failure_xyz,
    dx, dy, dz,
    reduction_factor=1,
    safety_factor=0.0
):
    # Step 1: Translate and filter original surfaces
    surface_initial, surface_failure, _ = translate_and_filter(initial_xyz, failure_xyz)

    # Step 2: Remove points from initial surface inside failure area
    surface_with_hole = filter_points_inside_failure(surface_initial, surface_failure)

    # Step 3: Merge failure surface into initial surface with hole
    combined_surface = merge_surface_files(surface_with_hole, surface_failure)

    # Step 4: Generate STL mesh from the merged surface
    stl_file = generate_stl_from_xyz(combined_surface, reduction_factor)

    # Step 5: Generate material points between initial and failure surfaces
    material_xyz = generate_material_points_from_xyz(surface_initial, surface_failure, dx, dy, dz, safety_factor)

    # Step 6: Filter out material points below STL surface
    filtered_xyz, _ = filter_material_points_below_surface(material_xyz, stl_file)

    # Step 7: Convert filtered XYZ points to JSON particle list
    json_particles = convert_xyz_to_json_particles(filtered_xyz, dx, dy, dz)

    return json_particles

# Example usage
if __name__ == "__main__":
    json_output = run_xyz2mpm_pipeline(
        initial_xyz="data/input/surface_before.xyz",
        failure_xyz="data/input/surface_failure.xyz",
        dx=2.0, dy=2.0, dz=2.0,
        reduction_factor=2,
        safety_factor=0.1
    )
    print(f"Pipeline completed. JSON particles file: {json_output}")