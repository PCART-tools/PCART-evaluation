import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', None, None, None, None, None, None, None, {}, None, None, None, labels={}, title=None, template=None, width=None, path=None)
