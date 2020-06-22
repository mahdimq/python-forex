from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes, RatesNotAvailableError
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = "secret123abc"
debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

"""import Forex Methods"""
c = CurrencyRates()  # <-- Currency rates
s = CurrencyCodes()  # <-- Currency Codes/Symbols


@app.route("/")
def index():
    """render Home/Index Page"""
    return render_template("index.html")


@app.route("/currency", methods=["GET"])
def show_rates():
    """Error handling if form input is empty
    and return a flash message if error thrown"""
    if not request.args['from']:
        flash("Currency cannot be blank.")
        return redirect("/")
    if not request.args['to']:
        flash("Currency cannot be blank.")
        return redirect("/")
    if not request.args['amount']:
        flash("Amount cannot be blank.")
        return redirect("/")

    """Get data from form input and save to variables"""
    from_curr = request.args["from"].upper()  # <-- get currency 1 input value
    to_curr = request.args['to'].upper()  # <-- get currency 2 input value
    initial_amount = float(request.args['amount'])  # <-- get amount as a float
    symbol = s.get_symbol(to_curr)  # <-- get symbol from Currency method
    from_curr_name = s.get_currency_name(from_curr)  # <-- get currency name
    to_curr_name = s.get_currency_name(to_curr)  # <-- get currency name

    # Using a try catch method to check if Currency codes are invalid
    try:
        """convert currency from user inputs and rounding to 2 decimal places"""
        convert = round(c.convert(from_curr, to_curr, initial_amount), 2)
    except RatesNotAvailableError:
        """shows flash error message if currency codes invalid
        and user is redirected to homescreen"""
        flash('Currency Code not valid')
        return redirect("/")

    return render_template("currency.html",
                           from_curr=from_curr,
                           to_curr=to_curr,
                           initial_amount=initial_amount,
                           converted_amount=convert,
                           symbol=symbol,
                           curr_name1=from_curr_name,
                           curr_name2=to_curr_name)
