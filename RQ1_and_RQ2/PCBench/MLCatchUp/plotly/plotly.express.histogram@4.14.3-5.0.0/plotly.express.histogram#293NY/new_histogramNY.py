import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, facet_col=None, facet_col_wrap=0, facet_row_spacing=None, facet_col_spacing=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, color_discrete_map=None, marginal=None, opacity=None, orientation=None, barmode='relative', barnorm=None, histnorm=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
