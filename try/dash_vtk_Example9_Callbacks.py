from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value=1, type='number')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(myValue):
    return html.Div(children=[
        html.Div(f"Hello {myValue}"),
        html.Div("*" * myValue),
    ])


if __name__ == '__main__':
    app.run_server(debug=True)
