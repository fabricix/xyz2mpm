import numpy as np
import json
import os

def load_xyz(file_name):
    """Loads an XYZ file and returns a NumPy array."""
    return np.loadtxt(file_name, delimiter=" ")

def convert_to_particle_list(points, dx, dy, dz):
    """
    Converts a set of points into a list of JSON particles with ID, position, and volume.
    """
    volume = (dx * dy * dz) / 8
    return [
        {
            "id": i + 1,
            "position": point.tolist(),
            "volume": volume
        }
        for i, point in enumerate(points)
    ]

def save_json(file_name, data):
    """Saves data to a JSON file."""
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def convert_xyz_to_json_particles(xyz_file, dx, dy, dz):
    """
    Converts an XYZ file with material points to a JSON particle list.
    Output file uses the same base name with .json extension.
    """
    points = load_xyz(xyz_file)
    particles = convert_to_particle_list(points, dx, dy, dz)
    json_file = os.path.splitext(xyz_file)[0] + ".json"
    save_json(json_file, particles)
    return json_file
