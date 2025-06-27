import os

# List of common generated files
generated_files = [
    "combined_surface.xyz",
    "mesh.stl",
    "surface_failure_origin.xyz",
    "surface_initial_hole.xyz",
    "surface_initial_origin.xyz",
    "translation.log",
    "particles_raw.xyz",
    "particles_raw_filtered.xyz",
    "particles_raw_filtered.json"
]

def clean_directory(path):
    deleted = 0
    for fname in generated_files:
        fpath = os.path.join(path, fname)
        if os.path.exists(fpath):
            try:
                os.remove(fpath)
                print(f"Deleted: {fname}")
                deleted += 1
            except Exception as e:
                print(f"Error deleting {fname}: {e}")
    if deleted == 0:
        print("No generated files found to delete.")
    else:
        print(f"Cleaned {deleted} generated files.")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Cleaning directory: {current_dir}")
    clean_directory(current_dir)
