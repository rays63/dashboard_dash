# Generated by Django 4.2.7 on 2023-11-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_cont_y'),
    ]

    operations = [
        migrations.CreateModel(
            name='CONT_Y',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('pop', models.BigIntegerField()),
                ('iso_code', models.CharField(max_length=50)),
                ('co2', models.FloatField()),
                ('co2_per_cap', models.FloatField()),
                ('co2_coal', models.FloatField()),
                ('co2_cons', models.FloatField()),
                ('co2_gas', models.FloatField()),
                ('co2_oil', models.FloatField()),
                ('co2_trade', models.FloatField()),
            ],
            options={
                'ordering': ('year',),
            },
        ),
    ]
