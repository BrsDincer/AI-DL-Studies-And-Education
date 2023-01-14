import numpy as np

class SPEARMAN_SCORE(object):
    """
    This script will output the Spearman correlation between the two arrays of data.
    
    Spearman correlation is a statistical measure of the relationship between two variables that assesses the strength and direction of the monotonic association between them.
    It is based on the rank of the values rather than the actual values, and ranges from -1 (perfectly negatively correlated) to 1 (perfectly positively correlated).
    It is commonly used to determine the correlation between two variables when the data is ordinal,
    rather than interval or ratio.
    
    """
    def __init__(self):
        self.__x = np.arange(1,6,1)
        self.__y = np.arange(2,7,1)
    def __str__(self):
        return "SPEARMAN SCORE - [Pseudocode]"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[PICKLED-DENIED]")
    def __repr__(self):
        return SPEARMAN_SCORE.__doc__
    def _CALCULATE(self):
        assert len(self.__x.shape) == len(self.__y.shape)
        n_count = len(self.__x)
        xrank = np.argsort(self.__x)
        yrank = np.argsort(self.__y)
        difference = xrank-yrank
        difference_square = difference**2
        sum_difference_square = np.sum(difference_square)
        spearman = 1 - (6*sum_difference_square)/(n_count*((n_count**2)-1))
        return spearman
 
if __name__ == "__main__":
    rslt = SPEARMAN_SCORE()._CALCULATE()
    print(rslt)