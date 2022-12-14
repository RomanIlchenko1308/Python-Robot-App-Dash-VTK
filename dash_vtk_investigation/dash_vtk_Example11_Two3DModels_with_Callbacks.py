from dash import Dash, dcc, html, Input, Output
import dash_vtk
from dash_vtk.utils import to_mesh_state
import pyvista as pv
import numpy as np

# ---------------------------------------------------------
def cubeModel(range_x_y_z):
    # ---
    # x = np.arange(-range_x_y_z, range_x_y_z, 1, dtype=np.float32)
    # y = np.arange(-range_x_y_z, range_x_y_z, 1, dtype=np.float32)
    # z = np.arange(-range_x_y_z, range_x_y_z, 1, dtype=np.float32)
    # x, y, z = np.meshgrid(x, y, z)
    #
    # grid = pv.StructuredGrid(x[::-1], y[::-1], z[::-1])

    # ---
    # grid = pv.Cube(
    #     center=(0.0, 0.0, 0.0),
    #     x_length=range_x_y_z,
    #     y_length=range_x_y_z,
    #     z_length=range_x_y_z)
    # mesh_state = to_mesh_state(grid)

    # ---
    filename = pv.read("cube_10_x_10_x_10mm_moved_z_dir_10mm.stl")
    # filename.rotate_vector((1, 0, 0), 90)
    filename.scale([0.1, 0.1, 0.1])
    # filename.origin(5, 5, 0)
    filename.translate([1, 0, -1])


    # ---
    mesh = pv.Plane()

    # ---
    mesh = mesh.merge(filename)
    mesh_state = to_mesh_state(mesh)

    return mesh_state


# ---------------------------------------------------------
app = Dash(__name__)

app.layout = html.Div(
    style={

        "width": "calc(100vh - 100px)",
        "height": "calc(100vh - 100px)"
    },
    children=[
        html.Div("Hello"),
        html.Div([
            "Input: ",
            dcc.Input(id='my-input', value=1, type='number')
        ]),
        dash_vtk.View([
            dash_vtk.GeometryRepresentation([
                dash_vtk.Mesh(id="my-output")
            ], property={
                "edgeVisibility": True,
                "edgeColor": (0.5, 0, 0.5),
                "color": (171/100, 235/100, 52/100)
            }),
        ]),

    ],
)


@app.callback(
    Output(component_id='my-output', component_property='state'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return cubeModel(range_x_y_z=input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
