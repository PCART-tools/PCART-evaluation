import plotly.express as px
df = px.data.wind()
fig = px.bar_polar(data_frame=df, r='frequency', theta='direction', color='strength', range_theta=None)
