import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, facet_col_wrap=0)
