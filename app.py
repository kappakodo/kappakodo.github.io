from flask import Flask, render_template
from flask_frozen import Freezer
import sys
import shutil
import os

app = Flask(__name__)
build_dir = 'build'
app.config['FREEZER_DESTINATION'] = build_dir
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
        print("Freezing site")
        freezer.freeze()
        print("Static site built in the 'build' directory.")
        
        # Manually move 404.html to the build directory
        source_path = os.path.join('templates', '404.html')
        destination_path = os.path.join(build_dir, '404.html')
        if os.path.exists(source_path):
            if not os.path.exists(build_dir):
                os.makedirs(build_dir)
            shutil.copy2(source_path, destination_path)
            print("Manually copied 404.html to build directory.")
        else:
            print("Error: 404.html not found in templates directory.")
    else:
        app.run(debug=True)