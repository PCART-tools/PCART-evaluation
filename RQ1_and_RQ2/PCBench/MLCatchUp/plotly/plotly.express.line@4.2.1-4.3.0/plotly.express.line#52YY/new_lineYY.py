import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(df, 'year', 'lifeExp', line_group=None, color=None, line_dash=None, hover_name=None, hover_data=None, custom_data=None, facet_col_wrap=0)
