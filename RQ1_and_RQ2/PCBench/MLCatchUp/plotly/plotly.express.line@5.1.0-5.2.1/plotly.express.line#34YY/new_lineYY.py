import plotly.express as px
df = px.data.gapminder().query("country=='Canada'")
fig = px.line(data_frame=df, x='year', y='lifeExp', line_group=None, color=None, line_dash=None, hover_name=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
