import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, {}, None, 'clockwise', 90, None, None, False, 'auto', title=None, template=None, width=None, height=None, range_theta=None)
