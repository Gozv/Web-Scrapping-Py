import pytest
from scraper.book_scraper import BookScraper
import os

def test_parse_books():
    scraper = BookScraper("http://localhost:5000")
    
    # Cargar HTML de prueba
    with open(os.path.join(os.path.dirname(__file__), '..', 'test_books.html'), 'r', encoding='utf-8') as f:
        html = f.read()
    
    books = scraper.parse_books(html, "test", max_price=30)
    
    assert len(books) == 1
    assert books[0]['title'] == "Python para Principiantes"
    assert books[0]['rating'] == 3
    assert books[0]['available'] is True

def test_scrape_category():
    scraper = BookScraper("http://books.toscrape.com")
    books = scraper.scrape_category('travel_2', pages=1)
    assert len(books) > 0
    assert all(isinstance(book['price'], float) for book in books)