import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, symbol=None, size=None, hover_name=None, range_theta=None)
