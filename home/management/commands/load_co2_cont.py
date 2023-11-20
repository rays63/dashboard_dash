import csv
from datetime import date
from itertools import islice
from django.conf import settings
from django.core.management.base import BaseCommand
from home.models import CONT_E


class Command(BaseCommand):
    help = 'Load data from CO2 file'

    def handle(self, *args, **kwargs):
        datafile = settings.BASE_DIR / 'data' / 'co2_emission_by_continents.csv'
        
        with open(datafile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                CONT_E.objects.get_or_create(
                    continents = row['country'],
                    year = row['year'],
                    co2 = row['co2'],
                    co2_per_cap = row['co2_per_capita'],
                    co2_coal = row['coal_co2'],
                    co2_cons = row['consumption_co2'],
                    co2_gas = row['gas_co2'],
                    co2_oil = row['oil_co2'],
                    co2_trade = row['trade_co2']
                )