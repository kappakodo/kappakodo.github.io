# app.py

from flask import Flask, render_template
from flask_frozen import Freezer
import sys

app = Flask(__name__)
app.config['FREEZER_DESTINATION'] = 'build'
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news/')
def news():
    return render_template('news.html')

@app.route('/reviews/')
def reviews():
    return render_template('review.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        print("❄️  Freezing site (shell pages + 404 router)...")
        freezer.freeze()
        print("✅ Static site built in the 'build' directory.")
    else:
        app.run(debug=True)