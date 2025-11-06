import requests
from requests_oauthlib import OAuth1
import json
from datetime import datetime

# --- Your API credentials ---
consumer_key = "40486486b474443980ac02ad8ad8bb00"
consumer_secret = "2c676b8384344b8490dddf99ea966fb2"

# --- API endpoint and parameters ---
url = "https://platform.fatsecret.com/rest/server.api"
params = {
    "method": "foods.search",          # Example method
    "search_expression": "coke",      # Change to any food you want
    "format": "json"
}

# --- OAuth 1.0 authentication ---
auth = OAuth1(consumer_key, consumer_secret)

# --- Send GET request ---
response = requests.get(url, params=params, auth=auth)

# --- Check for success ---
if response.status_code == 200:
    data = response.json()
    print("✅ Data fetched successfully!")

    # --- Create a filename with timestamp ---
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"fatsecret_foods_{timestamp}.json"

    # --- Save JSON data to file ---
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    print(f"💾 JSON saved as: {filename}")
else:
    print("❌ Failed to fetch data.")
    print("Status code:", response.status_code)
    print("Response:", response.text)
