#!/usr/bin/env python
#
# Classes and functions given as examples from Chapter 5
# in the book.
#
# Stock valuation using the total payout model
#
#     Share Price = PV(Future total dividends * Repurchases) 
#                   / Shares outstanding
#
#             ... = (Dividends * Repurchases) / Shares outstanding

from equity import EquitiesObject
from pandas_datareader import data
import datetime

class DividendEquity(EquitiesObject):
    """
    Variables:
        DIVIDEND     - Dividend rate ... e.g. $1,000/yr
        SHARE_REPUR  - Share repurshaes rate ... e.g. $500/yr
        EQUITY_CAP   - Cost of equity capital ... e.g. 11%
        GROWTH_RATE  - Growth rate ... e.g. 7%
        SHARES_OUTS  - Shares outstanding ... e.g. 100,000

    Valutaion exaple:
        share_price = ((1000 + 500) / (.11 - .07)) / 100000
    """

    def __init__(self):
        super().__init__()

    def _generate_dividend_dataframe(self):
        #TODO: Make this asynchronous!!!!
        for ticker in self.equities_dict['ticker']:
            year_start = '2018-01-01' 
            now = datetime.datetime.now()
            self.dividend_df.concat = \
                data.DataReader(ticker,
                                'yahoo-dividends',
                                '{}-{}-{}'.format(now.year,now.month,now.day),
                                '{}-{}-{}'.format(now.year,now.month,now.day))

