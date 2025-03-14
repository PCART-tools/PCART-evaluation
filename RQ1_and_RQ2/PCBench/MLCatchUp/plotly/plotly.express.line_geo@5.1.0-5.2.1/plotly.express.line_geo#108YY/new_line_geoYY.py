import plotly.express as px
df = px.data.gapminder().query('year == 2007')
fig = px.line_geo(df, None, None, 'iso_alpha', None, None, None, 'continent', None, None, None, None, facet_col_wrap=0, facet_row_spacing=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
