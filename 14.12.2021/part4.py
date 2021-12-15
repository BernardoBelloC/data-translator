import dash
from dash import dcc
from dash import html
import plotly.express as px
import requests
import io
import pandas as pd
from dash.dependencies import Input, Output

#reading csv in url (raw link)
url = "https://raw.githubusercontent.com/chyld/datasets/main/auto-mpg.csv" # Make sure the url is the raw version of the 
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')),error_bad_lines=False,engine='python')
df['horsepower']=pd.to_numeric(df['horsepower'],errors='coerce')

def label_nice (row):
    if row['cylinders'] == 4:
        return '4 cylinders'
    if row['cylinders'] == 6:
        return '6 cylinders'
    if row['cylinders'] == 8:
        return '8 cylinders'
df.apply (lambda row: label_nice(row), axis=1)
df[' cylinders '] = df.apply (lambda row: label_nice(row), axis=1)

all_dims = ['4 cylinders', '6 cylinders', 
            '8 cylinders']

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Horsepower by cylinders"),
    dcc.Dropdown(
    id="dropdown",
    options=[{"label": x, "value": x} for x in all_dims],
    value='8 cylinders'
    ),
    dcc.Graph(id='graph-with-dropdown'),

])


@app.callback(
    Output('graph-with-dropdown', 'figure'),
    Input('dropdown', 'value'))

def update_figure(dims):
    filtered_df = df[df[' cylinders '] == dims]
    fig = px.histogram(filtered_df,x='horsepower',nbins=30)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)