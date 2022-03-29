import dash
from dash import html
from dash import dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df=px.data.stocks()
print(df.columns)

fig = px.line(df,x='date',y=['GOOG','AAPL', 'AMZN', 'FB', 'NFLX', 'MSFT'],title='Stocks',log_y=True,markers=True)


app.layout = html.Div(children=[html.H1('Airline Dashboard', 
                                         style={'textAlign': 'center',
                                                'color': '#503D36',
                                                 'font-size': 40}),
                                html.P('Proportion of distance group by month (month indicated by numbers).',
                                        style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(
                                            figure=fig
                                )])
if __name__ == '__main__':
    app.run_server(debug=True)
