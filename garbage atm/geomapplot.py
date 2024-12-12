import plotly.express as px
import pandas as pd


# Import data from USGS
data = pd.read_csv('a.csv')


# Drop rows with missing or invalid values in the 'mag' column
data = data.dropna(subset=['Lat'])
data = data.dropna(subset=['Lon'])
data = data.dropna(subset=['Median'])
data = data.dropna(subset=['City'])
data = data[data.Median >= 80000]


# Create scatter map
fig = px.scatter_geo(data, lat='Lat', lon='Lon',
                     hover_name='City', size="Median",
                     title='Median Income in US')
#fig = px.scatter(data, x="Height",y="Weight", color = "Alignment", hover_name = "name", title='Random superhero dataset that angi gave us')
fig.show()