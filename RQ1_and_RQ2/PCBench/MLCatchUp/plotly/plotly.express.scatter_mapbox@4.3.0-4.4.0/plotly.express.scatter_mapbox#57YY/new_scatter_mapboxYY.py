import plotly.express as px
df = px.data.carshare()
fig = px.scatter_mapbox(df, 'centroid_lat', 'centroid_lon', color='peak_hour', text=None, hover_name=None, hover_data=None, custom_data=None, size=None, animation_frame=None, center=None, mapbox_style=None)
