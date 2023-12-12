# Newborn Analytics
![dashboard-landing-page](https://github.com/HuWenShin/newborn-analytics/blob/main/test.gif)

## The Idea

Number of birth tells us a lot about the development of a region, as the birth rate in Taiwan has been declining, I am curious about the overall birth trend in the country over the years and also the differences between regions. 

Additionally, I would like to see whether the gender preference and gender gap has changed over the years, since male babies were traditionally more desired than female babies.

To sum up, I made this interactive visualization of newborn numbers to see the birth trend, gender trend, and differences between regions for babies born in Taiwan during 1994-2021.

## The Process

### Data Set

The data set is collected from the [Gender Statistics Database](https://www.gender.ey.gov.tw/gecdb/Stat_Statistics_Query.aspx?sn=Lm21RKW7az4fHULaHwlb7w%3D%3D&statsn=81ca3xOmq7PeQ19JLb29nw%3D%3D&d=&n=5487), it is an official database released for public use by the Taiwanese Executive Yuan.

### Libraries Used

The three main libraries used to create this interactive dashboard are:

- Dash: contains HTML components that structures the website, and communicates with callbacks and servers
- Plotly: generates graph
- Pandas: reads and access the csv data

```python
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
```

### Frontend Web Design

The Dash library supports HTML frontend design components which builds up the structure, an external CSS file is also included to style the website with customized fonts, colors, and layout.

- Code snippet of the dropdown menu HTML layout using Dash

```python
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
        )
```

- Code snippet of the CSS font, body, and header. I chose a softer font and background colors to match the theme of newborn babies.

```python
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;700&display=swap');

body {
    font-family: 'Baloo 2', cursive;
    margin: 0;
    background-color: #fcf7f7;
}

.header {
    background-color: #d7dfeb;
    height: 288px;
    padding: 16px 0 0 0;
}
```

### Interactive Menu and Line Chart

The interactive parts of the dashboard was written with Python3, using the Dash library for website structure and the Plotly library for plotting the line chart.

When the user changes the option on the dropdown menu, the app issues a callback that updates the line chart immediately.

- **@app.callback** defines the input information (region chosen in the dropdown menu) and connected output of the input criteria (graph figure of the chosen region)
- **def update_graph(region)** takes the input information (region) and filters the data with Pandas, then generates a line graph with the filtered data using Plotly **px.line**, and color codes the lines according to gender.

```python
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
```

### Website Deployment

The interactive dashboard is deployed as a website with Render.
Click [here](https://newborn-analytics.onrender.com/) to access the web app! (sometimes it takes a while to load)

### Future improvements

- Make the html a separate file that links back to the python file
