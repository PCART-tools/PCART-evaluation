import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, color_discrete_sequence=None, color_discrete_map=None, color_continuous_scale=None, trendline_options=None, trendline_scope='trace')
