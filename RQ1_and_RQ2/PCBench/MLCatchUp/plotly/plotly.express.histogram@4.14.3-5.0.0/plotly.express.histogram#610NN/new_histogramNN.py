import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, opacity=None, orientation=None, barmode='relative', barnorm=None, histnorm=None, log_x=False, log_y=False, range_x=None, range_y=None, histfunc=None, cumulative=None, nbins=None, title=None, template=None, width=None, height=None, pattern_shape=None, pattern_shape_sequence=None, pattern_shape_map=None)
