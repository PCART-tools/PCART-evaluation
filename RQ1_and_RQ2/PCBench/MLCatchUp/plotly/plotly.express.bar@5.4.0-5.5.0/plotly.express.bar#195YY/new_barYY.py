import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, None, None, None, 0, None, None, None, None, None, text=None, base=None, error_x=None, error_x_minus=None, error_y=None, error_y_minus=None, text_auto=False)
