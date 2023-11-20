from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import pandas as pd
import plotly.express as px
from home.models import CONT_E

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('l_chart', external_stylesheets=external_stylesheets)

# Retrieve CO2 data from the database
data = CONT_E.objects.all()

df = pd.DataFrame(list(data.values('year', 'co2','continents','co2_coal','co2_gas','co2_oil')))
# df = pd.DataFrame(data)

# Create line charts for each variable
fig_co2 = px.line(df, x='year', y='co2',color='continents', title='CO2 Emissions')
fig_co2_coal = px.line(df, x='year', y='co2_coal',color='continents', title='CO2 Emissions from Coal')
fig_co2_gas = px.line(df, x='year', y='co2_gas',color='continents', title='CO2 Emissions from Gas')
fig_co2_oil = px.line(df, x='year', y='co2_oil',color='continents', title='CO2 Emissions from oil')

year_range = list(range(df['year'].min(), df['year'].max() + 1, 10))

year_slider = dcc.RangeSlider(
    id='year-slider',
    min=df['year'].min(),
    max=df['year'].max(),
    step=10,
    marks={str(year): str(year) for year in year_range},
    value=[df['year'].min(), df['year'].max()]
)

app.layout = html.Div([
    dcc.Tabs(id='chart-tabs', value='tab-co2', children=[
        dcc.Tab(label='CO2', value='tab-co2'),
        dcc.Tab(label='CO2 from Coal', value='tab-coal'),
        dcc.Tab(label='CO2 from Gas', value='tab-gas'),
        dcc.Tab(label='CO2 from Oil', value='tab-oil'),
    ]),
    year_slider,  # Add the year slider above the charts
    html.Div(id='chart-content')
])

@app.callback(
    Output('chart-content', 'children'),
    Input('chart-tabs', 'value'),
    Input('year-slider', 'value')  # Add the year slider as an input to the callback
)
def render_chart(selected_tab, selected_years):
    filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

    if selected_tab == 'tab-co2':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2', color='continents', title='CO2 Emissions'))
    elif selected_tab == 'tab-coal':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2_coal', color='continents', title='CO2 Emissions from Coal'))
    elif selected_tab == 'tab-gas':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2_gas', color='continents', title='CO2 Emissions from Gas'))
    elif selected_tab == 'tab-oil':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2_oil', color='continents', title='CO2 Emissions from Oil'))
