import numpy as np

INVALID_Z = 3.4028234663852886e+38

def load_xyz(file_name):
    """Loads an XYZ file and filters out invalid Z values."""
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            values = line.strip().split()
            if len(values) == 3:
                x, y, z = map(float, values)
                if z != INVALID_Z:
                    data.append([x, y, z])
    return np.array(data)

def translate_surfaces_to_origin(surface_initial, surface_failure):
    """
    Translates both surfaces so that the minimum point (x, y, z) of the initial surface is at the origin (0, 0, 0).
    """
    min_x, min_y, min_z = np.min(surface_initial, axis=0)

    surface_initial[:, 0] -= min_x
    surface_initial[:, 1] -= min_y
    surface_initial[:, 2] -= min_z

    surface_failure[:, 0] -= min_x
    surface_failure[:, 1] -= min_y
    surface_failure[:, 2] -= min_z

    return surface_initial, surface_failure, (min_x, min_y, min_z)

def save_xyz(output_name, data):
    """Saves the data to an XYZ file."""
    np.savetxt(output_name, data, fmt="%.6f", delimiter=" ")

def save_translation_log(file_name, min_x, min_y, min_z):
    """Saves translation values to a log file."""
    with open(file_name, "w") as file:
        file.write(f"Applied translation:\n")
        file.write(f"Min X: {min_x:.6f}\n")
        file.write(f"Min Y: {min_y:.6f}\n")
        file.write(f"Min Z: {min_z:.6f}\n")

def translate_and_filter(input_initial, input_failure, output_initial="surface_initial_origin.xyz", output_failure="surface_failure_origin.xyz", translation_log="translation.log"):
    surface_initial = load_xyz(input_initial)
    surface_failure = load_xyz(input_failure)

    surface_initial, surface_failure, (min_x, min_y, min_z) = translate_surfaces_to_origin(surface_initial, surface_failure)

    save_xyz(output_initial, surface_initial)
    save_xyz(output_failure, surface_failure)
    save_translation_log(translation_log, min_x, min_y, min_z)

    return output_initial, output_failure, translation_log