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

def label_nice (row):
    if row['cylinders'] == 4:
        return '4 cylinders'
    if row['cylinders'] == 6:
        return '6 cylinders'
    if row['cylinders'] == 8:
        return '8 cylinders'
df.apply (lambda row: label_nice(row), axis=1)
df['nice_label'] = df.apply (lambda row: label_nice(row), axis=1)

all_dims = ['4 cylinders', '6 cylinders', 
            '8 cylinders']

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-dropdown'),
    dcc.Dropdown(
        id="dropdown",
        options=all_dims,
        value=all_dims[:2],
        multi=True
    )
])


@app.callback(
    Output('graph-with-dropdown', 'figure'),
    Input('dropdown', 'value'))

def update_figure(dims):
    fig = px.histogram(df,x='nice_label',nbins=50)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
