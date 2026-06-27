import os
import duckdb

print("🔌 Initializing High-Performance Ingestion Engine...")

# Define paths for our lakehouse source and target dbt database
LAKEHOUSE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data_lakehouse'))
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'marketing_dbt', 'dev.duckdb'))

print(f"📦 Connecting straight to target database at: {DB_PATH}")
# Connect directly to the DuckDB file (it will create it if it doesn't exist)
conn = duckdb.connect(DB_PATH)

print("⚡ Streaming tables from Data Lakehouse into DuckDB...")

# 1. Ingest raw_ad_spend
ad_spend_path = os.path.join(LAKEHOUSE_DIR, 'raw_ad_spend.csv')
conn.execute(f"CREATE OR REPLACE TABLE raw_ad_spend AS SELECT * FROM read_csv_auto('{ad_spend_path.replace('\\', '/')}');")
print("✅ Loaded raw_ad_spend into DuckDB!")

# 2. Ingest raw_web_clicks
web_clicks_path = os.path.join(LAKEHOUSE_DIR, 'raw_web_clicks.csv')
conn.execute(f"CREATE OR REPLACE TABLE raw_web_clicks AS SELECT * FROM read_csv_auto('{web_clicks_path.replace('\\', '/')}');")
print("✅ Loaded raw_web_clicks into DuckDB!")

# 3. Ingest raw_transactions
transactions_path = os.path.join(LAKEHOUSE_DIR, 'raw_transactions.csv')
conn.execute(f"CREATE OR REPLACE TABLE raw_transactions AS SELECT * FROM read_csv_auto('{transactions_path.replace('\\', '/')}');")
print("✅ Loaded raw_transactions into DuckDB!")

# Close the connection safely
conn.close()

print("\n🏁 Success! All raw tables are now safely stored inside DuckDB and ready for dbt.")