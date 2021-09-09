import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import pickle


colors = {
    'background': '#111111',
    'text': '#7FDBFF',
}


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.layout = html.Div(style={'backgroundColor': colors['background'],'width':1500,'height':800},children=[
html.P(html.H1(children='APPLICATION TO PREDICT HEALTHCARE COSTS',style={
            'textAlign': 'center',
            'height': '60px',
    'line-height': '60px',
    'border-bottom': 'thin lightgrey solid',
            'color': colors['text']
        })),
html.P([
html.Label('AGE            ',style={
            'color': 'white',
            'font-size':25
        }),
dcc.Input(value='1', type='text', id='g1'),
],style={
            'textAlign': 'center'
        }),
html.Div([
html.Label('BMI            ',style={
            'color': 'white',
            'font-size':25
        }),
dcc.Input(value='0', type='text', id='g2'),
],style={
            'textAlign': 'center'}),
html.Div([
html.Label('NO OF. CHILDREN    ',style={
            'color': 'white',
            'font-size':25
        }),
dcc.Dropdown(id = 'g3',options=[
                                {'label': 'Not Applicable', 'value': '0'},
                                {'label': '1', 'value': '1'},
                                {'label': '2', 'value': '2'},
                                {'label': '3', 'value': '3'},
                                {'label': '4', 'value': '4'},
                                {'label': '5 or above', 'value': '5'}
                            ],style = dict(
                            width = '30%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            )),
],style={
            'textAlign': 'center'}),
html.Div([
html.Label('SEX   ',style={
            'textAlign': 'center',
            'color': 'white',
            'font-size':25
        }),
dcc.Dropdown(id = 'g4',options=[
                                {'label': 'Female', 'value': '0'},
                                {'label': 'Male', 'value': '1'}
                            ],style = dict(
                            width = '30%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            )),
],style={
            'textAlign': 'center'}),
html.Div([
html.Label('SMOKER          ',style={
            'textAlign': 'center',
            'color': 'white',
            'font-size':25
        }),
dcc.Dropdown(id = 'g5',options=[
                                {'label': 'Yes', 'value': '1'},
                                {'label': 'No', 'value': '0'}
                            ],style = dict(
                            width = '30%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            )),
],style={
            'textAlign': 'center'}),
html.Div([
html.Label('REGION          ',style={
            'textAlign': 'center',
            'color': 'white',
            'font-size':25
        }),
dcc.Dropdown(id = 'g6',options=[
                                {'label': 'Northeast', 'value': '0'},
                                {'label': 'Northwest', 'value': '1'},
                                {'label': 'Southeast', 'value': '2'},
                                {'label': 'Southwest', 'value': '3'}
                            ],style = dict(
                            width = '30%',
                            display = 'inline-block',
                            verticalAlign = "middle"
                            )),
],style={
            'textAlign': 'center'}),
html.P([
html.Label('YOUR PREDICTED HEALTHCARE COST IS  $',style={
            'textAlign': 'center',
            'color': 'white',
            'font-size':25
        }),
dcc.Input(value='0', type='text', id='pred')
],style={
            'textAlign': 'center'}),
])

def load_model():
    global model
    # model variable refers to the global variable
    with open('trained_costs_model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    
@app.callback(
Output(component_id='pred', component_property='value'),
[Input(component_id='g1', component_property='value'),
Input(component_id='g2', component_property='value'),
Input(component_id='g3', component_property='value'),
Input(component_id='g4', component_property='value'),
Input(component_id='g5', component_property='value'),
Input(component_id='g6', component_property='value')]
)
def update_prediction(a1, a2, a3, a4, a5, a6):
    new_row = { "age": a1,
               "bmi": a2,
               "children": a3, "Sex": a4,
               "Smoker": a5, "Region": a6}
    new_x = pd.DataFrame.from_dict(new_row,orient = "index").transpose()

    output = model.predict(new_x)
    return output

if __name__ == '__main__':
    load_model()  # load model at the beginning once only
    app.run_server(host='0.0.0.0', port=80)
