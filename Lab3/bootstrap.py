
from dash import dcc, Dash,html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
import plotly.express as px

df=px.data.gapminder()
fig=px.scatter(df,x="gdpPercap", y="lifeExp", size="pop", color="continent", log_x=True,template='plotly_dark',height=300)
app = Dash(external_stylesheets=[dbc.themes.DARKLY])
app.title = "Analytics!"
card_content = [
    
    dbc.CardBody(
        [
            html.H5("5K", className="card-title"),
            html.P(
                "fees",
                className="card-text",
            ),
        ]
    ), 
]

app.layout = html.Div(
    [   
        
        dbc.Row(dbc.Col(html.Div(html.H2("My Dashboard Example",
		style={'textAlign':'center'}),style = {'padding-bottom' : '1%','padding-bottom' : '1%'}))
         ),
        
        dbc.Row([  
                dbc.Col(dbc.Card(card_content, color="primary", inverse=True), 
						style = {'padding-left' : '30%'}),
                dbc.Col(dbc.Card(card_content, color="danger", inverse=True)),
                dbc.Col(dbc.Card(card_content, color="info", inverse=True),
						style = {'padding-right' : '30%'}),
               
            ],
            className="mb-4",  
        ),
        
        dbc.Row(
            [
                dbc.Col(html.Div(dcc.Graph(figure=fig)),
				style = {'padding-left' : '2%'}),
                dbc.Col(html.Div(dcc.Graph(figure=fig))),
                dbc.Col(html.Div(dcc.Graph(figure=fig)),
				style = {'padding-right' : '2%'}),    
            ], 
        )
    ]
)

if __name__ == "__main__":
    app.run_server()