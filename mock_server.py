from flask import Flask, send_file
import os

app = Flask(__name__)
app.config['TESTING'] = True


@app.route('/')
def home():
    return "Mock Server Funcionando", 200


@app.route('/catalogue/category/books/<category>_2/page-<int:page>.html')
def mock_category(category, page):
    file_path = os.path.join(os.path.dirname(__file__), f'test_{category}_page{page}.html')
    if os.path.exists(file_path):
        return send_file(file_path)
    return "Página no encontrada", 404


if __name__ == '__main__':
    app.run(port=5000, debug=False)

# Prueba en local
# scraper = BookScraper("http://localhost:5000") 

