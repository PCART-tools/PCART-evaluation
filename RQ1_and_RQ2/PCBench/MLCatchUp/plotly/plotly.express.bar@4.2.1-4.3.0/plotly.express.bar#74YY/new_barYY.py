import plotly.express as px
data_canada = px.data.gapminder().query("country == 'Canada'")
fig = px.bar(data_canada, 'year', 'pop', None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, custom_data=None, text=None, error_x=None, facet_col_wrap=0)
