from dash import dcc
from dash import html
import dash
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash_table import DataTable
from django_plotly_dash import DjangoDash
from home.models import CONT_E

# Create a Dash application
app = DjangoDash('P_chart')  # or DjangoDash('PieChartApp') if you're integrating with Django

data = CONT_E.objects.values('continents', 'year', 'co2_coal', 'co2_gas', 'co2_oil','co2_trade')
df = pd.DataFrame(list(data))

# Create unique lists of continents and years for dropdowns
continents = df['continents'].unique().tolist()
years = df['year'].unique().tolist()

# Define the initial layout for the Dash app
app.layout = html.Div([
    dcc.Dropdown(
        id='continents-dropdown',
        options=[{'label': continents, 'value': continents} for continents in continents],
        value=continents[0]  # Set a default value
    ),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in years],
        value=years[-1]  # Set a default value
    ),
    dcc.Graph(id='co2-pie-chart')
])

# Define callback to update the pie chart based on the selected continents and year
@app.callback(
    Output('co2-pie-chart', 'figure'),
    [Input('continents-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_figure(selected_continents, selected_year):
    # Filter the DataFrame for the selected continents and year
    filtered_df = df[(df['continents'] == selected_continents) & (df['year'] == selected_year)]

    if filtered_df.empty:
        # Handle case where there is no data for the selected combination
        fig = px.pie(title='No data for the selected year and continents')
    else:
        continents_data = filtered_df.iloc[0]
        
        # Prepare the data for the pie chart
        co2_data = {
            'sources': ['Coal', 'Gas', 'Oil','Trade'],
            'co2': [
                continents_data['co2_coal'], 
                continents_data['co2_gas'], 
                continents_data['co2_oil'],
                continents_data['co2_trade']
            ]
        }
        fig_data = pd.DataFrame(co2_data)
        
        # Generate the pie chart figure
        fig = px.pie(
            fig_data, 
            values='co2', 
            names='sources', 
            title=f'co2 Breakdown for {selected_continents} in {selected_year}'
        )

    return fig