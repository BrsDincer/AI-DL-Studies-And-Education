import numpy as np

class LOGCOSHSCORE(object):
    """
    Log-Cosh loss is a smooth approximation of the Absolute Loss.
    
    The Log-Cosh loss is calculated
    as the mean of the logarithm of the hyperbolic cosine of the residual
    for each sample.
    
    L(y_true, y_pred) =  mean(log(cosh(y_true - y_pred)))
    
    Where:
        y_true is the true value of the target variable
        y_pred is the predicted value
        
    The term cosh(y_true - y_pred) is the hyperbolic cosine of the residual,
    this term is always positive and smooth.
    
    The term log(cosh(y_true - y_pred)) is the natural logarithm of the hyperbolic cosine,
    this term is also smooth and it is a good approximation of the absolute value of the residual,
    especially for small residuals.
    
    """
    def __init__(self)->classmethod:
        self.__x = np.array([1,2,3])
        self.__y = np.array([2,2,2])
    def __str__(self)->str:
        return "LOG COSH CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return LOGCOSHSCORE.__doc__
    def _CALCULATE(self):
        diff = self.__x - self.__y
        loss = np.log(np.cosh(diff))
        logcosh = np.mean(loss)
        return logcosh
    
if __name__ == "__main__":
    logcosh = LOGCOSHSCORE()._CALCULATE()
    print(logcosh)