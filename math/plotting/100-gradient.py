#!/usr/bin/env python3
"""to create a scatter plot of sampled elevations on a mountain"""
import numpy as np
import matplotlib.pyplot as plt


def gradient():
    """
    The x-axis should be labeled x coordinate (m)
    The y-axis should be labeled y coordinate (m)
    The title should be Mountain Elevation
    A colorbar should be used to display elevation
    The colorbar should be labeled elevation (m)
    """
    np.random.seed(5)

    x = np.random.randn(2000) * 10
    y = np.random.randn(2000) * 10
    z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))
    plt.figure(figsize=(6.4, 4.8))
    plt.xlabel("x coordinate (m)")
    plt.ylabel("y coordinate (m)")
    plt.title("Mountain Elevation")
    plt.colorbar().set_label("elevation (m)")
    plt.scatter(x, y, c=z)
    plt.show()
