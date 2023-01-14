import numpy as np

class STANDART_DEVIATION_SCORE(object):
    """
    This script defines a function [STANDART_DEVIATION_SCORE]
    It takes a data as input and returns the standard deviation of the data.
    
    Standard deviation is a measure of the spread or dispersion of a set of data values.
    
    It gives an idea of how much the individual data points deviate from the mean or average of the set.
    
    The formula for the sample standard deviation (for a set of n observations) is:

        s = √(Σ(x_i - x_bar)^2 / (n-1))
    
    Where:
    
        x_i is the i-th observation
        x_bar is the sample mean
        n is the number of observations
        Σ denotes the sum over all observations
        
    The standard deviation is the square root of the sample variance,
    which is calculated by taking the average of the squared differences between each data point and the mean.
    
    The standard deviation is useful in many ways,
    for example it is used in statistics to measure the spread of a distribution and in finance it's used to measure the volatility of a stock.
    
    It is also used to calculate the z-score,
    which tells how many standard deviations a data point is from the mean of the data.
    
    """
    def __init__(self):
        self.__x = np.arange(1,11,2)
    def __str__(self):
        return "STANDART DEVIATION - [Pseudocode]"
    def __call__(self):
        return None
    def __getstate__(self):
        raise TypeError("[PICKLED-DENIED]")
    def __repr__(self):
        return STANDART_DEVIATION_SCORE.__doc__
    def _CALCULATE(self):
        n_count = len(self.__x)
        datamean = np.sum([self.__x])/n_count
        variance = np.sum([(i-datamean)**2 for i in self.__x])/(n_count-1)
        sqrtvariance = np.sqrt([variance])
        return sqrtvariance

if __name__ == "__main__":
    rslt = STANDART_DEVIATION_SCORE()._CALCULATE()
    print(rslt[0])