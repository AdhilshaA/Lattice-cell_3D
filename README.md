# Lattice Cell and Plane - 3D visualization

This is a simple 3D visualization of a lattice cell and plane.

Given the lattice paramters ($a$, $b$, $c$) and ($\alpha$, $\beta$, $\gamma$), the code generates a 3D visualization of the lattice cell. The code also generates a plane with the given Miller indices ($h$, $k$, $l$) and visualizes the plane in the lattice cell. It also outputs the normal vector to the plane and the angle between the normal vector axes of the lattice cell. This is relevant in crystallography to determine the orientation of the plane in the lattice cell.

After cloning this repository, you can check the `input.txt` file to see the input format. The input file contains the lattice parameters and the Miller indices of the plane. You can modify the input file to change the lattice parameters and the Miller indices of the plane.

To run the code, you can use run `main.py` file. The code will generate a 3D visualization of the lattice cell and the plane. The code uses the `matplotlib` library to generate the 3D visualization.