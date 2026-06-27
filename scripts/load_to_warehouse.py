import os
import csv
import json
import duckdb

print("🏗️ Initializing Explicit Python Warehouse Load...")

# Define folder paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LAKEHOUSE_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data_lakehouse'))
DB_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'marketing_dbt', 'dev.duckdb'))

# 1. Establish a real connection to our DuckDB Warehouse file
print(f"🔌 Connecting to Data Warehouse at: {DB_PATH}")
conn = duckdb.connect(DB_PATH)

# --- PHASE 1: LOAD THE JSON API EXCHANGE RATES ---
print("📥 Reading raw JSON exchange rates from Lakehouse...")
json_file_path = os.path.join(LAKEHOUSE_DIR, 'raw_exchange_rates.json')

with open(json_file_path, 'r', encoding='utf-8') as f:
    exchange_data = json.load(f)

base_currency = exchange_data['base_currency']
extracted_at = exchange_data['extracted_at']

# Drop old table if exists and create a fresh one for our JSON data
conn.execute("DROP TABLE IF EXISTS raw_exchange_rates;")
conn.execute("""
    CREATE TABLE raw_exchange_rates (
        base_currency VARCHAR,
        target_currency VARCHAR,
        exchange_rate DOUBLE,
        extracted_at VARCHAR
    );
""")

# Loop through the JSON dictionary and execute standard database INSERT statements
print("✏️ Writing JSON data into 'raw_exchange_rates' table row-by-row...")
for currency, rate in exchange_data['rates'].items():
    conn.execute("""
        INSERT INTO raw_exchange_rates VALUES (?, ?, ?, ?);
    """, (base_currency, currency, rate, extracted_at))


# --- PHASE 2: LOAD THE CSV FILES MANUALLY ---
csv_files = ['raw_ad_spend', 'raw_web_clicks', 'raw_transactions']

for file_name in csv_files:
    csv_file_path = os.path.join(LAKEHOUSE_DIR, f"{file_name}.csv")
    print(f"📥 Processing flat file: {file_name}.csv")
    
    # We use DuckDB's explicit read command to cleanly map the CSV directly to a table
    conn.execute(f"DROP TABLE IF EXISTS {file_name};")
    conn.execute(f"""
        CREATE TABLE {file_name} AS 
        SELECT * FROM read_csv_auto('{csv_file_path}');
    """)

# Close the database connection safely
conn.close()
print("🏁 Success! All CSV and JSON datasets are explicitly committed to DuckDB.")