import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, None, None, None, None, {}, {}, None, None, None, None, None, None, False, False, None, None, None, histnorm=None, nbinsx=None, nbinsy=None, title=None, template=None, facet_col_wrap=0)
