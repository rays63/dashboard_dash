from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash_table import DataTable
from django_plotly_dash import DjangoDash
from home.models import CONT_Y

# Create a Dash application
app = DjangoDash('Scat_plot')

data = CONT_Y.objects.all()

df = pd.DataFrame(list(data.values('year', 'co2','country','co2_per_cap')))


# Find the range of years in the dataset
min_year = df['year'].min()
max_year = df['year'].max()

# Assuming `df` is a DataFrame with the data from your CONT_Y model
# Initial scatter plot will show all data
fig = px.scatter(df, x='year', y='co2_per_cap', color='country',
                 size='co2', hover_data=['country'], title='CO2 Emissions per cap scatter chart')

year_range = list(range(df['year'].min(), df['year'].max() + 1, 10))
# Define the layout for the Dash app, including the scatter plot and range slider
app.layout = html.Div([
    dcc.Graph(id='scatter-plot', figure=fig),
    dcc.RangeSlider(
        id='year-slider',
        min=min_year,
        max=max_year,
        value=[min_year, max_year],  # default value to be the full range
        marks={str(year): str(year) for year in year_range},
        step=1,
        allowCross=False
    )
])

# Define callback to update the scatter plot based on the selected year range
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('year-slider', 'value')]
)
def update_figure(selected_years):
    filtered_df = df[(df['year'] >= selected_years[0]) & (df['year'] <= selected_years[1])]
    fig = px.scatter(filtered_df, x='year', y='co2_per_cap', color='country',
                     size='co2', hover_data=['country'], title='CO2 Emissions per cap scatter chart')
    return fig