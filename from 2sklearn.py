from sklearn.linear_model import LinearRegression
import numpy as np

x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([22,33,51,61,83])
model=LinearRegression
model.fit(x,y)

print(model.coef_[0])
print(model.intercept_)
