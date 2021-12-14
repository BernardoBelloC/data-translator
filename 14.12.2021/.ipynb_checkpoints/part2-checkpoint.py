import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='2', type='text')
    ]),
    html.Div(id='my-output', style={'fontSize': 24, 'color': 'olive'}),
])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'type: {type(input_value)}, value: {input_value}, squared: {float(input_value)**2}'


if __name__ == '__main__':
    app.run_server(debug=True)