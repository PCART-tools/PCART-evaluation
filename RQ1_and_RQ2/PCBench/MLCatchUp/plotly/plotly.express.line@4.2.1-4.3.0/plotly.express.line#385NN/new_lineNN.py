import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, {}, {}, None, color_discrete_map={}, line_dash_sequence=None, line_dash_map={}, log_x=False, log_y=False, range_x=None, facet_col_wrap=0)
