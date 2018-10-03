#!/usr/bin/env python
#
# Core Abstract Class
#

import asyncio
import pandas as pd
import aiohttp
import json

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

API_ENDPOINT = "https://api.iextrading.com/1.0"

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

class EquitiesObject(object):
    """
    Data access object for extending to valuation models.
    """

    def __init__(self):
        """
        Set up basic stuff.
        """
        self.api_endpoint = API_ENDPOINT
        self.equities_df = pd.DataFrame.from_dict(EQUITIES_DICT)


    async def get_market_cap(self):
        """
        Append market cap value for tickers in dataframe.
        """
        urls = [
            f"{self.api_endpoint}/stock/{ticker}/stats"
            for ticker in self.equities_df["ticker"]
        ]

        async with aiohttp.ClientSession() as session:
            results = await asyncio.gather(
                *[fetch(session, url) for url in urls]
            )
            results_json = list(map(json.loads, results))

        self.equities_df["market_cap"] = [
            i["marketcap"] for i in results_json
        ]


    async def get_total_debt(self):
        """
        Append total debt value for tickers in dataframe.
        """
        urls = [
            f"{self.api_endpoint}/stock/{ticker}/financials"
            for ticker in self.equities_df["ticker"]
        ]

        async with aiohttp.ClientSession() as session:
            results = await asyncio.gather(
                *[fetch(session, url) for url in urls]
            )
            results_json = list(map(json.loads, results))

        self.equities_df["total_debt"] = [
            i["financials"][0]["totalDebt"] for i in results_json
        ]


    async def get_total_revenue(self):
        """
        Append total revenue value for tickers in dataframe.
        """
        total_revenue_list = []

        for index, row in self.equities_df.iterrows():
            api_get_results = requests.get("{endpoint}/stock/{ticker}/financials"\
                                           .format(endpoint=self.api_endpoint,
                                                     ticker=row["ticker"]))
            total_revenue_list.append(api_get_results.json()["financials"][0]["totalRevenue"])

        self.equities_df["total_revenue"] = total_revenue_list


    async def get_cash_and_equivalents(self):
        """
        Append cash and equivalents for tickers in dataframe. Also known
        as total assets.
        """
        total_assets_list = []

        for index, row in self.equities_df.iterrows():
            api_get_results = requests.get("{endpoint}/stock/{ticker}/financials"\
                                           .format(endpoint=self.api_endpoint,
                                                     ticker=row["ticker"]))
            total_assets_list.append(api_get_results.json()["financials"][0]["totalAssets"])

        self.equities_df["total_assets"] = total_assets_list
