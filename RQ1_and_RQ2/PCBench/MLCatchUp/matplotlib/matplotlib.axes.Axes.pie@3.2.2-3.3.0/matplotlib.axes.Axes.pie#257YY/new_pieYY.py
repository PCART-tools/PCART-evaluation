import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, shadow=True, labeldistance=1.05, startangle=90, radius=False, counterclock=False, wedgeprops={'edgecolor': 'black'}, textprops={'color': 'white'}, center=(0, 0), frame=True, normalize=None)
