from dash import Dash, html,dcc
import plotly.express as px
import pandas as pd
fig=px.scatter()

app=Dash( external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout=html.Div([
                    html.Div(dcc.Graph(figure=fig),className='four columns'),
                    html.Div(dcc.Graph(),className='four columns'),
                    html.Div(dcc.Graph(),className='three columns'),
])
if __name__=='__main__':
    app.run_server(debug=True)

