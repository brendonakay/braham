#!/usr/bin/env python
#
# The Acquirer's Multiple valuation method.
#     source: https://acquirersmultiple.com/faq/
#
#     Intrinsic Value = Enterprise Value / Operating Earnings*
#
#     Operating earnings is constructed from the top of the income statement
#       down, where EBIT is constructed from the bottom up.
#
#    TODO: - Expand on denominator value for AM. It is more than just total rev.
#          - Make calculations asynchronous.

from equity import EquitiesObject

class AMEquity(EquitiesObject):
    """
    Variables:
        Enterprise Value - Market Cap + Market Value of Debt - Cash Equivalents
        Operating Earnings - Revenue - (Cost of goods sold
                                      + Selling, general admin costs
                                      + Deprectiation of amortization)
    """

    def __init__(self):
        super().__init__()
        self.get_market_cap()
        self.get_total_debt()
        self.get_cash_and_equivalents()
        self.get_total_revenue()
        self._calculate_acquirers_multiple()

    def _calculate_acquirers_multiple(self):
        self.equities_df["acquirers_multiple"] = (self.equities_df["market_cap"]\
                                                + self.equities_df["total_debt"]\
                                                - self.equities_df["total_assets"])\
                                                / \
                                                self.equities_df["total_revenue"]

ame = AMEquity()
print(ame.equities_df)