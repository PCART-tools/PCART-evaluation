import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, 'gdpPercap', 'pop', 'year', None, None, None, line_group=None, hover_name=None, hover_data=None, custom_data=None, error_x=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
