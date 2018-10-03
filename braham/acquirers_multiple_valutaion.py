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

import asyncio
from equity import EquitiesObject

async def create_ame(): #TODO rename this
    ame = AMEquity()
    await ame._init_async()
    return ame

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

    async def _init_async(self):
        await self.get_market_cap()
        await self.get_total_debt()
        await self.get_total_revenue()
        await self.get_cash_and_equivalents()
        await self._calculate_acquirers_multiple()

    async def _calculate_acquirers_multiple(self):
        self.equities_df["acquirers_multiple"] = (self.equities_df["market_cap"]\
                                                + self.equities_df["total_debt"]\
                                                - self.equities_df["total_assets"])\
                                                / \
                                                self.equities_df["total_revenue"]

async def main():
    ame = await create_ame()
    print(ame.equities_df)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
