import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(df, 'gdpPercap', 'pop', 'year', None, None, None, None, None, None, None, None, None, None, None, None, error_z_minus=None, animation_frame=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
