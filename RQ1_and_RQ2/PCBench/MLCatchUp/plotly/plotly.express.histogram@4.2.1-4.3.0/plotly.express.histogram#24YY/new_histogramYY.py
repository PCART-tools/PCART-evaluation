import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, facet_row=None, facet_col=None, facet_col_wrap=0)
