from IPython.display import display, HTML
import plotly.offline as py
import plotly.graph_objs as go
py.init_notebook_mode(connected=True)
trace = go.Scatter(x=[1, 2, 3], y=[4, 5, 6])
data = [trace]
py.iplot(data, False, 'Export to plot.ly', True, image=None, filename='plot_image', image_width=800, auto_play=True)
