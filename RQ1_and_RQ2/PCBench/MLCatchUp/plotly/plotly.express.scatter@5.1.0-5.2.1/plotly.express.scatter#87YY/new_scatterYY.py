import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, 'sepal_width', y='sepal_length', color=None, symbol=None, size=None, hover_name=None, hover_data=None, custom_data=None, text=None, facet_row=None, facet_col=None, trendline_options=None, trendline_scope='trace')
