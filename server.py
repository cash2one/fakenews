import os
from flask import Flask, render_template
from random import choice
from fakenews import do_generate, do_fetch, get_trends

app = Flask(__name__)


@app.route("/")
def homepage():
    publication = choice(['demorgen', 'hln'])
    do_fetch(publication)
    items = do_generate(publication)
    trends = get_trends()

    return render_template('homepage.html', items=items, trends=trends)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
