import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, None, None, 'iso_alpha', None, geojson=None, featureidkey=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
