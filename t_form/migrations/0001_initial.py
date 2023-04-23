# Generated by Django 4.2 on 2023-04-23 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('BSP', 'Burrito San Patricio'), ('BSC', 'Burrito Condado'), ('BGH', 'Burger Garden Hills'), ('BGC', 'Burger Condado'), ('BGP', 'Burger Ponce')], max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('cash_reported', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pennies', models.IntegerField()),
                ('nickels', models.IntegerField()),
                ('dimes', models.IntegerField()),
                ('quarters', models.IntegerField()),
                ('one_dollar', models.IntegerField()),
                ('five_dollar', models.IntegerField()),
                ('ten_dollar', models.IntegerField()),
                ('twenty_dollar', models.IntegerField()),
                ('fifty_dollar', models.IntegerField()),
                ('one_hundred', models.IntegerField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('difference', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
