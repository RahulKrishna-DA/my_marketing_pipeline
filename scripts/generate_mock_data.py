import os
import csv
import random
from datetime import datetime, timedelta

# Create the data lakehouse directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data_lakehouse'))
os.makedirs(OUTPUT_DIR, exist_ok=True)

START_DATE = datetime(2026, 1, 1)
CHANNELS = ['Google_Ads', 'Facebook_Ads', 'LinkedIn_Ads', 'Email_Marketing']

print("🌱 Generating consistent mock marketing data...")

# 1. Generate Raw Ad Spend
with open(os.path.join(OUTPUT_DIR, 'raw_ad_spend.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['campaign_id', 'ad_date', 'channel', 'daily_spend', 'impressions', 'clicks'])
    for i in range(1, 6):  # 5 campaigns
        for days in range(30): # 30 days of data
            current_date = (START_DATE + timedelta(days=days)).strftime('%Y-%m-%d')
            spend = round(random.uniform(50.0, 500.0), 2)
            impr = random.randint(1000, 15000)
            clicks = random.randint(50, int(impr * 0.1))
            writer.writerow([f"CAMP_{i:03d}", current_date, random.choice(CHANNELS), spend, impr, clicks])

# 2. Generate Raw Web Clicks
with open(os.path.join(OUTPUT_DIR, 'raw_web_clicks.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['click_id', 'timestamp', 'campaign_id', 'visitor_id', 'converted'])
    for i in range(1, 1001): # 1000 click events
        click_date = START_DATE + timedelta(days=random.randint(0, 29), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        writer.writerow([
            f"CLK_{i:06d}", 
            click_date.strftime('%Y-%m-%d %H:%M:%S'),
            f"CAMP_{random.randint(1, 5):03d}",
            f"VISITOR_{random.randint(100, 500)}",
            random.choice([True, False, False, False]) # 25% conversion rate approximation
        ])

# 3. Generate Raw Transactions
with open(os.path.join(OUTPUT_DIR, 'raw_transactions.csv'), 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['transaction_id', 'timestamp', 'visitor_id', 'amount', 'currency'])
    for i in range(1, 151): # 150 transactions
        tx_date = START_DATE + timedelta(days=random.randint(0, 29), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        writer.writerow([
            f"TXN_{i:05d}",
            tx_date.strftime('%Y-%m-%d %H:%M:%S'),
            f"VISITOR_{random.randint(100, 500)}",
            round(random.uniform(10.0, 250.0), 2),
            random.choice(['USD', 'EUR', 'GBP']) # Mix of currencies to join against our new API rates!
        ])

print("✅ Data generation complete! Check your 'data_lakehouse' folder.")