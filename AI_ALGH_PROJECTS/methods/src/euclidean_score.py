import numpy as np

class EUCLIDEAN_SCORE(object):
    """
    This script defines a function [EUCLIDEAN_SCORE].
    It takes two array structures as input and returns the Euclidean score between them.
    """
    def __init__(self):
        self.__x = np.arange(1,6,2)
        self.__y = np.arange(6,11,2)
    def __str__(self):
        return "EUCLIDEAN SCORE - [Pseudocode]"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[PICKLED-DENIED]")
    def __repr__(self):
        return EUCLIDEAN_SCORE.__doc__
    def _CALCULATE(self):
        assert len(self.__x.shape) == 1
        assert len(self.__x.shape) == 1
        distance_sum = np.sum([(a-b)**2 for a,b in zip(self.__x,self.__y)])
        sqrt_sum = np.sqrt(distance_sum)
        return sqrt_sum
    
if __name__ == "__main__":
    rslt = EUCLIDEAN_SCORE()._CALCULATE()
    print(rslt)