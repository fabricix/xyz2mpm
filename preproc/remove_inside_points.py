import numpy as np
from scipy.spatial import ConvexHull
from matplotlib import path

def load_xyz(file_name):
    """Loads an XYZ file and returns a NumPy array."""
    return np.loadtxt(file_name, delimiter=" ")

def compute_convex_hull_boundary(surface_failure):
    """Computes the convex hull of the failure surface in the XY plane."""
    hull = ConvexHull(surface_failure[:, :2])
    return surface_failure[hull.vertices, :2]

def remove_points_inside_boundary(surface_initial, boundary):
    """Removes points from the initial surface that fall inside the boundary polygon."""
    polygon = path.Path(boundary)
    inside = polygon.contains_points(surface_initial[:, :2])
    return surface_initial[~inside]

def save_xyz(file_name, data):
    """Saves data to an XYZ file."""
    np.savetxt(file_name, data, fmt="%.6f", delimiter=" ")

def filter_points_inside_failure(initial_surface_file, failure_surface_file, output_file="surface_initial_hole.xyz"):
    surface_failure = load_xyz(failure_surface_file)
    surface_initial = load_xyz(initial_surface_file)

    boundary = compute_convex_hull_boundary(surface_failure)
    filtered_surface = remove_points_inside_boundary(surface_initial, boundary)

    save_xyz(output_file, filtered_surface)
    return output_file