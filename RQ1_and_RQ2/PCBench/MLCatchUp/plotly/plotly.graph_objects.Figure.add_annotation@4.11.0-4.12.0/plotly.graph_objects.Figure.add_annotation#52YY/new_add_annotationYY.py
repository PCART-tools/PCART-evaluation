import plotly.graph_objects as go
fig = go.Figure()
trace1 = go.Bar(x=[1, 2, 3], y=[4, 5, 6], name='Bar Trace')
fig.add_trace(trace1)
fig.add_annotation(None, None, None, arrowhead=1, arrowside=None, arrowsize=None, arrowwidth=None, ax=20, axref=None, exclude_empty_subplots=None)
