import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error
data = pd.read_csv(r"C:\Users\Lenovo\Desktop\Datasets\Startups.csv")
print(data.head())
print(data.describe())
print(sns.heatmap(data.corr(),annot=True))
plt.show()
# plt.imsave('fig1.png')
x=data.drop(['State'],axis=1,inplace=True)
x=data.iloc[:,:-1]
y=data.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x.values,y.values,test_size=0.2,random_state=42)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print(y_pred)
print(mean_squared_error(y_pred,y_test))
