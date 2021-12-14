import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Img(
        src='https://d1m75rqqgidzqn.cloudfront.net/wp-data/2019/09/11134058/What-is-data-science-2.jpg',
        style={'width': '50%', 'border': '1px solid red'}),

    html.H1(children='Bernardo Bello', style={'color': 'red', 'backgroundColor': 'green'}),

    html.Div(children='I am a chemical engineer, currently working at Deacero',style={'color': 'red', 'border': '1px solid red'}),

])

if __name__ == '__main__':
    app.run_server(debug=True)