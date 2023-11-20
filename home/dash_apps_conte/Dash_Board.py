import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from home.models import CONT_Y

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Dash_Board', external_stylesheets=external_stylesheets)
# Retrieve CO2 data from the database
data = CONT_Y.objects.all().values('iso_code', 'year', 'co2')
df = pd.DataFrame(list(data))

# Assuming you have multiple years of data, find the range of years
year_range = list(range(df['year'].min(), df['year'].max() + 1, 10))

year_slider = dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        step=10,
        marks={str(year): str(year) for year in year_range},
        value=df['year'].max()  # Set initial value to the max year
    )

# Create the initial Choropleth map for the earliest year
fig = go.Figure()


app.layout = html.Div([
    dcc.Graph(id='world-map', figure=fig, style={'height': '90vh','overflow' :'hidden'}),
    year_slider
], style={'height': '100%', 'width': '100%', 'position': 'relative'})

@app.callback(
    Output('world-map', 'figure'),
    [Input('year-slider', 'value')]
)
def update_map(selected_year):
    filtered_df = df[df['year'] == selected_year]

    # Create the updated Choropleth map
    fig = go.Figure(data=go.Choropleth(
        locations=filtered_df['iso_code'],
        z=filtered_df['co2'],
        text=filtered_df['iso_code'],
        colorscale='Viridis',
        autocolorscale=False,
        reversescale=True,
        marker_line_color='darkgray',
        marker_line_width=0.5,
        colorbar_title='CO2 values',
    ))

    # Update the layout
    fig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        margin={"r":0, "t":0, "l":0, "b":0}, # Remove margins
        
    )

    return fig