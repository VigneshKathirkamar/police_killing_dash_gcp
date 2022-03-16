from cgi import print_directory
from dash import Dash,html,dcc
import plotly.express as px 
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("/home/vignesh/virtual_environments/police_killing/PoliceKillingsUS.csv",encoding="ISO-8859-1")
# print(df.head())
# print(df['gender'])

fig = px.bar(df, x="gender",color="gender", barmode="group")

common_weapons = df.armed.value_counts(dropna=False)[:7]

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: UI for police killing data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)