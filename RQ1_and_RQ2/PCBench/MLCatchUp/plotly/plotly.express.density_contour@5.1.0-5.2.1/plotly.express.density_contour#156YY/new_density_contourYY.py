import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', None, None, None, None, 0, None, None, None, None, None, animation_group=None, category_orders=None, labels=None, orientation=None, trendline_options=None, trendline_scope='trace')
