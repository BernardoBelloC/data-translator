import dash
from dash import dcc
from dash import html
from dash.dependencies import Output
import plotly.express as px
import requests
import io
import pandas as pd
#reading csv in url (raw link)
url = "https://raw.githubusercontent.com/chyld/datasets/main/auto-mpg.csv" # Make sure the url is the raw version of the 
download = requests.get(url).content
df = pd.read_csv(io.StringIO(download.decode('utf-8')),error_bad_lines=False,engine='python')

##df.to_csv('cars.info.csv')
##df = pd.read_csv('cars.info.csv')
fig = px.scatter(df, x="displacement", y="weight", trendline='ols')

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Displacement vs Weight"),
    html.Img(
        src='https://img.xcitefun.net/users/2013/11/345217,xcitefun-kia-gt4-stinger-concept-3.jpg',
        style={'width': '50%', 'border': '1px solid red'}),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)