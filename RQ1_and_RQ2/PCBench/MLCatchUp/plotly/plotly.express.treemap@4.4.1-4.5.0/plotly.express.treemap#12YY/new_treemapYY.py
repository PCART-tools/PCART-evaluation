import plotly.express as px
df = px.data.tips()
fig = px.treemap(df, None, 'total_bill', parents=None, path=None)
