import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import random

class BookScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.session = requests.Session()
        
    def fetch_page(self, url):
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

    def parse_books(self, html, category, max_price=None):
        soup = BeautifulSoup(html, 'html.parser')
        books = []
        
        # Selector genérico (ajustar según sitio real)
        for book in soup.select('article.product_pod'):
            title = book.select_one('h3 a')['title'].strip()
            price_text = book.select_one('p.price_color').text.strip()
            price = float(price_text.replace('£', '').replace(',', ''))
            
            if max_price and price > max_price:
                continue
            
            # Rating basado en clases (ej: 'star-rating Three')
            rating_class = book.select_one('p.star-rating')['class'][1]
            rating_map = {
                'One': 1,
                'Two': 2,
                'Three': 3,
                'Four': 4,
                'Five': 5
            }
            
            books.append({
                'title': title,
                'price': price,
                'category': category,
                'rating': rating_map.get(rating_class, 0),
                'available': 'In stock' in book.select_one('p.availability').text
            })
            
        return books

    def scrape_category(self, category, pages=3, max_price=None):
        all_books = []
        
        for page in range(1, pages + 1):
            print(f"Scraping {category} - Página {page}")
            url = f"{self.base_url}/catalogue/category/books/{category}/page-{page}.html"
            html = self.fetch_page(url)
            
            if html:
                all_books.extend(self.parse_books(html, category, max_price))
            
            sleep(random.uniform(1, 3))
            
        return all_books

    def save_to_csv(self, data, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

if __name__ == "__main__":
    scraper = BookScraper("http://books.toscrape.com")
    
    categories = {
        'travel_2': {'pages': 2, 'max_price': 50},
        'mystery_3': {'pages': 3, 'max_price': 30}
    }
    
    all_books = []
    for category, params in categories.items():
        books = scraper.scrape_category(
            category=category,
            pages=params.get('pages', 2),
            max_price=params.get('max_price', None)
        )
        all_books.extend(books)
    
    if all_books:
        scraper.save_to_csv(all_books, 'books_data.csv')
        print(f"Datos guardados correctamente. Total de libros: {len(all_books)}")
    else:
        print("No se encontraron libros con los filtros aplicados")