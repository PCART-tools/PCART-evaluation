import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, marginal_y=None, trendline=None, trendline_color_override=None, log_x=False, log_y=False, range_x=None, range_y=None, trendline_options=None, trendline_scope='trace')
