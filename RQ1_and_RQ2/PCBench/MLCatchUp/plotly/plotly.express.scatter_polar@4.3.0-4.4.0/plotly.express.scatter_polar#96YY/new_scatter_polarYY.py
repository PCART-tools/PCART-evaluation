import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, text=None, animation_frame=None, animation_group=None, category_orders={}, range_theta=None)
