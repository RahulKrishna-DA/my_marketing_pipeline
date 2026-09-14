import os
import csv
import json
import random
from datetime import datetime, timedelta
from email.utils import parsedate_to_datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data_lakehouse'))
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 1. Synchronize date with the API extraction timestamp if available
exchange_rate_path = os.path.join(OUTPUT_DIR, 'raw_exchange_rates.json')
anchor_date = datetime.utcnow()

if os.path.exists(exchange_rate_path):
    try:
        with open(exchange_rate_path, 'r', encoding='utf-8') as f:
            er_data = json.load(f)
            extracted_str = er_data.get("extracted_at")
            if extracted_str:
                # Safely parse strings like 'Mon, 14 Sep 2026...' into a clean datetime object
                parsed_dt = parsedate_to_datetime(extracted_str)
                anchor_date = parsed_dt.replace(tzinfo=None)
                print(f"🔗 Synchronized Faker window using API anchor date: {anchor_date.strftime('%Y-%m-%d')}")
    except Exception as e:
        print(f"⚠️ Could not parse exchange rate timestamp, defaulting to UTC: {e}")

END_DATE = anchor_date
START_DATE = END_DATE - timedelta(days=30)
CHANNELS = ['google_ads', 'facebook_ads', 'linkedin_ads', 'email_marketing']

print("🌱 Generating synchronized mock marketing data...")

# 1. Ad Spend
with open(os.path.join(OUTPUT_DIR, 'raw_ad_spend.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['campaign_id', 'ad_date', 'channel', 'daily_spend', 'impressions', 'clicks'])
    for i in range(1, 6):
        for days in range(30):
            current_date = (START_DATE + timedelta(days=days)).strftime('%Y-%m-%d')
            writer.writerow([
                f"CAMP_{i:03d}", 
                current_date, 
                random.choice(CHANNELS), 
                round(random.uniform(50.0, 500.0), 2), 
                random.randint(1000, 15000), 
                random.randint(50, 1500)
            ])

# 2. Web Clicks (Using campaign_id as the bridge)
with open(os.path.join(OUTPUT_DIR, 'raw_web_clicks.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['click_id', 'timestamp', 'campaign_id', 'visitor_id', 'converted'])
    for i in range(1, 1001):
        click_date = START_DATE + timedelta(days=random.randint(0, 29), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        writer.writerow([
            f"CLK_{i:06d}", 
            click_date.strftime('%Y-%m-%d %H:%M:%S'),
            f"CAMP_{random.randint(1, 5):03d}",
            f"VISITOR_{random.randint(100, 500)}",
            random.choice([True, False, False, False])
        ])

# 3. Transactions
with open(os.path.join(OUTPUT_DIR, 'raw_transactions.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['transaction_id', 'timestamp', 'visitor_id', 'amount', 'currency'])
    for i in range(1, 151):
        tx_date = START_DATE + timedelta(days=random.randint(0, 29), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        writer.writerow([
            f"TXN_{i:05d}",
            tx_date.strftime('%Y-%m-%d %H:%M:%S'),
            f"VISITOR_{random.randint(100, 500)}",
            round(random.uniform(10.0, 250.0), 2),
            random.choice(['USD', 'EUR', 'GBP'])
        ])

print("✅ Data generation complete and aligned with API timestamps!")