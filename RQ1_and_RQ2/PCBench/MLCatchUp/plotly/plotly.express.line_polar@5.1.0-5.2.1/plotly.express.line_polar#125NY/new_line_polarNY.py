import plotly.express as px
df = px.data.wind()
fig = px.line_polar(df, 'frequency', 'direction', 'strength', None, None, None, None, None, None, None, animation_group=None, category_orders=None, labels=None, color_discrete_sequence=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
