import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', trendline_options=None, trendline_scope='trace')
