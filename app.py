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
            html.Img(src="/assets/img/github_icon.svg", className="githubLogo")
        ],
               href="https://github.com/RomanIlchenko1308/PythonRobotApp",
               className="githubLogo")
    ], className="appGitHub"),
    html.Div([
        html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),
        html.Button('Button 2', id='btn-nclicks-2', n_clicks=0),
        html.Button('Button 3', id='btn-nclicks-3', n_clicks=0),
        html.Button('Button 4', id='btn-nclicks-4', n_clicks=0),
        html.Button('Button 5', id='btn-nclicks-5', n_clicks=0),
        html.Div(["Contact with me:"])
    ], className="menuControlFlow"),
    html.Div([], className="vtkVisualization"),
    html.Div([], className="manualCommands"),
], className="bodyDiv")

if __name__ == '__main__':
    app.run_server(debug=True)
