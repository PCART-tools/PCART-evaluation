import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, None, None, None, None, range_color=None, color_continuous_midpoint=None, barnorm=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
