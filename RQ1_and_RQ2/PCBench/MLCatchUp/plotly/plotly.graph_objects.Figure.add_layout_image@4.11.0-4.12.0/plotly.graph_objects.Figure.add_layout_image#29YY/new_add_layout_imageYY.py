import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_layout_image(None, None, None, None, 0.2, 0.2, None, exclude_empty_subplots=None)
