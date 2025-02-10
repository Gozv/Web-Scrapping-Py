from flask import Flask, send_file
import os

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/')
def home():
    return "Mock Server Funcionando", 200

@app.route('/catalogue/category/books/<category>/page-<int:page>.html')
def mock_category(category, page):
    file_path = os.path.join(os.path.dirname(__file__), 'test_books.html')
    return send_file(file_path)

if __name__ == '__main__':
    app.run(port=5000, debug=False)