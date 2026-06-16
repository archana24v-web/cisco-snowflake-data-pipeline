import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / 'data' / 'sales_campaign_data.csv'
OUTPUT_FILE = BASE_DIR / 'data' / 'sales_campaign_curated.csv'

def mask_email(email: str) -> str:
    if '@' not in email:
        return email
    name, domain = email.split('@', 1)
    return f"{name[:2]}***@{domain}"

def run_pipeline():
    df = pd.read_csv(INPUT_FILE)
    df['email_masked'] = df['email'].apply(mask_email)
    df['roi'] = ((df['revenue'] - df['spend']) / df['spend']).round(2)
    df['conversion_flag'] = df['converted'].apply(lambda x: 1 if x == 1 else 0)
    df.to_csv(OUTPUT_FILE, index=False)

if __name__ == '__main__':
    run_pipeline()
