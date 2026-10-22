# %%
from sklearn.linear_model import LinearRegression
import numpy as np
x=np.array([1,2,3,4]).reshape(-1,1)
y=np.array([20,35,50,65])
model=LinearRegression()
model.fit(x,y)
print(model.coef_[0])
print(model.intercept_)

#
#
#
#

# %%
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3,4,5]).reshape(-1,1)
y=np.array([50,60,65,70,85])
model=LinearRegression()
model.fit(x,y)
print(model.coef_)
print(model.intercept_)
pred=model.predict(x)
print(pred)
print(y)
plt.scatter(x,y,s=100,label='real data')
plt.plot(x,pred,label='pred data')
plt.legend()
plt.grid(True)
plt.show()
########test pred example:
test=np.array([6])
print(model.predict([test]))

#
#
#
#
# %%
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x=np.array([18,19,20,21,22]).reshape(-1,1)
y=np.array([70,74,78,83,90])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(x_train,y_train)
pred=model.predict(x)
predi=np.array([23,24])

print(pred)
plt.scatter(x,y,s=100,label='sen hanie')
plt.plot(x,pred,label='khoshgeli hanie')
plt.grid(True)
plt.legend()
plt.show()
######## R2:
print(model.score(x_train,y_train))
print(model.score(x_test,y_test))

#
#
#
#

# %%
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import numpy as np
y_true=np.array([10,20,30,40,50])
y_pred=np.array([12,18,29,45,47])

print('mae:',mean_absolute_error(y_true,y_pred))
print('mse:',mean_squared_error(y_true,y_pred))

#
#
#
#

# %%
import numpy as np
x=np.array([1,2,3,4,5])
y=np.array([50,60,65,70,85])
w=0
b=0
def mse(y_true,y_pred):
    return np.mean((y_true-y_pred)**2)
def predict(x,w,b):
    return w*x+b
def gradients(x,y,y_pred):
    n=len(y)
    error=y-y_pred
    dw=(-2/n)*np.sum(x*error)
    db=(-2/n)*np.sum(error)
    return dw,db
learning_rate=0.01
for i in range (1000):
    y_pred=predict(x,w,b)
    loss=mse(y,y_pred)
    dw,db=gradients(x,y,y_pred)
    w=w-learning_rate*dw
    b=b-learning_rate*db
    if i %1==0:
        print('step:',i,'loss:',loss)

#
#
#
#

# %%
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x=np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
y=np.array([10,15,22,28,35,40,42,56,62,70])
x1,x2,y1,y2=train_test_split(x,y,test_size=0.4,random_state=None)
model=LinearRegression()
model.fit(x1,y1)
print(model.score(x1,y1))
print(model.score(x2,y2))

#
#
#
#


# %%
from sklearn.linear_model import LinearRegression
study_hour=[1,3,4,6,7,8]
sleep_hour=[8,9,6,7,4,6]
age=[18,18,18,18,18,18]
score=[40,55,60,78,80,90]
x=list(zip(study_hour,sleep_hour,age))
model=LinearRegression()
model.fit(x,score)
print(model.coef_,model.intercept_)
print(model.predict([[9,10,18],[8,4,18],[0,9,18]]))

#
#
#
#

# %%
from sklearn.linear_model import LogisticRegression
study_hour=[1,2,3,4,5,6,7,8]
#inja har ozv az study_hour ro ye list mikone va dar x zakhire mikone
x = [[x] for x in study_hour]
passed=[0,0,0,0,1,1,1,1]
model=LogisticRegression()
model.fit(x,passed)
a1=model.predict_proba([[3]])
a2=model.predict_proba([[7]])
print(a1)
print(round(a1[0][1],2))

#
#
#
#

# %%
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
study_hours= np.array([1,2,3,4,5,6,7,8]).reshape(-1,1)
passed=np.array([0,0,0,0,1,1,1,1])
model=LogisticRegression()
model.fit(study_hours,passed)
x_test=np.linspace(1,8,100).reshape(-1,1)
proba=model.predict_proba(x_test)[:,1]
plt.figure(figsize=(8,5))
plt.plot(x_test,proba,label='probability class = 1')
plt.axhline(0.5,color='red',linestyle='-.')
plt.scatter(study_hours,passed,color='black',label='data points')
plt.xlabel('probability of passing')
plt.ylabel('logistic regression decision curve')
plt.legend()
plt.grid(True)
plt.show()

#
#
#
#

# %%
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score
x=[1,2,3,4,5,6,7,8]
x1=[[x] for x in x]
y=[0,0,0,0,1,1,1,1]
model=LogisticRegression()
model.fit(x1,y)
y_pred=model.predict(x1)
cm=confusion_matrix(y,y_pred)
print(cm)
acc=accuracy_score(y,y_pred)
print(acc)
# %%
