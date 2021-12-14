import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Change the value in the input box and find the value of 2 raised by this exponent"),
    html.Div([
        "Exponent: ",
        dcc.Input(id='input', value='1', type='text')
    ]),
    html.Div(id='result', style={'fontSize': 20, 'color': 'green'}),
])



if __name__ == '__main__':
    app.run_server(debug=True)
  