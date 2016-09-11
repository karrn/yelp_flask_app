import myyelp
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    term = request.values.get('term')
    results = None
    if address:
        results = myyelp.results(address, term)
        #address = address.title()
    if term:
    	term = term.title()
    return render_template('index.html', results=results, address=address, term=term)

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
    port =int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
