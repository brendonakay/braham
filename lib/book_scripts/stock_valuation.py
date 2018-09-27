#!/usr/bin/env python
#
# Classes and functions given as examples from Chapter 5
# in the book.
#
# Stock valuation using the dividend discount model
#

import scipy as sp

if __name__ == "__main__":
    """
    Go go super awesome stock valutation DDM
    """

    """
    Present Value demo:
    Given R=12%; D=1; and FV=50, where
        R is appropriate cost of equity
        D is the dividend
        and FV is the future value
    """
    sp.pv(0.12, 1, 1 + 50)

    """
    Grammatical growth demo:
    """
    dividends = [1.80, 2.07, 2.48193, 2.680, 2.7877]
    R = 0.182
    g = 0.03

    print(float(sp.npv(R, dividends[:-1]) * (1 + R)))
