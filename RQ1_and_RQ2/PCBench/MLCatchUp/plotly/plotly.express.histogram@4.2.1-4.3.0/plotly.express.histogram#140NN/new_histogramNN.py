import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, None, {}, {}, None, color_discrete_map={}, marginal=None, opacity=None, facet_col_wrap=0)
