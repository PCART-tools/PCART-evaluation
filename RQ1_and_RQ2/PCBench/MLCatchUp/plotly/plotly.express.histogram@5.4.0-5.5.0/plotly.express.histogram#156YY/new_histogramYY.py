import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, None, 0, None, None, None, None, None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, text_auto=False)
