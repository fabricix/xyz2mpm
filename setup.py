from setuptools import setup, find_packages

setup(
    name="xyz2mpm",
    version="0.1.0",
    description="Convert XYZ topography to MPM-ready format",
    author="Fabricio Fernández",
    packages=find_packages(),
    install_requires=[
        "numpy", "scipy", "pyvista", "matplotlib"
    ],
    python_requires=">=3.8"
)