import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(data_frame=df, x='total_bill', y='tip', z=None, facet_row=None, facet_col=None, facet_col_wrap=0)
