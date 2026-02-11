#!/usr/bin/env python3
"""
Script to calculate a Binomial distribution
"""


class Binomial:
    """
    class to show functions of binomial dist.
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        initializing the data
        """
        self.data = data
        self.n = n
        self.p = p
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if not (p > 0 and p < 1):
                raise ValueError('p must be greater than 0 and less than 1')
        else:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if not (p > 0 and p < 1):
                raise ValueError('p must be greater than 0 and less than 1')
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            variance = sum((x-mean)**2 for x in data) / len(data)
            p = 1 - (variance / mean)
            self.n = int(round(mean/p))
            self.p = float(mean/self.n)
