# Import the necessary modules and libraries
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

np.random.seed(0)   #新增
X = np.random.rand(100, 1)  # 新增
y = X[:, 0]**2 + np.random.normal(0, 0.1, size=100)  # 新增

def presort_():
    mse_list = []
    lr_t = DecisionTreeRegressor()
    lr_t.fit(X,y)
    y_t = lr_t.predict(X)
    mse_list.append(mean_squared_error(y,y_t))



    lr_f = DecisionTreeRegressor()
    lr_f.fit(X,y)
    y_f = lr_f.predict(X)
    mse_list.append(mean_squared_error(y,y_f))
    plt.plot([0,1],mse_list, c="g", label="presort", linewidth=2)
    plt.show()

presort_()  #新增