#!/usr/bin/python3
"""
script that starts a Flask web application
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hhbnb():
    """Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cIsFun(text):
    """
    display “C ” followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonIsCool(text='is cool'):
    """
    display “Python ” followed by the value of the text
    variable (replace underscore _ symbols with a space )
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
     display “n is a number” only if n is an integer
    """
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def is_number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def is_number_template_odd(n):
    """
    display a HTML page only if n is an integer and said if is odd or even
    """
    if n % 2 == 0:
        is_odd = 'even'
    else:
        is_odd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, is_odd=is_odd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
