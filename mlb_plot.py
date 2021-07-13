# do all runs, here - keep plotting and basic EDA seperate 
import numpy as np

from numpy.lib.function_base import average
from pandas.core.frame import DataFrame
from statsmodels.genmod.families.family import Binomial
from mlb import *



    # my guesses from eyeballin' it:  
    # x1 is uniform
    # x2 is gaussian
    # x3 is t distribution
    # x5 is exponetial 
    # x6 is double-exponetial (laplace)
  
# my candidates
from scipy.stats import uniform, norm, t, expon, pareto, laplace, beta, probplot

import matplotlib.pyplot as plt

def q1a(df_X):

    #x1
    u, sig = uniform.fit(df_X.x1)
    u = round(u,3)
    sig = round(sig,3)
    probplot(df_X.x1,dist=uniform(u,sig),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x1 with uniform distribution - fit using MLE')
    txt = 'u: ' + str(u) + ' std: ' + str(sig)
    plt.title(txt)
    plt.show()



    #x2
    u, sig = norm.fit(df_X.x2)
    u = round(u,3)
    sig = round(sig,3)
    probplot(df_X.x2,dist=norm(u,sig),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x2 with normal distribution - fit using MLE')
    txt = 'u: ' + str(u) + ' std: ' + str(sig)
    plt.title(txt)
    plt.show()

    #x3 - t
    deg_free, loc, scale = t.fit(df_X.x3)
    deg_free = round(deg_free,3)
    loc = round(loc,3)
    scale = round(scale, 3)
    
    probplot(df_X.x3,dist=t(deg_free,loc,scale),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x3 with t distribution - fit using MLE')
    txt = 'deg free: ' + str(deg_free) + ' location: ' + str(loc) + ' scale: ' + str(scale)
    plt.title(txt)
    plt.show()

    #x3 - beta (looks like one with equal terms...)
    a1, b1, loc1, scale1 = beta.fit(df_X.x3)
    a1 = round(a1,3)
    b1 = round(b1,3)
    loc1 = round(loc1,3)
    scale1 = round(scale1,3)
    
    probplot(df_X.x3,dist=beta(a1,b1,loc=loc1,scale=scale1),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x3 with beta distribution - fit using MLE')
    txt = 'alpha ' + str(a1) + ' location: ' + ' beta: ' + str(b1) + ' location: ' + str(loc1) + ' scale: ' + str(scale1)
    plt.title(txt)
    plt.show()


    #x4
    params = expon.fit(df_X.x5,floc=0)
    probplot(df_X.x5,dist=expon(params[0],params[1]),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x5 with exponential distribution - fit using MLE')
    txt = 'loc: ' + str(params[0]) + ' scale: ' + str(round(params[1],3))
    plt.title(txt)
    plt.show()


    #x5
    params = laplace.fit(df_X.x6,floc=0)
    probplot(df_X.x6,dist=laplace(loc=params[0],scale=params[1]),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x5 with laplace(double exp) distribution - fit using MLE')
    txt = 'loc: ' + str(params[0]) + ' scale' + str(round(params[1],3))
    plt.title(txt)
    plt.show()

    #x2
    u, sig = norm.fit(df_X.x6)
    u = round(u,3)
    sig = round(sig,3)
    probplot(df_X.x6,dist=norm(u,sig),plot=plt.figure().add_subplot(111))
    plt.suptitle('SciPy probplot of x6 with normal distribution - fit using MLE')
    txt = 'u: ' + str(u) + ' std: ' + str(sig)
    plt.title(txt)
    plt.show()





q1a(df_X)


