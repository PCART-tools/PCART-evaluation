import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, x='year', y='lifeExp', line_group=None, color=None, line_dash=None, facet_col_wrap=0)
