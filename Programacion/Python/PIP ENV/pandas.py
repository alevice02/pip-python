import pandas as pd

df = pd.read_csv()
df = df[df['Continent'] == 'South America']

countries = df['Country'].values
percentages = df['World Population'].values

