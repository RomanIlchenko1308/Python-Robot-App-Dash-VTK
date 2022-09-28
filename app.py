import dash
from dash import dcc
from dash import html

app = dash.Dash('')

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
                html.Div("Start", className="btnText"),
                html.Div(children=[
                    html.Div("GO!", className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
            html.Div(dcc.Input(id='input-on-submit button', type='text')),
            html.Button(children=[
                html.Div("Place", className="btnText"),
                html.Div(children=[
                    html.Div("GO!", className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
            html.Button(children=[
                html.Div("Left", className="btnText"),
                html.Div(children=[
                    html.Div("GO!", className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
            html.Button(children=[
                html.Div("Right", className="btnText"),
                html.Div(children=[
                    html.Div("GO!", className="btnText2")
                ], className="btnTwo"),
            ], className="button", n_clicks=0),
            html.Button(children=[
                html.Div("Report", className="btnText"),
                html.Div(children=[
                    html.Div("GO!", className="btnText2")
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

    html.Div([], className="vtkVisualization"),
    html.Div([], className="manualCommands"),
], className="bodyDiv")

if __name__ == '__main__':
    app.run_server(debug=True)
