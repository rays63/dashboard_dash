from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash_table import DataTable
from django_plotly_dash import DjangoDash
from home.models import CONT_Y

app = DjangoDash('Area_chart')

data = CONT_Y.objects.all().values('country', 'year', 'co2_per_cap')
df = pd.DataFrame(list(data))

# Find the range of years in the dataset
min_year = df['year'].min()
max_year = df['year'].max()

# Initial heatmap will show all data
df_grouped = df.groupby('year')['co2_per_cap'].sum().reset_index()
fig = px.area(df_grouped, x='year', y='co2_per_cap', title='CO2 Emissions Per Capita Over Time')

year_range = list(range(df['year'].min(), df['year'].max() + 1, 10))

# Define the layout for the Dash app, including the area plot and range slider
app.layout = html.Div([
    dcc.Graph(id='heatmap', figure=fig),
    dcc.RangeSlider(
        id='year-slider',
        min=min_year,
        max=max_year,
        value=[min_year, max_year],  # default value to be the full range
        marks={str(year): str(year) for year in year_range},
        step=1
    )
])

# Define callback to update the heatmap based on the selected year range
@app.callback(
    Output('heatmap', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_years):
    # Filter the DataFrame based on the selected year range
    filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]
    df_grouped = filtered_df.groupby('year')['co2_per_cap'].sum().reset_index()
    # Generate the updated figure
    fig = px.area(df_grouped, x='year', y='co2_per_cap', title='CO2 Emissions Per Capita Over Time')
    return fig