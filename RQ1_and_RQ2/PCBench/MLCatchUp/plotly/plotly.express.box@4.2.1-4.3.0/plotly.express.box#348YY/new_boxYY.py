import plotly.express as px
df = px.data.tips()
fig = px.box(df, 'time', 'total_bill', color=None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, custom_data=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, orientation='v', boxmode='group', log_x=False, log_y=False, range_x=None, range_y=None, points=None, notched=False, title=None, template=None, facet_col_wrap=0)
