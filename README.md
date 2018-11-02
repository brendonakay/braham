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
* Flask setup commands
    * `export FLASK_APP=braham_flask`
    * `export FLASK_ENV=development`
    * `flask init-db`
    * `flask run`
* Tutorial
    * [Tutorial](http://flask.pocoo.org/docs/1.0/tutorial/)

## Mission:
- Implement Valuation Equity meta DAO.
  - IEX API.
  - Base class for valuation models.

- Implement Systemaptic Equity meta DAO.
    - IEX API? May need something better...
    - Consider the strategy.

### Valuation:

- Dividend approach
  - Pull information for variables from the top 10 dividend paying companies in the DOW Industrial.
  - Asynchronously process each equity using the share repurchase  and the total payout model.
  - Serve up in a digestible GUI. TODO: Flask app

- Acquirers Multiple
  - [AM](https://acquirersmultiple.com/faq/)

### Systematic:

- [Pairs trading approach](https://www.quantopian.com/lectures/introduction-to-pairs-trading)
  - May need to set up a crawler to identify optimal pairs in a market.
  - Get the basics implemented.
    - Maybe one from [here](https://www.quantopian.com/posts/how-to-build-a-pairs-trading-strategy-on-quantopian)
  - Try implementing a system with options as the execution instrument.
    - Implement one pair system with long/short options strategies according to what the pair trading strategy indicates.

- Write a back tester! To be done right after first strategy is implemented. Maybe even concurrently.
