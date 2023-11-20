from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
from dash_table import DataTable
from django_plotly_dash import DjangoDash
from home.models import CONT_E

app = DjangoDash("D_table")

# Query the CO2 data from the database
data = CONT_E.objects.all().values()
df = pd.DataFrame(list(data))
# df = pd.DataFrame.from_records(data)

app.layout = html.Div([
    DataTable(
        id='co2-data-table',
        columns=[{'name': col, 'id': col} for col in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'},
    ),
])
