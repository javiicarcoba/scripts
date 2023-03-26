import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

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

def sigmoid(z):
    return 1/(1+np.exp(-z))

def compute_gradient(x, y, w, b): 
    m,n = X.shape
    dj_dw = np.zeros((n,))
    dj_db = 0.
    err = 0
    
    for i in range(m):  
        z = np.dot(X[i],w)+b
        f_wb = sigmoid(z)
        err += (f_wb - y[i])
        for j in range(n):
            dj_dw[j] += err * X[i,j]
        dj_db += err
        
    dj_dw = dj_dw / m 
    dj_db = dj_db / m 
        
    return dj_dw, dj_db

def gradient_descent(x, y, w_in, b_in, alpha, num_iters, gradient_function): 
    b = b_in
    w = w_in
    
    for i in range(num_iters):
        dj_dw, dj_db = gradient_function(x, y, w , b)     
    
        b = b - alpha * dj_db                            
        w = w - alpha * dj_dw                            
    
        if i% math.ceil(num_iters/10) == 0:
            print(f"Iteration: {i}, w = {w}, b = {b}")
    
    return w, b

w_tmp  = np.zeros_like(X[0])
b_tmp  = 0.
alph = 0.01
iters = 1000
w_final, b_final= gradient_descent(X, y, w_tmp, b_tmp, alph, iters, compute_gradient) 
print(f"w={w_final},b={b_final}")
