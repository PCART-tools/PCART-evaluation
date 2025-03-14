import plotly.express as px
df = px.data.gapminder().query("country=='Brazil'")
fig = px.line_3d(data_frame=df, x='gdpPercap', y='pop', z='year', color=None, line_dash=None, text=None, line_group=None, hover_name=None, hover_data=None, custom_data=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, error_z=None, error_z_minus=None, symbol=None, symbol_sequence=None, symbol_map=None, markers=False)
