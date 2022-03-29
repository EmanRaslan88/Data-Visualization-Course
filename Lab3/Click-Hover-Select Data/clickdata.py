from dash import dcc, Dash,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import json

app = Dash()
df = pd.read_csv('wheels.csv')
fig=px.scatter(df,x='color',y='wheels',color='color', size='wheels', color_discrete_map={
                "red": "red",
                "blue": "blue",
                "yellow": "yellow"
                })
app.layout = html.Div([
    
    html.Div([
    dcc.Graph(
        id='wheels-plot',
        figure=fig
    )], style={'width':'50%', 'float':'left'}),

    html.Div([
    html.Img(id='click-image',src=app.get_asset_url('choose.png'),height=300),
    ], style={'paddingTop':35}),


    html.Div([
    html.Div(id='selection', style={'paddingTop':25})
    ], style={'width':'30%', 'display':'inline-block', 'verticalAlign':'top'})
])

@app.callback(
    Output('click-image', 'src'),
    Output('selection', 'children'),
    Input('wheels-plot', 'hoverData'))#hoverData#clickData#selectedData
def callback_image(clickData):
    
    wheel=clickData['points'][0]['y']
    color=clickData['points'][0]['x']
    return app.get_asset_url(df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0]),json.dumps(clickData, indent=2)

if __name__ == '__main__':
    app.run_server()