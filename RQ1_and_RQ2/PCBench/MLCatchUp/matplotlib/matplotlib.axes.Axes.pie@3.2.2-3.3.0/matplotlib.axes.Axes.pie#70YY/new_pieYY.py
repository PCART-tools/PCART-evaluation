import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(shadow=True, pctdistance=0.85, autopct='%1.1f%%', labels=labels, colors=colors, x=sizes, data=None, explode=explode, normalize=None)
