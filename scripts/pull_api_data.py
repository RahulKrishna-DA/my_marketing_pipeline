import os
import json
import requests

print("🌐 Initializing Live API Data Pull via HTTP Requests...")

# 1. Define where the data will land in our Data Lakehouse
LAKEHOUSE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_lakehouse'))
output_file_path = os.path.join(LAKEHOUSE_DIR, 'raw_exchange_rates.json')

# Ensure the directory exists just in case
os.makedirs(LAKEHOUSE_DIR, exist_ok=True)

# 2. Define the public API endpoint (using USD as our base currency)
URL = "https://open.er-api.com/v6/latest/USD"

try:
    print(f"🚀 Pinging API endpoint: {URL}")
    response = requests.get(URL, timeout=10)
    
    # Check if the HTTP request was successful (Status Code 200)
    response.raise_for_status()
    
    # Parse the incoming network data into clean Python JSON object
    api_data = response.json()
    
    print("⏳ Filtering response for our target pipeline currencies (USD, EUR, GBP)...")
    all_rates = api_data.get("rates", {})
    filtered_rates = {
        "base_currency": "USD",
        "extracted_at": api_data.get("time_last_update_utc"),
        "rates": {
            "USD": all_rates.get("USD", 1.0),
            "EUR": all_rates.get("EUR"),
            "GBP": all_rates.get("GBP")
        }
    }

    # 3. Physically save the raw file to our Data Lakehouse folder
    print(f"💾 Saving raw API file directly to: {output_file_path}")
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(filtered_rates, f, indent=4)
        
    print("🏁 Success! Live API currency layers are safely landed in the Lakehouse.")

except requests.exceptions.RequestException as e:
    print(f"❌ API Pull Failed! Network or Connection Error: {e}")