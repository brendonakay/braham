#!/usr/bin/env python
#
# Classes and functions given as examples from Chapter 5
# in the book.
#
# Bonds lol
#

from matplotlib.pyplot import *
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # time=[3/12,6/12,2,3,5,10,30]
    # rate=[0.47,0.6,1.18,1.53,2,2.53,3.12]
    # title("Term Structure of Interest Rate ")
    # xlabel("Time ")
    # ylabel("Risk-free rate (%)")
    # plot(time,rate)
    # show()

    # .interpolate()
    x = pd.Series([1,2,np.nan,np.nan,6])
    x.interpolate()

    nan = np.nan
    x = pd.Series([2,nan,nan,nan,nan,2.53])

    x.interpolate()
