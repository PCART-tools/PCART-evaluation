import plotly.graph_objs as go
fig = go.Figure([go.Scatter(x=[1, 2, 3], y=[3, 1, 6])], go.Layout(title='My Plot'), skip_invalid=False)
