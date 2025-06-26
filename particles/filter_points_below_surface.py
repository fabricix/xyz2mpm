import numpy as np
import pyvista as pv
import os

def load_xyz(file_name):
    """Loads an XYZ file and returns a NumPy array with 3D points."""
    points = np.loadtxt(file_name)
    if points.ndim != 2 or points.shape[1] < 3:
        raise ValueError("The file must contain at least 3 columns (x, y, z)")
    return points[:, :3]

def save_xyz(file_name, points):
    """Saves points to an XYZ file."""
    np.savetxt(file_name, points, fmt="%.6f")

def save_vtp(file_name, points):
    """Saves points to a VTP file for visualization."""
    cloud = pv.PolyData(points)
    cloud["ID"] = np.arange(1, len(points) + 1)
    cloud.save(file_name)

def filter_points_below_surface(points, mesh):
    """
    Filters out points that are not below the STL surface
    using ray tracing from each point downward in Z.
    """
    filtered_points = []
    for p in points:
        _, intersections = mesh.ray_trace(p, p + np.array([0, 0, -1]) * 1e3)
        if intersections.shape[0] > 0:
            filtered_points.append(p)
    return np.array(filtered_points)

def filter_material_points_below_surface(points_file, stl_file):
    """
    Filters material points to ensure they are below the STL surface.
    Returns the filtered XYZ and VTP file paths.
    """
    if not os.path.isfile(points_file) or not os.path.isfile(stl_file):
        raise FileNotFoundError("Check that both the points file and STL file exist.")

    points = load_xyz(points_file)
    mesh = pv.read(stl_file).extract_surface().triangulate()
    filtered = filter_points_below_surface(points, mesh)

    xyz_out = points_file.replace(".xyz", "_filtered.xyz")
    vtp_out = points_file.replace(".xyz", "_filtered.vtp")

    save_xyz(xyz_out, filtered)
    save_vtp(vtp_out, filtered)

    return xyz_out, vtp_out
