#!/usr/bin/env python3
"""
initializing normal dist class
"""


class Normal:
    """
    class to show functions of Normal distribution
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        data: list of data given
        mean: self attribute of the mean of the data
        stddev: standard error of the data
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            sigma = 0
            for i in range(len(data)):
                sigma += (data[i] - self.mean)**2
            self.stddev = (sigma / len(data)) ** (1 / 2)

    def z_score(self, x):
        """
        calculating z-score
        """
        z = (x - self.mean) / self.stddev
        return z

    def x_value(self, z):
        """
        calculating x_value
        """
        x = z * self.stddev + self.mean
        return x
