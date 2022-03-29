import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output,State
import plotly.express as px
import pandas as pd
import numpy as np

df=px.data.gapminder()
app=dash.Dash()
app.layout=html.Div([
                        html.H1('Call back Example 3', style={'textAlign':'center'}),
                       
                        dcc.Graph(id='myGraph', figure={}),
                       
                        dcc.Slider(
                                    id='my-slider',
                                    min=df['year'].min(),
                                    max=df['year'].max(),
                                    value=df['year'].min(),
                                    marks={str(years):str(years) for years in df['year'].unique()}
                                ),
                        dcc.Dropdown(
                                        id='demo-dropdown',
                                        options=[ 
                        {'label': str(continent), 'value': str(continent)}  for continent in df['continent'].unique()
                                        ],
                                        value=None,
                                        multi=True,
                                        placeholder='Choose a continent .....',        
                                )

])

@app.callback(
    Output('myGraph','figure'),
    Input('my-slider','value'),
    Input('demo-dropdown','value'))
def update_graph(slidervalue,dropdownvalue):
    if dropdownvalue==None:
        filtered_df=df[(df.year==slidervalue)]
        fig=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", size="pop", color="continent")
    else:
        filtered_df=df[(df.year==slidervalue) & (np.isin(df.continent,dropdownvalue))]
        fig=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", size="pop", color="continent", log_x=True)
    return fig

if __name__=='__main__':
    app.run_server(debug=True)