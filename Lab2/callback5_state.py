import dash
from dash import html
from dash import dcc
from dash.dependencies import Input,Output, State
import plotly.express as px
import pandas as pd
df=px.data.gapminder()
app=dash.Dash()
app.layout=html.Div([
                        html.H1('Call back Example state', style={'textAlign':'center'}),
html.Button(id='submit-button-state', children='Submit',n_clicks=0),
                        dcc.Dropdown(
                                        id='demo-dropdown',
                                        options=[ 
                                           {'label': str(country), 'value': str(country)}  for country in df['continent'].unique()
                                        ],
                                        value=None,
                                        placeholder='Choose a continent .....',
                                    ),
                        dcc.Graph(id='myGraph1', figure={}),
                        dcc.Graph(id='myGraph2', figure={}),
                        dcc.Slider(
                                    id='my-slider',
                                    min=df['year'].min(),
                                    max=df['year'].max(),
                                    value=df['year'].min(),
                                    marks={str(years):str(years) for years in df['year'].unique()}
        ),
])

@app.callback(
    Output('myGraph1','figure'),
    Output('myGraph2','figure')
    State('my-slider','value'),
    State('demo-dropdown','value'),
    Input('submit-button-state', 'n_clicks'))
def update_graph(slidervalue,dropdownvalue,n):
    if dropdownvalue==None:
        filtered_df=df[(df.year==slidervalue)]
        fig1=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", size="pop", color="continent")
        fig2=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", size="pop", color="continent")

    else:
        filtered_df=df[(df.year==slidervalue) & (df.continent==dropdownvalue)] 
        fig1=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", size="pop", color="continent", log_x=True)
        fig2=px.scatter(filtered_df,x="gdpPercap", y="lifeExp", size="pop", color="continent")

    return fig1,fig2





if __name__=='__main__':
    app.run_server(debug=True)
    