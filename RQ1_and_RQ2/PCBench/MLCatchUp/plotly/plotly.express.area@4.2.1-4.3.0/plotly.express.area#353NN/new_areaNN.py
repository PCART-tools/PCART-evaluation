import plotly.express as px
df = px.data.gapminder()
fig = px.area(df, 'year', 'pop', 'country', 'continent', None, None, None, None, None, None, None, None, {}, {}, None, {}, 'v', None, False, False, None, None, None, None, template=None, facet_col_wrap=0)
