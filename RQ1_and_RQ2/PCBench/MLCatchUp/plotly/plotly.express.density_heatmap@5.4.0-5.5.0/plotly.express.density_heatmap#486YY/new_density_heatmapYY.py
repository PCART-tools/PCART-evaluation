import plotly.express as px
df = px.data.tips()
fig = px.density_heatmap(df, 'total_bill', 'tip', None, None, None, 0, None, facet_col_spacing=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, category_orders=None, labels=None, orientation=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, marginal_x=None, marginal_y=None, opacity=None, log_x=False, log_y=False, range_x=None, range_y=None, histfunc=None, histnorm=None, nbinsx=None, nbinsy=None, text_auto=False)
