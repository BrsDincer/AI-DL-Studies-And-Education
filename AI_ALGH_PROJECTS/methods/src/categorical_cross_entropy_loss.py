import numpy as np

class CATEGORICALCROSSENTROPYLOSS(object):
    """
    Categorical cross-entropy loss is a commonly used loss function
    for multi-class classification problems in data science.
    
    It measures the dissimilarity between true labels and predicted probabilities.
    
    The goal is to minimize the categorical cross-entropy loss,
    which indicates that the model is able to predict the true labels with a high level of accuracy.
    
    The formulation of the Categorical Cross-Entropy Loss is as follows:
        
        L(y, y_pred) = -(1/n) * Σ(y_i * log(y_pred_i))
        
    where:
        
        y is the true label, which is a one-hot encoded vector
        y_pred is the predicted probability, which is a probability distribution over the classes
        n is the number of samples
        Σ denotes the summation over all classes
        log is the natural logarithm
    
    The true labels are one-hot encoded vectors,
    which means that only one element of the vector is 1 (indicating the true class)
    and the rest are 0. 
    
    The predicted probabilities are probability distributions over the classes,
    which means that they are non-negative and sum to 1.
    
    The goal is to minimize the categorical cross-entropy loss,
    which indicates that the model is able to predict the true labels with a high level of accuracy.
    
    This can be achieved by using optimization techniques
    such as gradient descent to adjust the model's parameters.
    """
    def __init__(self)->classmethod:
        self.__x = np.array([0,0,1])
        self.__y = np.array([0.2,0.3,0.5])
    def __str__(self)->str:
        return "CATEGORİCAL CROSS ENTROPY LOSS CALCULATION - SUBPROCESS"
    def __call__(self)->None:
        return None
    def __getstate__(self)->classmethod:
        raise TypeError("[DENIED-PICKLED]")
    def __repr__(self)->str:
        return CATEGORICALCROSSENTROPYLOSS.__doc__
    def _CALCULATE(self):
        self.__y /= self.__y.sum(axis=-1,keepdims=True)
        self.__y = np.clip(self.__y,1e-7,1-1e-7)
        logy = np.log(self.__y)
        loss = -(self.__x*logy).sum(axis=-1)
        return loss
    
if __name__ == "__main__":
    lss = CATEGORICALCROSSENTROPYLOSS()._CALCULATE()
    print(lss)