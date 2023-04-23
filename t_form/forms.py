from django.forms import ModelForm
from django import forms
from .models import Report


class ReportForm(ModelForm):

	locs = [('BSP', 'Burrito San Patricio'), 
			('BSC', 'Burrito Condado'),
			('BGH', 'Burger Garden Hills'),
			('BGC', 'Burger Condado'),
			('BGP', 'Burger Ponce')]
	
	location = forms.CharField(label='Location', widget=forms.Select(choices=locs))
	name = forms.CharField(label="Name", max_length=100)
	date = forms.DateField(label="Date")
	cash_reported = forms.CharField(label="Cash Reported", max_length=100)
	pennies = forms.IntegerField(label="Pennies",  widget=forms.TextInput(attrs={'class': 'input-field'}))
	nickels = forms.IntegerField(label="Nickels", widget=forms.TextInput(attrs={'class': 'input-field'}))
	dimes = forms.IntegerField(label="Dimes", widget=forms.TextInput(attrs={'class': 'input-field'}))
	quarters = forms.IntegerField(label="Quarters", widget=forms.TextInput(attrs={'class': 'input-field'}))
	one_dollar = forms.IntegerField(label="One Dollar", widget=forms.TextInput(attrs={'class': 'input-field'}))
	five_dollar = forms.IntegerField(label="Five Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
	ten_dollar = forms.IntegerField(label="Ten Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
	twenty_dollar = forms.IntegerField(label="Twenty Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
	fifty_dollar = forms.IntegerField(label="Fifty Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
	one_hundred = forms.IntegerField(label="One Hundred Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))

	class Meta:
		model = Report
		fields = ['location', 'name', 'date', 'cash_reported',
    	'pennies', 'nickels', 'dimes', 'quarters', 'one_dollar',
    	'five_dollar', 'ten_dollar', 'twenty_dollar', 'fifty_dollar',
    	'one_hundred']































# class NameForm(forms.Form):

#     locs = [
#         ('ny', 'New York'),
#         ('tx', 'Texas'),
#     ]

#     locations = forms.CharField(label='Location', widget=forms.Select(choices=locs))
#     name = forms.CharField(label="Name", max_length=100)
#     date = forms.DateField(label="Enter Date")
#     cash = forms.CharField(label="Cash Reported", max_length=100)

#     one_cent = forms.IntegerField(label="Pennies",  widget=forms.TextInput(attrs={'class': 'input-field'}))
#     nickle = forms.IntegerField(label="Nickels", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     dime = forms.IntegerField(label="Dimes", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     quarter = forms.IntegerField(label="Quarters", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     one_dollar = forms.IntegerField(label="One Dollar", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     five_dollar = forms.IntegerField(label="Five Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     ten_dollar = forms.IntegerField(label="Ten Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     twenty_dollar = forms.IntegerField(label="Twenty Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     fifty_dollar = forms.IntegerField(label="Fifty Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))
#     one_hundred = forms.IntegerField(label="One Hundred Dollars", widget=forms.TextInput(attrs={'class': 'input-field'}))


