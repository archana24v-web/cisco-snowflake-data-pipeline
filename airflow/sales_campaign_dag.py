from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR / 'src'))

from etl_pipeline import run_pipeline

with DAG(
    dag_id='sales_campaign_etl',
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False,
    tags=['snowflake', 'sales', 'etl']
) as dag:

    run_etl = PythonOperator(
        task_id='run_sales_campaign_pipeline',
        python_callable=run_pipeline
    )

    run_etl
