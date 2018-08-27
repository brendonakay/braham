# braham
<<<<<<< HEAD
Stock valuation app.
=======
Stock valuation and Flask experiment. The `book_scripts` directory was written
from examples out of chapter 5 in [Python for Finance - Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/python-finance-second-edition)
>>>>>>> wip

## Installation
* Python 3.7
* [venv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
* Fish:
    * `source venv/bin/activate.fish`
* BASH:
    * `source venv/bin/activate`
* `pip install -r requirements.txt`
* Don't forget `sudo apt-get install python3-tk`

## Flask
* Flask variables
    * `export FLASK_APP=braham_flask`
    * `export FLASK_ENV=development`
* Tutorial
    * [Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/)

## Mission:
- Implement Equity meta dao
  - IEX API

- Dividend approach
  - Pull information for variables from the top 10 dividend paying companies
 in the DOW Industrial.
  - Asynchronously process each equity using the share repurchase  and the total
 payout model.
  - Serve up in a digestible GUI. TODO: Flask app

<<<<<<< HEAD
- Enterprise value approach
   I'm unsure how to approach this one, so I'll start simple and build from
there.
  - Pull information for variables from the top 10 dividend paying companies
 in the DOW Industrial.
    - API: Pandas
  - Asynchronously process each equity using the future free cash flows method.
  - Serve up in same GUI interface.

- [Acquirer's Multiple](https://acquirersmultiple.com/faq/)

#### Book Scripts:
From Chapter 5: [Python for Finance - Second Edition](https://www.packtpub.com/big-data-and-business-intelligence/python-finance-second-edition)
=======
- Acquirers Multiple
  - [AM](https://acquirersmultiple.com/faq/)

>>>>>>> wip
