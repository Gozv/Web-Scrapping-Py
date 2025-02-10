import pytest
import os
from scraper.book_scraper import BookScraper  # Importa desde el paquete scraper


def test_parse_books():
    """Prueba el método parse_books con un archivo HTML de prueba."""
    scraper = BookScraper("http://localhost:5000")  # Usa el servidor mock
    
    # Cargar HTML de prueba
    with open('../test_books.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    books = scraper.parse_books(html, "test", max_price=30)
    
    # Verificaciones
    assert len(books) == 1  # Solo un libro bajo $30
    assert books[0]['title'] == "Python para Principiantes"
    assert books[0]['price'] == 29.99
    assert books[0]['rating'] == 3
    assert books[0]['available'] is True


def test_scrape_category():
    """Prueba el método scrape_category usando el servidor mock."""
    scraper = BookScraper("http://localhost:5000")  # Usa el servidor mock
    
    # Usar categoría simulada y parámetros correctos
    books = scraper.scrape_category(
        category='travel',  # Categoría simulada
        pages=1,
        max_price=50
    )
    
    # Verificaciones
    assert len(books) > 0
    assert all(isinstance(book['price'], float) for book in books)
    assert all('travel' == book['category'] for book in books)


def test_save_to_csv(tmp_path):
    """Prueba el método save_to_csv."""
    scraper = BookScraper("http://localhost:5000")
    
    # Datos de prueba
    data = [
        {
            'title': 'Libro de Prueba',
            'price': 19.99,
            'category': 'test',
            'rating': 4,
            'available': True
        }
    ]
    
    # Ruta temporal para el archivo CSV
    csv_file = tmp_path / "test_output.csv"
    
    # Guardar datos en CSV
    scraper.save_to_csv(data, str(csv_file))
    
    # Verificar que el archivo fue creado
    assert csv_file.exists()
    
    # Leer el archivo CSV y verificar su contenido
    with open(csv_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    assert len(lines) == 2  # Encabezado + una fila de datos
    assert "Libro de Prueba" in lines[1]