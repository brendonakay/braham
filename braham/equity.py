#!/usr/bin/env python
#
# Core Abstract Class
#

import pandas as pd
#from pandas_datareader import data
import requests
import concurrent.futures

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

    def get_market_cap(self):
        """
        Append market cap value for tickers in dataframe.
        """
        market_cap_list = []

        urls = [
            f"{self.api_endpoint}/stock/{ticker}/stats"
            for ticker in self.equities_df["ticker"]
        ]

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
            futures = [pool.submit(requests.get, x) for x in urls]
            for future in concurrent.futures.as_completed(futures):
                market_cap_list.append(future.result().json()["marketcap"])

        # for index, row in self.equities_df.iterrows():
        #     api_get_results = requests.get("{endpoint}/stock/{ticker}/stats"\
        #                                    .format(endpoint=self.api_endpoint,
        #                                              ticker=row["ticker"]))
        #     market_cap_list.append(api_get_results.json()["marketcap"])

        self.equities_df["market_cap"] = market_cap_list

    def get_total_debt(self):
        """
        Append total debt value for tickers in dataframe.
        """
        total_debt_list = []

        urls = [
            f"{self.api_endpoint}/stock/{ticker}/financials"
            for ticker in self.equities_df["ticker"]
        ]

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
            futures = [pool.submit(requests.get, x) for x in urls]
            for future in concurrent.futures.as_completed(futures):
                total_debt_list.append(future.result().json()["financials"][0]["totalDebt"])

        # for index, row in self.equities_df.iterrows():
        #     api_get_results = requests.get("{endpoint}/stock/{ticker}/financials"\
        #                                    .format(endpoint=self.api_endpoint,
        #                                              ticker=row["ticker"]))
        #     total_debt_list.append(api_get_results.json()["financials"][0]["totalDebt"])

        self.equities_df["total_debt"] = total_debt_list

    def get_total_revenue(self):
        """
        Append total revenue value for tickers in dataframe.
        """
        total_revenue_list = []

        urls = [
            f"{self.api_endpoint}/stock/{ticker}/financials"
            for ticker in self.equities_df["ticker"]
        ]

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
            futures = [pool.submit(requests.get, x) for x in urls]
            for future in concurrent.futures.as_completed(futures):
                total_revenue_list.append(future.result().json()["financials"][0]["totalRevenue"])

        # for index, row in self.equities_df.iterrows():
        #     api_get_results = requests.get("{endpoint}/stock/{ticker}/financials"\
        #                                    .format(endpoint=self.api_endpoint,
        #                                              ticker=row["ticker"]))
        #     total_revenue_list.append(api_get_results.json()["financials"][0]["totalRevenue"])

        self.equities_df["total_revenue"] = total_revenue_list

    def get_cash_and_equivalents(self):
        """
        Append cash and equivalents for tickers in dataframe. Also known
        as total assets.
        """
        total_assets_list = []

        urls = [
            f"{self.api_endpoint}/stock/{ticker}/financials"
            for ticker in self.equities_df["ticker"]
        ]

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as pool:
            futures = [pool.submit(requests.get, x) for x in urls]
            for future in concurrent.futures.as_completed(futures):
                total_assets_list.append(future.result().json()["financials"][0]["totalAssets"])

        # for index, row in self.equities_df.iterrows():
        #     api_get_results = requests.get("{endpoint}/stock/{ticker}/financials"\
        #                                    .format(endpoint=self.api_endpoint,
        #                                              ticker=row["ticker"]))
        #     total_assets_list.append(api_get_results.json()["financials"][0]["totalAssets"])

        self.equities_df["total_assets"] = total_assets_list
