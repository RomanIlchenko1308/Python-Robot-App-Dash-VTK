from dash import Dash, dcc, html, Input, Output
import dash_vtk
from dash_vtk.utils import to_mesh_state
import pyvista as pv
import numpy as np


# ---------------------------------------------------------
def cubeModel(range_x_y_z=5):
    x = np.arange(-range_x_y_z, range_x_y_z, 1, dtype=np.float32)
    y = np.arange(-range_x_y_z, range_x_y_z, 1, dtype=np.float32)
    z = np.arange(-range_x_y_z, range_x_y_z, 1, dtype=np.float32)
    x, y, z = np.meshgrid(x, y, z)
    grid = pv.StructuredGrid(x[::-1], y[::-1], z[::-1])
    mesh_state = to_mesh_state(grid)
    return mesh_state


# ---------------------------------------------------------
content = dash_vtk.View([
    dash_vtk.GeometryRepresentation([
        dash_vtk.Mesh(state=cubeModel())
    ], property={
        "edgeVisibility": True,
        "edgeColor": (0.5, 0, 0.5)
    }),
])

# ---------------------------------------------------------
app = Dash(__name__)

app.layout = html.Div(
    style={
        "width": "100%",
        "height": "calc(100vh - 16px)"
    },
    children=[
        html.Div("Hello"),
        content
    ],
)

if __name__ == '__main__':
    app.run_server(debug=True)
