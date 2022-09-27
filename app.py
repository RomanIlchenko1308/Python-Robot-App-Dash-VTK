import dash
from dash import dcc
from dash import html


app = dash.Dash('')

app.scripts.config.serve_locally = True

app.layout = html.Div([
    html.Div("Hello Dash App!", style={'color': 'blue', 'fontSize': 14})
], style={'marginBottom': 50, 'marginTop': 25, "backgroundColor": "red"})

if __name__ == '__main__':
    app.run_server(debug=True)
