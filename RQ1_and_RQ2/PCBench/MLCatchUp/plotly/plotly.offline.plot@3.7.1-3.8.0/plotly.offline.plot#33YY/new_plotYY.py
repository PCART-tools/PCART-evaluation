import plotly.graph_objs as go
import plotly.offline as pyo
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6], animation_opts=None)
data = [trace]
pyo.plot(data, False, link_text='Export to plot.ly', validate=True, output_type='file', include_plotlyjs=True, filename='temp-plot.html', animation_opts=None)
