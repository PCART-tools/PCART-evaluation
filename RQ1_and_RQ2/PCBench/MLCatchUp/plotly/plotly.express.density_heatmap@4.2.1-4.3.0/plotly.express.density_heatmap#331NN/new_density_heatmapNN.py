import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, None, None, None, None, {}, {}, None, None, None, None, None, None, False, False, range_x=None, range_y=None, histfunc=None, histnorm=None, nbinsx=None, facet_col_wrap=0)
