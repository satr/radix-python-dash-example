import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_latex as dl

app = dash.Dash()

app.layout = html.Div([
    html.H1('Example'),
    html.P(dl.DashLatex(r"""Doc form""")),
    html.Div([html.Div(['Val1.........: ', dcc.Input(id='val1', type='number', value=1)]),
              html.Div(['Val2..........: ', dcc.Input(id='val2', type='number', value=10)]),
              html.P(id='result')], style={'text-align': 'center'}),
    html.P(
    )
], style={'width': '50%', 'font-family': 'Arial'})


@app.callback(Output('result', 'children'), [
    Input('val1', 'value'),
    Input('val2', 'value')]
              )
def get_res(val1, val2):
    return "Sum: {}".format(val1 + val2)


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port="8000")
