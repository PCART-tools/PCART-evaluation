import plotly.express as px
df = px.data.wind()
fig = px.scatter_polar(df, r='frequency', theta='direction', color=None, symbol=None, size=None, hover_name=None, hover_data=None, custom_data=None, text=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, range_theta=None)
