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

from . import equity

class DividendEquity(EquitiesObject):
    """
    Variables:
        DIVIDEND     - Dividend rate ... e.g. $1,000/yr
        SHARE_REPUR  - Share repurshaes rate ... e.g. $500/yr
        EQUITY_CAP   - Cost of equity capital ... e.g. 11%
        GROWTH_RATE  - Growth rate ... e.g. 7%
        SHARES_OUTS  - Shares outstanding 100,000

    Valutaion exaple:
        share_price = ((1000 + 500) / (.11 - .07)) / 100000
    """
