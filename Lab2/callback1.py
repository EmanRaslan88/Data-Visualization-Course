import dash
from dash import html
from dash import dcc

app=dash.Dash()
app.layout=html.Div([
                dcc.Input(id='my-input', value=None,type='text'),
                html.Div(id='my_Div')
])





from dash.dependencies import Input,Output
@app.callback(
    Output(component_id='my_Div',component_property='children'),
    Input(component_id='my-input',component_property='value')
)
def update_My_Div(input_value):
    if input_value==None:
        return 'hello!!'
    else:
        return 'you write: {}'.format(input_value)

app.run_server()
