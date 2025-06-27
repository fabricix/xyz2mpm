import os

# Extensiones de archivos generados por el pipeline
extensions_to_delete = [".xyz", ".json", ".vtp", ".stl", ".log"]

# Archivos que deben conservarse aunque coincidan con las extensiones
excluded_files = {
    "run_example.py",
    "README.md"
}

# Carpetas que no deben tocarse
excluded_dirs = {
    "input"
}

def clean_generated_files_in_current_dir():
    current_dir = os.getcwd()
    deleted = 0

    for item in os.listdir(current_dir):
        item_path = os.path.join(current_dir, item)

        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            if ext in extensions_to_delete and item not in excluded_files:
                try:
                    os.remove(item_path)
                    print(f"Deleted: {item}")
                    deleted += 1
                except Exception as e:
                    print(f"Error deleting {item}: {e}")

        elif os.path.isdir(item_path) and item in excluded_dirs:
            print(f"Skipped folder: {item}")

    if deleted == 0:
        print("No generated files found to delete.")
    else:
        print(f"Cleaned {deleted} files.")

if __name__ == "__main__":
    print(f"Cleaning directory: {os.getcwd()}")
    clean_generated_files_in_current_dir()
