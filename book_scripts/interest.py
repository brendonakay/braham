#!/usr/bin/env python
#
# Classes and functions given as examples from Chapter 5
# in the book.
#
# Intro
#

import numpy as np
from math import log

class APR_obj():
    """
    Annual Percentage Rate stuff
    """

    def APR2Rm(self, APR1: float, m1: int, m2: int) -> float:
        """
        APR1: annual percentage rate
          m1: compounding frequency for APR1
          m2: effective period rate of our target effective rate

        Example #1>>>APR2Rm(0.1,2,4)
        0.02469507659595993
        """
        return (1+APR1/m1)**(m1/m2)-1

    def APR2APR(self, APR1: float, m1: int, m2: int) -> float:
        """
        APR1: annual percentage rate
          m1: compounding frequency for APR1
          m2: effective period rate of our target effective rate

        Example #1>>>APR2APR(0.1,2,4)
        0.02469507659595993
        """
        return m2*((1+APR1/m1)**(m1/m2)-1)

    def APR2Rc(self, APR, m):
        """
        TODO: comment
        """
        return m*log(1+APR/m)

    def EAR_f(self, APR: float, m: int) -> float:
        """
        TODO: comment
        """
        return (1+APR/m)**m-1

    def Rc2APR(self, Rc: float, m: int) -> float:
        """
        TODO: comment
        """
        return m*(exp(Rc/m)-1)

    def Rc2Rm(self, Rc: float, m: int) -> float:
        """
        TODO: comment
        """
        return exp(Rc/m)-1


if __name__ == "__main__":
    """
    Go go gadget this thing.
    """
    days = 365
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    ms = seconds*1000
    x = np.array([1,
                  2,
                  4,
                  12,
                  days,
                  hours,
                  minutes,
                  seconds,
                  ms])

    apr = APR_obj()
    apr.APR = 0.1

    for i in x:
        print(apr.EAR_f(apr.APR,i))

