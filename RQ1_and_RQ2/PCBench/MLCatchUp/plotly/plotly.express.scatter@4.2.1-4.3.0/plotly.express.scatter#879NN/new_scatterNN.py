import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, None, color_continuous_midpoint=None, symbol_sequence=None, symbol_map={}, opacity=None, size_max=None, marginal_x=None, marginal_y=None, trendline=None, trendline_color_override=None, log_x=False, log_y=False, range_x=None, range_y=None, render_mode='auto', title=None, template=None, width=None, facet_col_wrap=0)
