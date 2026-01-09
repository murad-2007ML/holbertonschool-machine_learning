#!/usr/bin/env python3
""" to plot y as a line graph"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    y should be plotted as a solid red line
    The x-axis should range from 0 to 10
    """
    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))
    plt.xlim(0, 10)
    plt.plot(y, color="red")
