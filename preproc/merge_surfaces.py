import numpy as np

def load_xyz(file_name):
    """Loads an XYZ file and returns a NumPy array."""
    return np.loadtxt(file_name, delimiter=" ")

def merge_surfaces(surface_initial, surface_failure):
    """Merges the initial surface with the failure surface by stacking their points."""
    return np.vstack((surface_initial, surface_failure))

def save_xyz(file_name, data):
    """Saves data to an XYZ file."""
    np.savetxt(file_name, data, fmt="%.6f", delimiter=" ")

def merge_surface_files(initial_surface_file, failure_surface_file, output_file="combined_surface.xyz"):
    surface_initial = load_xyz(initial_surface_file)
    surface_failure = load_xyz(failure_surface_file)
    merged = merge_surfaces(surface_initial, surface_failure)
    save_xyz(output_file, merged)
    return output_file
