import numpy as np
from scipy.special import gammaln

class POISSONLOSSSCORE(object):
    """
    The Poisson loss function is defined as:
        L(y_true, y_pred) = mean(y_true * log(y_pred) - y_pred - log(y_true!))
    
    where:
        y_true is the true value of the target variable
        y_pred is the predicted value
        log(y_true!) is the natural logarithm of the factorial of the true value
        
    The Poisson loss is a loss function that is used
    when the target variable follows a Poisson distribution.
    
    The Poisson loss is not differentiable,
    it is used to estimate the probability of the target variable following a Poisson distribution.

    It is used when the target variable is a count and it follows a Poisson distribution,
    it is not sensitive to the scale of the target variable.
    
    """
    def __init__(self)->classmethod:
        self.__x = np.array([1,2,3])
        self.__y = np.array([2,2,2])
    def __str__(self)->str:
        return "POISSON LOSS CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return POISSONLOSSSCORE.__doc__
    def _CALCULATE(self):
        self.__x = self.__x.astype(int)
        fact = gammaln(self.__x+1)
        xylog = self.__x*np.log(self.__y)
        loss = xylog-self.__y-fact
        plss = np.mean(loss)
        return round(plss,3)

if __name__ == "__main__":
    plss = POISSONLOSSSCORE()._CALCULATE()
    print(plss)