import plotly.express as px
data = dict(character=['Eve', 'Cain', 'Seth', 'Enos', 'Noam', 'Abel', 'Awan', 'Enoch', 'Azura'], parent=['', 'Eve', 'Eve', 'Seth', 'Seth', 'Eve', 'Eve', 'Awan', 'Eve'], value=[10, 14, 12, 10, 2, 6, 6, 4, 4])
fig = px.sunburst(data, 'character', 'value', 'parent', None, None, None, None, None, color_discrete_sequence=None, color_discrete_map={}, hover_name=None, hover_data=None, path=None)
