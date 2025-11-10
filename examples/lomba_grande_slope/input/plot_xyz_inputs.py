import os
import numpy as np
import pyvista as pv

INVALID_Z = 3.4028234663852886e+38

def load_xyz_filtered(filepath):
    try:
        data = np.loadtxt(filepath)
        if data.ndim != 2 or data.shape[1] < 3:
            return None
        return data[data[:, 2] != INVALID_Z]
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def plot_xyz_file(filepath, output_dir, point_size=4.0):
    points = load_xyz_filtered(filepath)
    if points is None or points.size == 0:
        print(f"No valid data to plot in {filepath}")
        return

    cloud = pv.PolyData(points[:, :3])
    cloud["Elevation"] = points[:, 2]  # usar Z como escalar

    plotter = pv.Plotter(off_screen=True)
    plotter.set_background("white")
    plotter.add_points(cloud, scalars="Elevation", cmap="viridis", point_size=point_size, render_points_as_spheres=True)
    plotter.view_xy()  # vista en planta
    plotter.reset_camera()

    filename = os.path.splitext(os.path.basename(filepath))[0] + "_topview.png"
    output_path = os.path.join(output_dir, filename)
    plotter.show(auto_close=False)
    plotter.screenshot(output_path)
    plotter.close()
    print(f"Saved top-view image: {output_path}")

def main():
    current_dir = os.getcwd()
    output_dir = os.path.join(current_dir, "figures")
    os.makedirs(output_dir, exist_ok=True)

    for fname in os.listdir(current_dir):
        if fname.endswith(".xyz"):
            plot_xyz_file(os.path.join(current_dir, fname), output_dir)

if __name__ == "__main__":
    main()
