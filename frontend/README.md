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

## Tech Stack

- **Frontend:** HTML, CSS, and vanilla JavaScript.
- **Styling:** [Tailwind CSS](https://tailwindcss.com/) is used for styling the user interface.
- **Barcode Scanning Library:** [Quagga2.js](https://github.com/ericblade/quagga2) is used for barcode detection.

## How to Use

1.  Open the `index.html` file in the `frontend` directory in a web browser.
2.  Click the "Select Multiple Photos" button to upload images containing barcodes.
3.  The uploaded photos will be displayed in a grid.
4.  Click the "Scan All Barcodes Now" button to start the scanning process.
5.  The results will be displayed in a table.
6.  You can then copy the barcodes to your clipboard or export them as a CSV file.

