import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(df, 'frequency', 'direction', 'strength', None, None, None, base=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, barnorm=None, barmode='relative', direction='clockwise', pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
