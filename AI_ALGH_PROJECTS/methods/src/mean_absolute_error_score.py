import numpy as np

class MEANABSOLUTEERRORSCORE(object):
    """
    Mean Absolute Error (MAE) is another commonly used loss function for regression problems,
    similar to Mean Squared Error (MSE).
    It measures the average of the absolute differences between the predicted and actual values.
    The smaller the MAE, the better the model is at predicting the target variable.
    
    The MAE is less sensitive to outliers than the MSE,
    it will be affected less by the large differences
    and it is not sensitive to the scale of the target variable.

    The formula for MAE is:
        MAE = (1/n) * Σ|y_true - y_pred|
        
    where:
        y_pred is the predicted value
        y_true is the true value of the target variable
    
    """
    def __init__(self)->classmethod:
        self.__x = np.array([1,2,3])
        self.__y = np.array([2,2,2])
    def __str__(self)->str:
        return "MEAN ABSOLUTE ERROR CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return MEANABSOLUTEERRORSCORE.__doc__
    def _CALCULATE(self):
        assert len(self.__x.shape) == len(self.__y.shape)
        vlen = len(self.__x)
        diff = self.__x - self.__y
        vabs = np.abs(diff)
        mae = np.sum(vabs/vlen)
        return round(mae,3)
    
if __name__ == "__main__":
    mae = MEANABSOLUTEERRORSCORE()._CALCULATE()
    print(mae)