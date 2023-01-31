import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/HuWenShin/newborn-analytics/main/newborn.csv")
year = df['Year'].unique()
gender = df['Gender'].unique()

'''
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500&display=swap",
        "rel": "stylesheet"
    },
]
'''

# <a target="_blank" href="https://icons8.com/icon/22409/crying-baby">Crying Baby</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>

app = dash.Dash(__name__)
server = app.server
app.title = "Newborn Analytics"

app.layout = html.Div(
    children = [
        #header
        html.Div(
            children = [
                html.P(children="👶🏻", className="header-emoji"),
                html.H1(children="Newborns in Taiwan", className = "header-title"),
                html.P(children="Analyzing number and gender of newborn babies in Taiwan 🇹🇼, for babies born during 1994-2021", className = "header-description"),
            ], className="header"
        ),

        #menu
        html.Div(
            children = [
                #dropdown
                html.Div(children = "Region", className = "menu-title"),
                dcc.Dropdown(
                    id="region-filter",
                    options=df.Region.unique(),
                    value='Total',
                    clearable=False
                ),
            ], className = "menu"
        ),

        #plot
        html.Div(
            children = [
                #first plot
                html.Div(children = dcc.Graph(id = "number-graph", config = {"displayModeBar": False}, className="card")),
                #second plot
                # html.Div(children = dcc.Graph(id = "ratio-graph", config = {"displayModeBar": False}, className="card"))
            ], className = "wrapper"     
        ), 

    ]
)

@app.callback(Output('number-graph', 'figure'), Input('region-filter', 'value'))

def update_graph(region):
    mask = (df.Region == region)
    fig = px.line(df[mask], x='Year', y='Number of Newborns', color='Gender', title='Trend of Newborn Numbers')
    for d in fig['data']:
        if d['name'] == 'All':
            d['line']['color']='#ab7ce6'
        elif d['name'] == 'Male':
            d['line']['color']='#81b9eb'
        else:
            d['line']['color']='#faacc6'
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
