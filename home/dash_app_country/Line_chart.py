from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash_table import DataTable
from django_plotly_dash import DjangoDash
from home.models import CONT_Y

app = DjangoDash("Line_chart")

# Sample data (you can replace this with your actual data)
data = CONT_Y.objects.all()

df = pd.DataFrame(list(data.values('year', 'co2','country','co2_coal','co2_gas','co2_oil')))
# df = pd.DataFrame(data)

# Create line charts for each variable
fig_co2 = px.line(df, x='year', y='co2',color='country', title='CO2 Emissions')
fig_co2_coal = px.line(df, x='year', y='co2_coal',color='country', title='CO2 Emissions from Coal')
fig_co2_gas = px.line(df, x='year', y='co2_gas',color='country', title='CO2 Emissions from Gas')
fig_co2_oil = px.line(df, x='year', y='co2_oil',color='country', title='CO2 Emissions from Oil')

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
    ]),  # Add the year slider above the charts
    html.Div(id='chart-content'),
    year_slider
])

@app.callback(
    Output('chart-content', 'children'),
    Input('chart-tabs', 'value'),
    Input('year-slider', 'value')  # Add the year slider as an input to the callback
)
def render_chart(selected_tab, selected_years):
    filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]

    if selected_tab == 'tab-co2':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2', color='country', title='CO2 Emissions'))
    elif selected_tab == 'tab-coal':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2_coal', color='country', title='CO2 Emissions from Coal'))
    elif selected_tab == 'tab-gas':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2_gas', color='country', title='CO2 Emissions from Gas'))
    elif selected_tab == 'tab-oil':
        return dcc.Graph(figure=px.line(filtered_df, x='year', y='co2_oil', color='country', title='CO2 Emissions from Oil'))