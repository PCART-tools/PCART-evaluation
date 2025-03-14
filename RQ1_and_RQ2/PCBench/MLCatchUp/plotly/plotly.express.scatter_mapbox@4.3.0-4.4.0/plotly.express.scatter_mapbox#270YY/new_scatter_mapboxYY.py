import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(data_frame=df, lat='centroid_lat', lon='centroid_lon', color='peak_hour', text=None, hover_name=None, hover_data=None, custom_data=None, size=None, animation_frame=None, animation_group=None, category_orders={}, labels={}, color_discrete_sequence=None, color_discrete_map={}, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, opacity=None, size_max=None, zoom=8, title=None, center=None, mapbox_style=None)
