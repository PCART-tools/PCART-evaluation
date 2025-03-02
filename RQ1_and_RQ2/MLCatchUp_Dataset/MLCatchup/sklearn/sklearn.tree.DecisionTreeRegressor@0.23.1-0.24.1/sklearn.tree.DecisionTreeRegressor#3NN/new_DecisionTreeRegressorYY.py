import pandas as pd
import numpy as np  #新增

#file_path='./kc_house_data.csv'

#data=pd.read_csv(file_path)

np.random.seed(334)     #新增
# 假设有 500 行数据
data = pd.DataFrame({       #新增
    'bedrooms': np.random.randint(1, 6, 500),
    'bathrooms': np.random.uniform(1, 4, 500),
    'sqft_living': np.random.uniform(500, 3500, 500),
    'sqft_lot': np.random.uniform(1000, 10000, 500),
    'floors': np.random.randint(1, 3, 500),
    'waterfront': np.random.randint(0, 2, 500),
    'sqft_living15': np.random.uniform(500, 3500, 500),
    'price': np.random.uniform(100000, 1000000, 500)
})


# this is called X
attribute_taken_for_predictor=['bedrooms','bathrooms','sqft_living','sqft_lot','floors','waterfront','sqft_living15']
X=data[attribute_taken_for_predictor]
Y=data.price

from sklearn.tree import DecisionTreeRegressor

# Defining the model


# Fit the model

housing_model = DecisionTreeRegressor(criterion='mse', max_depth=None, max_features=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, min_samples_leaf=1, min_samples_split=2, min_weight_fraction_leaf=0.0, random_state=None, splitter='best')

housing_model.fit(X,Y)      #此处有调整