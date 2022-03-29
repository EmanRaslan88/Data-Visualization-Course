import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

app=dash.Dash( )

app.layout = html.Div(children=[ 
 
                                # Segment 1
                                html.Div([
                                        html.Div('div1'),
                                        html.Div('div2')
                                ], style={'display': 'flex'}),
                                # Segment 2
                                html.Div([
                                        html.Div(dcc.Graph()),
                                        html.Div(dcc.Graph())
                                ], style={'display': 'flex'}),
                               
                                ])

app.run_server()