import requests

def get_product_info(barcode):
    url = f'https://world.openfoodfacts.org/api/v0/product/{barcode}.json'
    response = requests.get(url)
    if response.ok:
        data = response.json()
        if data.get('status') == 1:
            return data['product']
        else:
            print('Product not found in the database.')
            return None
    else:
        print('Error:', response.status_code)
        return None

a= int(input("enter the number: "))
barcode = a  # Example barcode for Nutella
product = get_product_info(barcode)

if product:
    print("Product Name:", product.get('product_name'))
    print("Brands:", product.get('brands'))
    print("Ingredients:", product.get('ingredients_text'))
    print("Nutritional Grade:", product.get('nutrition_grades', 'Not Available'))
    print("Allergens:", product.get('allergens', 'None'))
    print("Image URL:", product.get('image_url', 'No Image'))
