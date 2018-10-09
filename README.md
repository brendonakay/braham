# braham
Stock valuation app.

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
    * `flask init-db`
    * `flask run`
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

- Acquirers Multiple
  - [AM](https://acquirersmultiple.com/faq/)

