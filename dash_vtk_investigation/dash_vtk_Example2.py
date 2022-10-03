from dash import html, dash
import dash_vtk

import numpy as np
import pyvista

# Make the xyz points


app = dash.Dash(__name__)

app.scripts.config.serve_locally = True

app.layout = html.Div([

    html.Div([dash_vtk.View([
        dash_vtk.GeometryRepresentation(
            children=[
                dash_vtk.PolyData(
                    # create kp
                    points=[
                        0, 0, 0,
                        0, 1, 0,
                        1, 1, 0,
                        1, 0, 0,
                    ],
                    # create lines
                    # lines=[4, 0, 1, 2, 3, 0],
                    # create area
                    polys=[4, 0, 1, 2, 3, 0],

                    children=[
                        dash_vtk.PointData([
                            dash_vtk.DataArray(
                                # registration='setScalars', # To activate field
                                name='onPoints',
                                values=[0, 0.5, 0.75, 1],
                            )
                        ]),
                        dash_vtk.CellData([
                            dash_vtk.DataArray(
                                # registration='setScalars', # To activate field
                                name='onCells',
                                values=[0, 1],
                            )
                        ])
                    ],
                ),
            ],
        ),
    ])], style={"width": "100%", "height": "400px"})])

if __name__ == '__main__':
    app.run_server(debug=True)
