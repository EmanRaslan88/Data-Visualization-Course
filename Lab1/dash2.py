import dash
from dash import html
from dash import dcc

app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Dashboard', 
                                         style={'textAlign': 'center',
                                                'color': '#503D36',
                                                 'font-size': 40}),
                                html.P('Proportion of distance group by month (month indicated by numbers).',
                                        style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(
                                            figure={'data':[
                                                {'x':[1,2,3,4,5],'y':[44,66,88,99,100],'label':'NYC','mode':"lines+markers"},
                                                {'x':[1,2,3,4,5],'y':[100,50,44,20,0],'mode':"markers"}
                                            ],
                                            'layout':{'title':'Graph1',  "xaxis": {'title':'x'},"yaxis": {'title':'y'}}}
                                )])
if __name__ == '__main__':
    app.run_server(debug=True)

