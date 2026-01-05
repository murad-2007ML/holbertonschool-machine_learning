#!/usr/bin/env python3
"""loading data from array"""
import pandas as pd


def from_file(filename, delimiter):
    """loading data from array"""
    return pd.read_csv("filename", sep=delimiter)
