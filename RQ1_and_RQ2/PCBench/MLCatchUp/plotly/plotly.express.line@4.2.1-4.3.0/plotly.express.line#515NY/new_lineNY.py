import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, None, error_x_minus=None, error_y=None, error_y_minus=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, line_dash_sequence=None, line_dash_map={}, log_x=False, log_y=False, range_x=None, range_y=None, line_shape=None, render_mode='auto', title=None, facet_col_wrap=0)
