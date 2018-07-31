#!/usr/bin/env python
#
# Core Abstract Class for interfacing with equities via the Pandas API.
#

import pandas as pd
from pandas_datareader import data

#TODO: Turn this into a config parser
EQUITIES_DICT = {0: {'ticker'   : 'VZ',
                     'name'     : 'Verizon'},
                 1: {'ticker'   : 'XOM',
                     'name'     : 'ExxonMobil'},
                 2: {'ticker'   : 'CVX',
                     'name'     : 'Chevron'},
                 3: {'ticker'   : 'IBM',
                     'name'     : 'IBM'},
                 4: {'ticker'   : 'PFE',
                     'name'     : 'Pfizer'},
                 5: {'ticker'   : 'KO',
                     'name'     : 'Coca-Cola'},
                 6: {'ticker'   : 'MRK',
                     'name'     : 'Merck'},
                 7: {'ticker'   : 'PG',
                     'name'     : 'Procter & Gamble'},
                 8: {'ticker'   : 'GE',
                     'name'     : 'General Electric'},
                 9: {'ticker'   : 'CSCO',
                     'name'     : 'Cisco Systems'}}

class EquitiesObject(object):
    """
    Get list of top 10 equities with highest dividend payouts in the DOW Jones
    Industrial index.
    """
    
    def __init__(self):
        """
        Construct a pandas data frame of the most recent valuation for each
        stock.
        """
        self.equities_dict = EQUITIES_DICT
        self.equities_df = pd.DataFrame(data = self.equities_dict)
        #import pdb; pdb.set_trace()
        
        #TODO: Make this asynchronous!!!!
        for key, equity in self.equities_df.items():
            self.equities_df[key]['dividend'] = \
                data.DataReader(equity['ticker'],
                                       'yahoo-actions')['value'][:-1]


