from flask import Flask, send_from_directory
import os

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/catalogue/category/books/<category>/page-<int:page>.html')
def books(category, page):
    return send_from_directory(
        os.path.join(os.path.dirname(__file__), 'tests'),
        'test_books.html'
    )

if __name__ == '__main__':
    app.run(port=5000)