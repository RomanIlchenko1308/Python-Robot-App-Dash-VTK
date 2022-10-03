import dash
from dash import dcc
from dash import html
import dash_vtk
from dash_vtk.utils import to_mesh_state

try:
    # VTK 9+
    from vtkmodules.vtkImagingCore import vtkRTAnalyticSource
except ImportError:
    # VTK =< 8
    from vtk.vtkImagingCore import vtkRTAnalyticSource

# Use VTK to get some data
data_source = vtkRTAnalyticSource()
data_source.Update()  # <= Execute source to produce an output
dataset = data_source.GetOutput()

# Use helper to get a mesh structure that can be passed as-is to a Mesh
# RTData is the name of the field
mesh_state = to_mesh_state(dataset)

content = dash_vtk.View([
    dash_vtk.GeometryRepresentation([
        dash_vtk.Mesh(state=mesh_state)
    ]),
])

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
            html.Button(children=[
                html.Div("Place", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_place_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
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
            html.Button(children=[
                html.Div("Report", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_report_icon.svg", className="robNavLogo")],
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

    html.Div([
        html.Div(
            style={"width": "100%", "height": "100%"},
            children=[content],
        )
    ], className="vtkVisualization"),
    html.Div([], className="manualCommands"),
], className="bodyDiv")

if __name__ == '__main__':
    app.run_server(debug=True)
