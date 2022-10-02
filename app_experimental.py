import dash
from dash import Dash, dcc, html, Input, Output
import dash_vtk
from dash_vtk.utils import to_mesh_state
import pyvista as pv


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
app = dash.Dash(__name__)

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div([
        html.Img(src="/assets/img/robot_icon.png", className="robotLogo"),
        html.H2("Robot App"),
        html.A(children=[
            html.Img(src="/assets/img/Github_icon.svg", className="githubLogo")
        ],
            href="https://github.com/RomanIlchenko1308/PythonRobotApp",
            target="_blank",
            className="githubLogo")
    ], className="projectHeader"),
    html.Div([
        html.Div([
            html.Button(children=[
                html.Div("Home", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_home_origin_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
            html.Div(children=[
                html.Div(children=[
                    dcc.Input(id='my-input', className="inputBox inputX", placeholder="X", min=0, max=5, type='number'),
                    dcc.Input(id='input-y', className="inputBox inputY", placeholder="Y", min=0, max=5, type='number'),
                    dcc.Input(id='input-f', className="inputBox inputF", placeholder="F", min=0, max=5, type='number'),
                ], className="inputBoxesBlock"),
                html.Button(children=[
                    html.Div("Place", className="btnText"),
                    html.Div(children=[
                        html.Div(
                            children=[
                                html.Img(src="/assets/img/robot_place_icon.svg", className="robNavLogo")],
                            className="btnText2")
                    ], className="btnTwo"),
                ], className="button", n_clicks=0),
            ], className="enterPlaceBox"),

            html.Button(children=[
                html.Div("Left", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_turn_left_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
            html.Button(children=[
                html.Div("Right", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_turn_right_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),

        ], className="menuButtons menuButtonsBackground"),
        html.Div([
            html.H4("Contact with me:"),
            html.A(children=[
                html.Img(src="/assets/img/LinkedIn_icon.svg", className="githubLogo")
            ],
                href="https://www.linkedin.com/in/romanilichenko/",
                target="_blank",
                className="linkedInLogo")
        ], className="contactWithMe menuButtonsBackground")
    ], className="menuControlFlow"),

    html.Div(
        style={"width": "100%", "height": "100%"},
        children=[
            dash_vtk.View([
                dash_vtk.GeometryRepresentation([
                    dash_vtk.Mesh(id="my-output")
                ], property={
                    "edgeVisibility": True,
                    "edgeColor": (0.5, 0, 0.5),
                    "color": (171 / 100, 235 / 100, 52 / 100)
                }),
            ]),

        ], className="vtkFlow",
    ),
    html.Div([
        html.Div(children=[
            dcc.Textarea(
                className='textArea',
                value='Textarea content initialized\nwith multiple lines of text',
                style={"width": "100%", "height": "300px"},
            ),
            html.Button(children=[
                html.Div("Report", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_report_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
        ], className="manualMenu manualTextBtnBackground"),
    ], className="manualCommandsFlow")
], className="bodyDiv")


@app.callback(
    Output(component_id='my-output', component_property='state'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return cubeModel(range_x_y_z=input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
