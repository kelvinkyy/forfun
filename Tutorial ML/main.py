import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
from matplotlib import pyplot as plt
import pickle

data = pd.read_csv("student-mat.csv", sep=';')
data = data[["G1","G2","G3","failures","studytime","absences"]]
print(data.head)

x = np.array(data.drop("G3",1))
y = np.array(data["G3"])

x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)
"""
best = 0
for _ in range(30):
    x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

    linear = linear_model.LinearRegression()

    linear.fit(x_train,y_train)
    acc = linear.score(x_test, y_test)
    print("ACCURACY:",[acc])

    if acc >best:
        acc = best
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)"""

pickle_in = open("studentmodel.pickle", "rb")
linear = pickle.load(pickle_in)

print("coefficient: \n", linear.coef_)
print("intercept: \n", linear.intercept_)

predictions = linear.predict(x_test)

for X in range(len(predictions)):
    print(round(predictions[X],2),x_test[X],y_test[X])

p = "absences"
plt.style.use("ggplot")
plt.scatter(data[p],data["G3"])
plt.xlabel(p)
plt.ylabel("FINAL GRADE")
plt.show()