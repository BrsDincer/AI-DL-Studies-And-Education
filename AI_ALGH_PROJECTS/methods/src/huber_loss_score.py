import numpy as np

class HUBERLOSSSCORE(object):
    """
    The Huber loss function is a combination of Mean Squared Error (MSE)
    and Mean Absolute Error (MAE).
    
    It is a smooth approximation of the Absolute Loss.
    
    L(y_true, y_pred) = 
         { 1/2 * (y_true - y_pred)^2  if |y_true - y_pred| < delta
         { delta * |y_true - y_pred| - delta^2/2  otherwise

    In the equation:
        y_true is the true value of the target variable
        y_pred is the predicted value
        delta is a user-defined parameter
    
    """
    def __init__(self)->classmethod:
        self.__x = np.array([1,2,3])
        self.__y = np.array([2,2,2])
    def __str__(self)->str:
        return "HUBER LOSS CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return HUBERLOSSSCORE.__doc__
    def _CALCULATE(self,delta:float=1.0):
        diff = self.__x - self.__y
        loss = np.where(np.abs(diff)<delta,
                        (1/2)*diff**2,
                        delta*(np.abs(diff)-(delta**2)/2))
        hbl = np.mean(loss)
        return round(hbl,3)

if __name__ == "__main__":
    hbl = HUBERLOSSSCORE()._CALCULATE()
    print(hbl)