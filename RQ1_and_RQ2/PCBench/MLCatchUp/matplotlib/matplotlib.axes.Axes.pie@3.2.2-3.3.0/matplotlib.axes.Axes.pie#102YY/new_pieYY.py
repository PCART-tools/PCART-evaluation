import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, pctdistance=0.85, labeldistance=1.05, shadow=True, startangle=90, colors=colors, autopct='%1.1f%%', data=None, normalize=None)
