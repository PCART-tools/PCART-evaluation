import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, 'frequency', 'direction', None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, None, None, {}, opacity=None, direction='clockwise', start_angle=90, size_max=None, range_r=None, log_r=False, render_mode='auto', title=None, template=None, width=None, height=None, range_theta=None)
