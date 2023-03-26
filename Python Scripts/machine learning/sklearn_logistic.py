import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv("./archive/mushrooms.csv")
df = df.dropna()

poisonous = pd.get_dummies(df["class"], drop_first=True)
bruises = pd.get_dummies(df["bruises"], drop_first=True)
surface = pd.get_dummies(df["cap-surface"], drop_first=True)
space = pd.get_dummies(df["gill-spacing"], drop_first=True)
size = pd.get_dummies(df["gill-size"], drop_first=True)

df = pd.concat([bruises,surface,space,size],axis=1)

X = np.array(df)
y = np.array(poisonous)

from sklearn.linear_model import LogisticRegression

X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.33, random_state=42)

logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train)

print(logisticRegr.coef_, logisticRegr.intercept_)