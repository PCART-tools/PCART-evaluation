import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(data_frame=df, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
