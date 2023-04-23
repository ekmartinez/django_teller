import pandas as pd
import numpy as np

df = pd.read_csv('reports.csv')
df['pennies_total'] = df['pennies'] * .01
df['nickles_total'] = df['nickels'] * .05
df['dimes_total'] = df['dimes'] * .1
df['quarters_total'] = df['quarters'] * .25
df['one_dollar_total'] = df['one_dollar'] * 1
df['five_dollar_total'] = df['five_dollar'] * 5
df['ten_dollar_total'] = df['ten_dollar'] * 10
df['twenty_dollar_total'] = df['twenty_dollar'] * 20
df['fifty_dollar_total'] = df['fifty_dollar'] * 50
df['One_hundred_total'] = df['one_hundred'] * 100


df_B = df[['location', 'name', 'date', 'cash_reported', 
			'one_dollar_total',  'five_dollar_total',  'ten_dollar_total',  
			'twenty_dollar_total',  'fifty_dollar_total',  'One_hundred_total']]


print(df_B.T)


 