import numpy as np

class QUANTILELOSSSCORE(object):
    """
    The Quantile loss is a loss function that is used to estimate quantiles of a target variable.
    The Quantile loss is calculated as the mean of the loss for each sample.
    
    The Quantile loss is not differentiable,
    which makes it not suitable for training models using gradient descent,
    it is used to estimate percentiles of the target variable.
    
    L(y_true, y_pred, tau) =
        { tau * (y_true - y_pred) if y_true > y_pred
     { (tau - 1) * (y_true - y_pred) if y_true <= y_pred
    
    Where:
        y_true is the true value of the target variable
        y_pred is the predicted value
        tau is the quantile level
        
    The term (y_true - y_pred) represents the residual or error,
    this term is always positive or zero.
    
    The term tau is a scalar value that represents the quantile level that we want to estimate,
    it is between 0 and 1.
    

    """
    def __init__(self)->classmethod:
        self.__x = np.array([1,2,3])
        self.__y = np.array([2,2,2])
    def __str__(self)->str:
        return "QUANTILE LOSS CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return QUANTILELOSSSCORE.__doc__
    def _CALCULATE(self,tau:float=0.5):
        diff = self.__x - self.__y
        loss = np.where(self.__x>self.__y,
                        tau*diff,
                        (tau-1)*diff)
        qlss = np.mean(loss)
        return round(qlss,3)
    
if __name__ == "__main__":
    qlss = QUANTILELOSSSCORE()._CALCULATE()
    print(qlss)