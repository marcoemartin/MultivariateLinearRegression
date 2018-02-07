import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

def h(theta1, theta2, x):
    return theta1*x + theta2

def mean(vector):
    return sum(vector) / float(len(vector))

def covariance(x, x_mean, y, y_mean):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i]-x_mean) * (y[i] - y_mean)
    return covar

def variance(values, x_mean):
    return sum([(x - x_mean)**2 for x in values])

def coefficients(x, y):
    x_mean, y_mean = mean(x), mean(y)
    theta1 = covariance(x, x_mean, y, y_mean) / variance(x, x_mean)
    theta2 = mean(Y) - theta1 * mean(X)
    return (theta1, theta2)

if __name__ == "__main__":
    boston = load_boston()
    bos = pd.DataFrame(boston.data)
    bos.columns = boston.feature_names
    print bos.keys()
    Y = boston.target
    X = bos.RM

    m = bos.shape[0]
#    theta1, theta2 = coefficients(X, Y)
#    plt.plot(X,Y,'ro')
#    plt.plot(X,h(theta1, theta2, X))
#    plt.show()

