import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, facet_col_wrap=0)
