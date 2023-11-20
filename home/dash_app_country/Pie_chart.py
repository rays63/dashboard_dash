from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash_table import DataTable
from django_plotly_dash import DjangoDash
from home.models import CONT_Y

# Create a Dash application
app = DjangoDash('Pie_chart')  # or DjangoDash('PieChartApp') if you're integrating with Django

data = CONT_Y.objects.values('country', 'year', 'co2_coal', 'co2_gas', 'co2_oil','co2_trade')
df = pd.DataFrame(list(data))

# Create unique lists of countries and years for dropdowns
countries = df['country'].unique().tolist()
years = df['year'].unique().tolist()

# Define the initial layout for the Dash app
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value=countries[0]  # Set a default value
    ),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in years],
        value=years[-1]  # Set a default value
    ),
    dcc.Graph(id='co2-pie-chart')
])

# Define callback to update the pie chart based on the selected country and year
@app.callback(
    Output('co2-pie-chart', 'figure'),
    [Input('country-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_figure(selected_country, selected_year):
    # Filter the DataFrame for the selected country and year
    filtered_df = df[(df['country'] == selected_country) & (df['year'] == selected_year)]

    if filtered_df.empty:
        # Handle case where there is no data for the selected combination
        fig = px.pie(title='No data for the selected year and country')
    else:
        country_data = filtered_df.iloc[0]
        
        # Prepare the data for the pie chart
        co2_data = {
            'sources': ['Coal', 'Gas', 'Oil','Trade'],
            'co2': [
                country_data['co2_coal'], 
                country_data['co2_gas'], 
                country_data['co2_oil'],
                country_data['co2_trade']
            ]
        }
        fig_data = pd.DataFrame(co2_data)
        
        # Generate the pie chart figure
        fig = px.pie(
            fig_data, 
            values='co2', 
            names='sources', 
            title=f'co2 Breakdown for {selected_country} in {selected_year}'
        )

    return fig
