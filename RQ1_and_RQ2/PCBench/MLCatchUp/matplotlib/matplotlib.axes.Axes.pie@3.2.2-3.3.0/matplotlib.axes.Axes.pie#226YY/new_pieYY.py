import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, '%1.1f%%', 0.85, counterclock=False, startangle=90, wedgeprops={'edgecolor': 'black'}, radius=False, labeldistance=1.05, center=(0, 0), data=None, textprops={'color': 'white'}, shadow=True, normalize=None)
