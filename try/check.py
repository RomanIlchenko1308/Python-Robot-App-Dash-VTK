import dash
from dash.dependencies import Input, Output
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('Button 1', id='btn1', n_clicks=0),
    html.Button('Button 2', id='btn2', n_clicks=0),
    html.Div(id='msg-container')
])

@app.callback(Output('msg-container', 'children'),
              Output('btn1', 'n_clicks'),
              Output('btn2', 'n_clicks'),
              Input('btn1', 'n_clicks'),
              Input('btn2', 'n_clicks'))
def displayClick(btn1, btn2):
    if btn2 > btn1:
        btn1, btn2 = 0, 0
    msg = "Button 1 clicked {} times, Button 2 clicked {} times".format(btn1, btn2)
    return msg, btn1, btn2

if __name__ == '__main__':
    app.run_server(debug=True)