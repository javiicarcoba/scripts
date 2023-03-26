import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("./archive/trainrl.csv")
df = df.dropna()
x = np.array(df["x"])
y = np.array(df["y"])

df = pd.read_csv("./archive/testrl.csv")
x_test = np.array(df["x"])
y_test = np.array(df["y"])

def cost_func(x, y, w, b):
    m = x.shape[0]
    costo = 0
    for i in range(m):
        f_wb = w*x[i]+b
        costo += (f_wb - y[i])**2
        
    costo_total = 1/(2*m) * costo
    
    return costo_total

def compute_gradient(x, y, w, b): 
    m = x.shape[0]    
    dj_dw = 0
    dj_db = 0
    
    for i in range(m):  
        f_wb = w*x[i]+b 
        dj_dw += (f_wb - y[i])*x[i]
        dj_db += (f_wb - y[i])
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

def modelo (x, w, b):    
    m = len(x)
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w*x[i]+b
    
    return f_wb

w_init = 0
b_init = 30
alpha = 0.0001
iterations = 100000
w_final,b_final= gradient_descent(x,y,w_init,b_init,alpha,iterations,compute_gradient)
print(f"w={w_final},b={b_final}")

y_pred = modelo(x_test, w_final, b_final)
plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,color="red")

while(True):
    prediction = input("Ingrese el numero que quiera predecir: ")
    
    result = w_final*prediction+b_final
    print("La predicción para el número {} es: {}".format(prediction, result))



