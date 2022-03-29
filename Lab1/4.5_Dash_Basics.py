import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc

# ## Load the data
# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Month', names='DistanceGroup', title='Distance group proportion by month')
fig.show()

# Create dash Application
app = dash.Dash(__name__)

app.layout = html.Div(children=[html.H1('Airline Dashboard', 
                                         style={'textAlign': 'center',
                                                'color': '#503D36',
                                                 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by month (month indicated by numbers).',
                                        style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig)])
if __name__ == '__main__':
    app.run_server(debug=True)

