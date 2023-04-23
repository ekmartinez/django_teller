from django.db import models

class Report(models.Model):

    locs = [('BSP', 'Burrito San Patricio'), 
            ('BSC', 'Burrito Condado'),
            ('BGH', 'Burger Garden Hills'),
            ('BGC', 'Burger Condado'),
            ('BGP', 'Burger Ponce')]

    location = models.CharField(max_length=3, choices=locs)
    name = models.CharField(max_length=100)
    date = models.DateField()
    cash_reported = models.CharField(max_length=100)
    pennies = models.IntegerField()
    nickels = models.IntegerField()
    dimes = models.IntegerField()
    quarters = models.IntegerField()
    one_dollar = models.IntegerField()
    five_dollar = models.IntegerField()
    ten_dollar = models.IntegerField()
    twenty_dollar = models.IntegerField()
    fifty_dollar = models.IntegerField()
    one_hundred = models.IntegerField()