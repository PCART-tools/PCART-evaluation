import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', 'sepal_length', None, None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, log_x=False, log_y=False, range_x=None, range_y=None, render_mode='auto', trendline_options=None, trendline_scope='trace')
