import os
import csv
import random
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'data_lakehouse'))
os.makedirs(OUTPUT_DIR, exist_ok=True)

START_DATE = datetime.utcnow() - timedelta(days=30)
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

print("✅ Data generation complete and aligned!")