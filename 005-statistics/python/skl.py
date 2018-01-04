from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_predict

linear_regression = linear_model.LinearRegression()
boston = datasets.load_boston() # Example in docs
prediction = cross_val_predict(linear_regression, boston.data, boston.target)
