import numpy as np

class COVARIANCE_SCORE(object):
    """
    This script defines a function [COVARIANCE_SCORE].
    It takes two array structres as input and returns the covariance between them.
    
    Covariance is a measure of the joint variability of two random variables.
    It tells us how much two variables change together.

    The mathematical formula for the covariance between two variables X and Y is:
    
        cov(X,Y) = 1/(n-1) * Σi=1 to n (X_i - mean(X)) * (Y_i - mean(Y))
    
    Where:
    
        X and Y are the two random variables
        n is the number of observations or data points
        mean(X) and mean(Y) are the means of the two variables
        X_i and Y_i are the i-th observations of the two variables
        
    Covariance can be positive or negative,
    indicating that the two variables tend to increase or decrease together,respectively.
    
    A positive covariance means that both variables increase together,
    while a negative covariance means that one variable increases as the other decreases.
    
    A covariance of zero indicates that the two variables are not related.
    
    It's worth noting that covariance is not a standardized measure and it's hard to interpret the magnitude of a covariance as it depends on the units of the variables. That's why correlation coefficient such as Pearson Correlation coefficient that use the standard deviation and normalize the covariance is more widely used.
    
    """
    def __init__(self):
        self.__x = np.arange(1,6,2)
        self.__y = np.arange(6,11,2)
    def __str__(self):
        return "COVARIANCE SCORE - [Pseudocode]"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[PICKLED-DENIED]")
    def __repr__(self):
        return COVARIANCE_SCORE.__doc__
    def _CALCULATE(self):
        assert len(self.__x.shape) == 1
        assert len(self.__x.shape) == 1
        n_count = len(self.__x)
        xmean = np.mean(self.__x)
        ymean = np.mean(self.__y)
        xdevi = [i - xmean for i in self.__x]
        ydevi = [i - ymean for i in self.__y]
        tdevi = np.sum([i*j for i,j in zip(xdevi,ydevi)])
        cov = 1/(n_count-1) * tdevi
        return cov
    
if __name__ == "__main__":
    rslt = COVARIANCE_SCORE()._CALCULATE()
    print(rslt)