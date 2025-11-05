# Barcode_scanner-app
A Python-based application that scans product barcodes and retrieves detailed food product information by integrating with open, free APIs such as Open Food Facts. The system is designed for hackathon use, rapid prototyping, or educational demos.
# Barcode Food Info Scanner & Health Classifier

A Python hackathon/demo project: scan a food product barcode, instantly retrieve open food information, and classify healthiness using machine learning. Built around the Open Food Facts API and ready for further ML integration.

## Features

- **Barcode Scanning**: Extract UPC/EAN codes from product packaging (integrate your favorite barcode library)
- **Open Data Lookup**: Connects to the Open Food Facts API for product details (ingredients, nutrition, allergens, etc.)
- **Free and Public Datasets**: No API keys or authentication required for Open Food Facts
- **Health Classification Ready**: Use Nutri-Score and nutrition facts to train and test a healthy/unhealthy prediction model
- **Python-first**: Works with Python 3.x, easily extensible for web/backend or mobile projects

## Tech Stack

- Python 3.x
- `requests` for API calls
- [Open Food Facts API](https://world.openfoodfacts.org/data)
