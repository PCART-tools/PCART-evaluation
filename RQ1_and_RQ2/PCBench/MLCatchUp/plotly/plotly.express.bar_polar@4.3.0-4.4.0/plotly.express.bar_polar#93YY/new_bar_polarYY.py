import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, {}, {}, None, color_discrete_map={}, range_theta=None)
