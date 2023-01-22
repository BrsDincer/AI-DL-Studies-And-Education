import numpy as np

class MEANSQUAREDERRORSCORE(object):
    """
    Mean Squared Error (MSE) is a commonly used loss function for regression problems.
    It measures the average of the squared differences between the predicted and actual values.
    The smaller the MSE, the better the model is at predicting the target variable.

    The formula for MSE is:
            MSE = (1/n) * Σ(y_true - y_pred)^2
    where:
        y_pred is the predicted value
        y_true is the true value of the target variable
    """
    def __init__(self)->classmethod:
        self.__x = np.array([1,2,3])
        self.__y = np.array([2,2,2])
    def __str__(self)->str:
        return "MEAN SQUARED ERROR CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return MEANSQUAREDERRORSCORE.__doc__
    def _CALCULATE(self):
        assert len(self.__x.shape) == len(self.__y.shape)
        vlen = len(self.__x)
        diff = self.__x - self.__y
        sqr = diff**2
        mse = np.sum(sqr/vlen)
        return round(mse,3)
    
if __name__ =="__main__":
    mse = MEANSQUAREDERRORSCORE()._CALCULATE()
    print(mse)