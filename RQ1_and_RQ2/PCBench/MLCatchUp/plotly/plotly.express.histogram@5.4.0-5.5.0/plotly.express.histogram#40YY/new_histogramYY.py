import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, color=None, pattern_shape=None, facet_row=None, facet_col=None, facet_col_wrap=0, text_auto=False)
