import plotly.express as px
df = px.data.tips()
fig = px.density_contour(df, 'total_bill', 'tip', z=None, color=None, facet_row=None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, trendline_options=None, trendline_scope='trace')
