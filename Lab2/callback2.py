import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output
import plotly.express as px
import pandas as pd

app=dash.Dash()

df=px.data.gapminder()


app.layout=html.Div([

                        html.H1('Call back Example 2', style={'textAlign':'center'}),
                        dcc.Graph(id='myGraph'),
                        dcc.Slider(
                                    id='my-slider',
                                    min=df['year'].min(),
                                    max=df['year'].max(),
                                    value=df['year'].min(),
                                    step=None,
             marks={str(years):str(years) for years in df['year'].unique()}
        )
])
@app.callback(
    Output('myGraph','figure'),
    Input('my-slider','value'))
def update_graph(slidervalue):
    filtered_df=df[df.year==slidervalue]
    fig=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", 
    size="pop", color="continent")
    return fig


if __name__=='__main__':
    app.run_server(debug=True)