import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, {}, None, {}, False, False, None, range_y=None, line_shape=None, facet_col_wrap=0)
