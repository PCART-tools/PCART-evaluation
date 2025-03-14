import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, line_group=None, text=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, line_dash_sequence=None, line_dash_map={}, direction='clockwise', start_angle=90, line_close=False, line_shape=None, render_mode='auto', range_r=None, log_r=False, title=None, template=None, range_theta=None)
