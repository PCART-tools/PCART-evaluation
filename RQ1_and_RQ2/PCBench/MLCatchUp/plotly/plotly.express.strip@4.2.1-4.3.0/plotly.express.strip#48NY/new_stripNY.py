import plotly.express as px
df = px.data.tips()
fig = px.strip(df, 'total_bill', 'day', None, None, None, None, hover_data=None, custom_data=None, facet_col_wrap=0)
