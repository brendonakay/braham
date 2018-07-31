# braham
Stock valuation using the discount dividend model.

From Chapter 5: [Python for Finance - Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/python-finance-second-edition)

## Installation
* Install [venv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
* Fish:
    * `source venv/bin/activate.fish`
* BASH:
    * `source venv/bin/activate`
* `pip install -r requirements.txt`
* Don't forget `sudo apt-get install python3-tk`

### Mission:
- Dividend approach
  - Pull information for variables from the top 10 dividend paying companies
 in the DOW Industrial.
  - Synchronously process each equity using the share repurchase  and the total
 payout model.
  - Serve up in a digestible GUI. Jupyter notebook? REACT?

- Enterprise value approach
   I'm unsure how to approach this one, so I'll start simple and build from
there.
  - Pull information for variables from the top 10 dividend paying companies
 in the DOW Industrial.
    - API: Pandas
  - Synchronously process each equity using the future free cash flows method.
  - Serve up in same GUI interface.
