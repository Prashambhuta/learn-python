"""
Write function stdDevOfLengths(L) that takes in a list of strings (L) and
outputs the sd of the lengths of strings, return float('NaN') if L is empty.

Returns://
    sd of the lengths, float('NaN') if empty
"""

import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"
import numpy as np


# def stdDevOfLengths(L):
#     """
#     returns the std dev of the length of the strings.
#
#         Parameters:
#                 L (list): list of strings
#
#         Returns:
#                 float: std dev of the lengths of strings.
#     """
#     if not L:
#         return float('NaN')
#     len_of_strings = []
#     tot = 0
#     for string in L:
#         len_of_strings.append(len(string))
#         tot += len(string)
#
#     mean = tot/len(len_of_strings)
#     var = 0
#     for n in len_of_strings:
#         var += (n - mean)**2
#     std = (var/len(len_of_strings))**0.5
#     return std

def stdDevOfLengths(L):
    """
    returns the std dev of the length of the strings.

        Parameters:
                L (list): list of strings

        Returns:
                float: std dev of the lengths of strings.
    """
    if not L:
        return float('NaN')
    std = np.std([len(i) for i in L])
    print(std)

stdDevOfLengths(['nybsqfrenaim', 'butaell', '', 'jewyw', 'jkwe', 'ianqb'])