import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 

kiss  = [5, 7, 10, 14, 15, 22]
love = [15, 17, 28, 27, 36, 45]
ha = [1,2,3,4,5,6]
plt.scatter(kiss, ha, color='blue', s=100)
plt.xlabel('kiss count')
plt.ylabel('love(percent%)')
plt.title('how much kiss to make me fall in love')
plt.grid(True)
plt.show()
#


#
from sklearn.linear_model import LinearRegression
X = np.array(kiss).reshape(-1, 1)
y = np.array(love)
model = LinearRegression()
model.fit(X, y) 
print('Model trained successfully!')
#

#
test_kiss  = [[17]]
prediction = model.predict(test_kiss)
print(f"{prediction[0]:.0f}% !")
test_kiss2 = [[30]]
print(f'{model.predict(test_kiss2)[0]:.0f}% !')