import numpy as np
from scipy.interpolate import LinearNDInterpolator

def load_xyz(file_name):
    """Loads an XYZ file and removes invalid lines."""
    points = []
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 3:
                try:
                    x, y, z = map(float, values)
                    points.append([x, y, z])
                except ValueError:
                    continue
    return np.array(points)

def generate_grid_xy(surface, dx, dy):
    """Generates a regular XY grid within the bounding box of the surface."""
    x_min, x_max = np.min(surface[:, 0]), np.max(surface[:, 0])
    y_min, y_max = np.min(surface[:, 1]), np.max(surface[:, 1])
    x_vals = np.arange(x_min, x_max, dx)
    y_vals = np.arange(y_min, y_max, dy)
    X, Y = np.meshgrid(x_vals, y_vals)
    return X.flatten(), Y.flatten()

def generate_material_points(surface_initial, surface_failure, dx, dy, dz, safety_factor=0):
    """
    Generates 8 material points per cell between initial and failure surfaces,
    offsetting by safety factor along Z.
    """
    interp_initial = LinearNDInterpolator(surface_initial[:, :2], surface_initial[:, 2])
    interp_failure = LinearNDInterpolator(surface_failure[:, :2], surface_failure[:, 2])

    X, Y = generate_grid_xy(surface_failure, dx, dy)
    material_points = []

    for x, y in zip(X, Y):
        z_init = interp_initial(x, y)
        z_fail = interp_failure(x, y)

        if np.isnan(z_init) or np.isnan(z_fail):
            continue
        if z_fail >= z_init:
            continue

        z_fail_adj = z_fail + safety_factor * dz
        z_vals = np.arange(z_fail_adj, z_init, dz)

        for z in z_vals:
            for i in [-0.25, 0.25]:
                for j in [-0.25, 0.25]:
                    for k in [-0.25, 0.25]:
                        px = x + i * dx
                        py = y + j * dy
                        pz = z + k * dz
                        material_points.append([px, py, pz])

    return np.array(material_points)

def save_xyz(file_name, data):
    """Saves material points to an XYZ file."""
    np.savetxt(file_name, data, fmt="%.6f", delimiter=" ")

def generate_material_points_from_xyz(initial_file, failure_file, dx, dy, dz, safety_factor=0.0, output_file="material_points.xyz"):
    surface_initial = load_xyz(initial_file)
    surface_failure = load_xyz(failure_file)
    points = generate_material_points(surface_initial, surface_failure, dx, dy, dz, safety_factor)
    save_xyz(output_file, points)
    return output_file
