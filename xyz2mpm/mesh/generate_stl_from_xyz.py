import numpy as np
import pyvista as pv
from scipy.spatial import Delaunay

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

def reduce_points(points, reduction_factor):
    """Reduces the number of points for coarser meshes."""
    if reduction_factor > 1:
        return points[::reduction_factor]
    return points

def delaunay_triangulation(points):
    """Generates Delaunay triangulation on the XY plane."""
    return Delaunay(points[:, :2])

def export_to_stl(file_name, points, triangles):
    """Exports triangulated surface to STL using PyVista."""
    faces = np.hstack((np.full((triangles.simplices.shape[0], 1), 3), triangles.simplices)).astype(np.int32)
    mesh = pv.PolyData(points, faces)
    mesh.save(file_name)

def generate_stl_from_xyz(xyz_file, reduction_factor=1, output_file="surface_mesh.stl"):
    points = load_xyz(xyz_file)
    if points.shape[0] == 0:
        raise ValueError("No valid data found in the input file.")

    reduced_points = reduce_points(points, reduction_factor)
    triangles = delaunay_triangulation(reduced_points)
    export_to_stl(output_file, reduced_points, triangles)

    return output_file
