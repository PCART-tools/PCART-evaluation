import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, 'gdpPercap', 'pop', 'year', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, False, False, False, None, None, None, None, template=None, width=None, height=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
