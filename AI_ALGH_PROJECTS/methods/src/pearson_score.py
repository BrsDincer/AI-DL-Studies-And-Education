import numpy as np

class PEARSON_SCORE(object):
    """
    This script defines a function [PEARSON_SCORE].
    It takes two array structres as input and returns the Pearson correlation coefficient between them.
    The function uses the formulas for the Pearson correlation coefficient to calculate the numerator and denominator.
    It then divides the numerator by the denominator to get the final score.
    
    Pearson correlation coefficient (also known as Pearson's r) is a measure of the linear correlation between two variables.
    It ranges from -1 to 1.
    
    where:
        -1 indicates a strong negative correlation
        0 indicates no correlation
        1 indicates a strong positive correlation.

    The mathematical formula for the Pearson correlation coefficient is as follows:
    
       r = (n∑(xy) - ∑x∑y) / √((n∑x^2 - (∑x)^2) * (n∑y^2 - (∑y)^2))
    
    Where:
    
        x and y are the two variables being measured
        n is the number of observations
        ∑x is the sum of the x values
        ∑y is the sum of the y values
        ∑x^2 is the sum of the x values squared
        ∑y^2 is the sum of the y values squared
        ∑xy is the sum of the products of the x and y values
    
    In this formula --> 
    the numerator represents the covariance between the two variables,
    while the denominator represents the product of the standard deviations of the two variables.
    
    The value of the Pearson correlation coefficient is the ratio of the covariance to the product of the standard deviations,
    which gives a dimensionless value that can range from -1 to 1.
    
    """
    def __init__(self):
        self.__x = np.arange(1,6,2)
        self.__y = np.arange(6,11,2)
    def __str__(self):
        return "PEARSON SCORE - [Pseudocode]"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[PICKLED-DENIED]")
    def __repr__(self):
        return PEARSON_SCORE.__doc__
    def _CALCULATE(self):
        assert len(self.__x.shape) == 1
        assert len(self.__x.shape) == 1
        n_count = len(self.__x)
        sumx = np.sum(self.__x)
        sumy = np.sum(self.__y)
        sumx_square = np.sum(np.square([i for i in self.__x]))
        sumy_square = np.sum(np.square([i for i in self.__y]))
        p_sum = np.sum([i*j for i,j in zip(self.__x,self.__y)])
        numerator = p_sum-(sumx*sumy/n_count)
        denominator = np.sqrt([((sumx_square-(sumx**2)/n_count)*(sumy_square-(sumy**2)/n_count))])
        if denominator == 0:
            return 0
        return numerator/denominator


if __name__ == "__main__":
    rslt = PEARSON_SCORE()._CALCULATE()
    print(rslt[0])
    