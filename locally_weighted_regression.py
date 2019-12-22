
from math import ceil, pi
import numpy as np
import matplotlib.pyplot as plt


def lowess(x, y, f=2./3., iter=3):

    r = ceil(f*n)
    h = [np.sort(np.abs(x-xi))[r] for xi in x]

    w = np.clip(np.abs((x[:, None]-x[None, :])/h), 0.0, 1.0)
    w = (1 - w**3)**3
    
    yest = np.zeros(n)
    delta = np.ones(n)
    
    for j in range(iter):
        for i in range(n):
            weights = delta * w[:, i]
            b = np.array([np.sum(weights*y), np.sum(weights*y*x)])
            A = np.array([[np.sum(weights), np.sum(weights*x)], 
                          [np.sum(weights*x), np.sum(weights*x*x)]])
            beta = np.linalg.solve(A, b)
            yest[i] = beta[0] + beta[1]*x[i]
        
        plt.figure(figsize=(7,5))
        plt.plot(x, y, label='y noisy')
        plt.plot(x, yest, label='y pred')
        plt.title("Iteration " + str(j+1))
        plt.legend()
            
        residuals = y - yest
        mid = np.median(np.abs(residuals))
        delta = np.clip(residuals/(6.0*mid), -1, 1)
        delta = (1-delta**2)**2
        
    return yest

if __name__=='__main__':
    n = 100
    x = np.linspace(0, 2*pi, n)
    #print("=================value of x ===================")
    #print(x)
    y = np.sin(x) + 0.3*np.random.randn(n)
    y[25] = 4
    y[40] = 3
    y[75] = 4
    #print("================vlaue of y ====================")
    #print(y)
    yest = lowess(x, y, f = 0.25, iter=3)
    
    
    
    
