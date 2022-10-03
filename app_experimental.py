import dash
from dash import Dash, dcc, html, Input, Output, ctx
import dash_vtk
from dash_vtk.utils import to_mesh_state
import pyvista as pv
from dash.exceptions import PreventUpdate
import pandas as pd


# ---------------------------------------------------------
def place_robot(input_x=0, input_y=0, input_f=0):
    # ---
    directions = ["North", "West", "South", "East"]

    # ---
    # Import 3D model
    filename = pv.read("Simplified_Robot.stl")
    filename.scale([0.1, 0.1, 0.1])

    # ---
    # XY rotation on 90 deg around z axis
    filename.rotate_vector((0, 0, 1), input_f)

    # ---
    # filename.origin(5, 5, 0)
    filename.translate([input_x, input_y, 0.5])

    # ---
    mesh = pv.Plane(
        center=(2, 2, 0),
        direction=(0, 0, 1),
        i_size=5,
        j_size=5,
        i_resolution=5,
        j_resolution=5
    )

    # ---
    mesh = mesh.merge(filename)
    mesh_state = to_mesh_state(mesh)

    return mesh_state


# ---------------------------------------------------------
def txt_output_file(txt_output: str):
    list_txt_output = txt_output.split("\n")
    df = pd.DataFrame(list_txt_output, columns=['Commands'])
    df[['Commands', 'Coord: X', 'Coord: Y', "Vector: F"]] = df['Commands'].str.split(',', expand=True)
    return str(df)

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
            ], className="button", id="home-btn", n_clicks=0),
            html.Div(children=[
                html.Div(children=[
                    dcc.Input(id='input-x', className="inputBox inputX", value=1, min=1, max=5, type='number'),
                    dcc.Input(id='input-y', className="inputBox inputY", value=1, min=1, max=5, type='number'),
                    dcc.Input(id='input-f', className="inputBox inputF", value=0, min=-360, max=360, step=90,
                              type='number'),
                ], className="inputBoxesBlock"),
                html.Button(children=[
                    html.Div("Place", className="btnText"),
                    html.Div(children=[
                        html.Div(
                            children=[
                                html.Img(src="/assets/img/robot_place_icon.svg", className="robNavLogo")],
                            className="btnText2")
                    ], className="btnTwo"),
                ], className="button", id="place-btn", n_clicks=0),
            ], className="enterPlaceBox"),

            html.Button(children=[
                html.Div("Left", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_turn_left_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", id="left-btn", n_clicks=0),
            html.Button(children=[
                html.Div("Right", className="btnText"),
                html.Div(children=[
                    html.Div(
                        children=[
                            html.Img(src="/assets/img/robot_turn_right_icon.svg", className="robNavLogo")],
                        className="btnText2")
                ], className="btnTwo"),
            ], className="button", id="right-btn", n_clicks=0),

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
                id="text-area",
                className='textArea',
                value='HOME,X,Y,F',
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
            ], className="button", id="btn-download-txt", n_clicks=0),
            dcc.Download(id="download-text"),
        ], className="manualMenu manualTextBtnBackground"),
    ], className="manualCommandsFlow")
], className="bodyDiv")


@app.callback(
    Output(component_id='my-output', component_property='state'),
    Output(component_id='input-x', component_property='value'),
    Output(component_id='input-y', component_property='value'),
    Output(component_id='input-f', component_property='value'),
    Output(component_id='home-btn', component_property='n_clicks'),
    Output(component_id='place-btn', component_property='n_clicks'),
    Output(component_id='left-btn', component_property='n_clicks'),
    Output(component_id='right-btn', component_property='n_clicks'),
    Output(component_id='text-area', component_property='value'),
    Input(component_id='input-x', component_property='value'),
    Input(component_id='input-y', component_property='value'),
    Input(component_id='input-f', component_property='value'),
    Input(component_id='home-btn', component_property='n_clicks'),
    Input(component_id='place-btn', component_property='n_clicks'),
    Input(component_id='left-btn', component_property='n_clicks'),
    Input(component_id='right-btn', component_property='n_clicks'),
    Input(component_id='text-area', component_property='value'),
)
def update_place_btn(input_x, input_y, input_f,
                     home_clicks, place_clicks,
                     left_click, right_click,
                     text_area):
    # text_area

    # check which button was clicked:
    button_clicked = ctx.triggered_id
    print(button_clicked)

    # Home Button
    if button_clicked == "home-btn":
        home_clicks, place_clicks = 0, 0
        input_x, input_y, input_f = 1, 1, 0
        text_area += f"\nHOME,{input_x},{input_y},{input_f}"

    # Place Button
    if button_clicked == "place-btn":
        text_area += f"\nPLACE,{input_x},{input_y},{input_f}"

    # Turn Left Button
    if button_clicked == "left-btn":
        input_f = input_f + 90
        print(f"--> Left, angel is: {input_f}")

        if input_f == 360:
            input_f = 0

        text_area += f"\nLEFT,{input_x},{input_y},{input_f}"

    # Turn Right Button
    if button_clicked == "right-btn":
        input_f = input_f - 90

        if input_f == -360:
            input_f = 0
        print(f"--> Right, angel is: {input_f}")

        text_area += f"\nRIGHT,{input_x},{input_y},{input_f}"

    # text_area = "0"
    return place_robot(input_x - 1, input_y - 1, input_f), \
           input_x, input_y, input_f, \
           home_clicks, place_clicks, \
           left_click, right_click, text_area


@app.callback(
    Output("download-text", "data"),
    Input(component_id='text-area', component_property='value'),
    Input("btn-download-txt", "n_clicks"),
    prevent_initial_call=True,
)
def func(text_output_str, n_clicks):
    button_clicked = ctx.triggered_id

    if button_clicked == "btn-download-txt":
        text = txt_output_file(text_output_str)
        return dict(content=text, filename="hello.txt")


if __name__ == '__main__':
    app.run_server(debug=True)
