import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, 'total_bill', y=None, color=None, facet_row=None, facet_col=None, hover_name=None, hover_data=None, animation_frame=None, animation_group=None, facet_col_wrap=0)
