from django.db import models

class Report(models.Model):

    locs = [('SNJ', 'San Juan'), 
            ('BAY', 'Bayamon'),
            ('GUA', 'Guaynabo'),
            ('CAR', 'Carolina'),
            ('CAG', 'Caguas')]

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
