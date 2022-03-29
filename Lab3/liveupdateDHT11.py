import dash
from dash.dcc.Interval import Interval
from dash.html.Div import Div
import serial 
import time
from dash import html 
from dash import dcc
from dash.dependencies import Input,Output,State
from collections import deque
import plotly.express as px
import dash_daq as daq
import numpy as np

'''
device = 'COM3' #this will have to be changed to the serial port you are using
while True:
    try:
      print ("Trying...",device )
      arduino = serial.Serial(device, 9600)
      break
    except: 
      print ("Failed to connect on",device)

max_length = 50
times = deque(maxlen=max_length)
Tempreature = deque(maxlen=max_length)
Humidity = deque(maxlen=max_length)


def update_sensor_data():
  i=0
  while True:
    
      time.sleep(4)
      data = arduino.readline()  #read the data from the arduino
      print(data)
      pieces = data.decode ( 'utf-8' ).split(",")  #split the data by the tab   
      Tempreature.append(pieces[0])
      Humidity.append(pieces[1])
      times.append(i)
      i=i+1

 '''  


app=dash.Dash(__name__, external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout=html.Div([
                        html.H1('RealTime DHT11 Arduino Example ',style={'textAlign':'center', 'color':'blue'}),
                        dcc.Interval(id='timing',interval=10000,n_intervals=0),
                        html.Div([
                                    html.Div([html.H1('Humidity'),
                                            daq.Gauge(
                                              id='my-daq-gauge',
                                              min=0,
                                              max=200
                                                     )
                                             ],style={'textAlign':'center', 'color':'blue', 'backgroundColor':'yellow'}, className="six columns"), 
                                    html.Div([html.H1('Temperature'),
                                            daq.Thermometer(
                                                  id='my-daq-thermometer',
                                                  min=0,
                                                  max=200,
                                                           )
                                              ],style={'textAlign':'center', 'color':'blue', 'backgroundColor':'yellow'}, className="six columns")
                        ],
                        style={'textAlign':'center', 'color':'blue', 'backgroundColor':'yellow'}, className="container")

])


@app.callback(Output('my-daq-thermometer','value'), 
Output('my-daq-gauge','value'), 
Input('timing','n_intervals' ))
def update(value):
      '''time.sleep()
      data = arduino.readline()  #read the data from the arduino
      pieces = data.decode ( 'utf-8' ).split(",")  #split the data by the tab   
      print(pieces[0])
      return float(pieces[1]),float(pieces[0])'''
      return np.random.randint(10,200),np.random.randint(10,200)

if __name__ == '__main__':
  app.run_server(debug=True)