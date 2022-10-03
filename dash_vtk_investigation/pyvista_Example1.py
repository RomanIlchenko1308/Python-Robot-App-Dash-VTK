import pyvista as pv


plotter = pv.Plotter()
plotter.add_mesh(pv.Sphere(), name="mymesh1")
plotter.add_mesh(pv.Plane(direction=(0, 1, 0)), name="mymesh2")
# Only the Plane is shown!
plotter.show()