#!/usr/bin/env python
#
# Core Abstract Class for interfacing with equities via the Pandas API.
#

import pandas as pd
from pandas_datareader import data

#TODO: * Turn this into a config parser
#      * Refactor data input to something more dynamic.
EQUITIES_DICT = {"name" : ['Verizon',
                           'ExxonMobil',
                           'Chevron',
                           'IBM',
                           'Pfizer',
                           'Coca-Cola',
                           'Merck',
                           'Procter & Gamble',
                           'General Electric',
                           'Cisco Systems'],
               "ticker" : ['VZ',
                           'XOM',
                           'CVX',
                           'IBM',
                           'PFE',
                           'KO',
                           'MRK',
                           'PG',
                           'GE',
                           'CSCO']}

class EquitiesObject(object):
    """
    Get list of top 10 equities with highest dividend payouts in the DOW Jones
    Industrial index.
    """

    def __init__(self):
        """
        Construct a pandas data frames
        """
        # Equities
        self.equities_dict = EQUITIES_DICT
        self.equities_df = pd.DataFrame(data = self.equities_dict)

        # Dividends
        self.dividend_df_dict = {}
