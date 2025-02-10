# 📚 Book Price Scraper

Un scraper avanzado para extraer datos de libros de sitios web, con capacidad de filtrado por categorías y precios. Ideal para análisis de mercado literario o construcción de bases de datos bibliográficas.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)

📂 Estructura del Proyecto

book-price-scraper/
├── scraper/
│   ├── __init__.py
│   └── book_scraper.py      # Script principal
├── tests/
│   ├── __init__.py
│   └── test_scraper.py      # Pruebas unitarias
├── data/                    # Datos generados (ignorado por git)
├── mock_server.py           # Servidor de prueba local
├── test_books.html          # HTML de prueba
├── requirements.txt         # Dependencias
├── LICENSE
└── README.md


## 🚀 Características

- Extracción multi-categoría con paginación automática
- Filtrado por precio máximo por categoría
- Detección automática de disponibilidad en stock
- Sistema de rating adaptable (sitios reales y pruebas locales)
- Exportación a CSV estructurado
- Servidor mock para pruebas locales
- Suite de pruebas unitarias

## ⚙️ Tecnologías Utilizadas

- Python 3.8+
- BeautifulSoup4
- Requests
- Flask (para servidor mock)
- Pytest (para pruebas unitarias)

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Gozv/Web-Scrapping-Py.git
cd book-price-scraper
