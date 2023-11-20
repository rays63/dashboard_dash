from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash
from home.models import CONT_Y

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Bub_chart', external_stylesheets=external_stylesheets)

# Query the CO2 data from the database
data = CONT_Y.objects.all().values()
df = pd.DataFrame(list(data.values('year', 'co2','country','pop','co2_per_cap')))

year_range = list(range(df['year'].min(), df['year'].max() + 1, 10))

app.layout = html.Div([
    dcc.Graph(id='bubble-chart'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        step=10,
        marks={str(year): str(year) for year in year_range},
        value=df['year'].max()  # Set initial value to the max year
    )
])

@app.callback(
    Output('bubble-chart', 'figure'),
    Input('year-slider', 'value')
)
def update_bubble_chart(selected_year):
    # Query the data points for the selected year
    filtered_df = df[df['year'] == selected_year]
    fig = px.scatter(
        filtered_df,
        x='co2_per_cap',
        y='co2',
        size='pop',  # Use 'co2' values to determine bubble size
        color='country',
        hover_name='country',
        log_x=True,  # Use a logarithmic scale for the x-axis
        title='CO2 Emissions Bubble Chart'
    )
    return fig