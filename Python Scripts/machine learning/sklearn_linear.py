import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

precios_metros = datasets.load_boston()

x = precios_metros.data[:, np.newaxis, 5]
y = precios_metros.target

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

lr = linear_model.LinearRegression()
lr.fit(x_train, y_train)

pred = lr.predict(x_test)

plt.scatter(x, y, marker='x')
plt.plot(x_train, y_train, c='red')
plt.show()

w = lr.coef_
b = lr.intercept_

print("El valor de w es {} y el valor de b es {} en la ecuación de regresión\n\
lineal simple: wx+b".format(w, b))
