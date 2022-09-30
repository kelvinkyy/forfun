import pickle

import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing

data = pd.read_csv("car.txt", ",")
print(data.head())

"""data processing"""

dp = preprocessing.LabelEncoder()

buying = dp.fit_transform(np.array(data["buying"]))
maint = dp.fit_transform(np.array(data["maint"]))
doors = dp.fit_transform(np.array(data["doors"]))
persons = dp.fit_transform(np.array(data["persons"]))
lug_boot = dp.fit_transform(np.array(data["lug_boot"]))
safety = dp.fit_transform(np.array(data["safety"]))
cls = dp.fit_transform(np.array(data["class"]))

predict = "class"

x = list(zip(buying,maint,doors,persons,lug_boot,safety))
y = list(cls)

best = 0
x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)
model = KNeighborsClassifier(n_neighbors=7)

names = ["unacc", "acc", "good", "vgood"]
"""
for _ in range(30):
    x_train,x_test,y_train,y_test = sklearn.model_selection.train_test_split(x,y,test_size=0.1)

    model = KNeighborsClassifier(n_neighbors=7)

    model.fit(x_train,y_train)
    acc = model.score(x_test,y_test)
    print(acc)

    if acc > best:
        acc = best
        with open("knnmodel.pickle", "wb") as f:
            pickle.dump(model, f)"""
pickle_in = open("knnmodel.pickle", "rb")
model = pickle.load(pickle_in)

predicted = model.predict(x_test)

for p in range (len(predicted)):
    print("predicted:", names[predicted[p]], "Data:", x_test[p], "actual:", names[y_test[p]])
    n = model.kneighbors([x_test[p]], 7 , True)
    print(n)