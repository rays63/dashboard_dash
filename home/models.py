from django.db import models

# Create your models here.
# Database for continents
class CONT_E(models.Model):
    continents = models.CharField(max_length = 255)
    year = models.PositiveIntegerField()
    co2 = models.FloatField()
    co2_per_cap = models.FloatField()
    co2_coal = models.FloatField()
    co2_cons = models.FloatField()
    co2_gas = models.FloatField()
    co2_oil = models.FloatField()
    co2_trade = models.FloatField()

    class Meta:
        ordering = ('year',)

# Database for countries
class CONT_Y(models.Model):
    country = models.CharField(max_length= 100)
    year = models.PositiveIntegerField()
    pop = models.FloatField()
    iso_code = models.CharField(max_length=50)
    co2 = models.FloatField()
    co2_per_cap = models.FloatField()
    co2_coal = models.FloatField()
    co2_cons = models.FloatField()
    co2_gas = models.FloatField()
    co2_oil = models.FloatField()
    co2_trade = models.FloatField()

    class Meta:
        ordering = ('year',)