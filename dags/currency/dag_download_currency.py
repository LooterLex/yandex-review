import sys
import os
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from airflow import DAG
from airflow.operators.python import PythonOperator

from currency.download_currency import download


with DAG(
    'download_currency',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 0,
        'retry_delay': timedelta(minutes=5),
    },
    description='Download currency',
    schedule_interval="0 */3 * * *",
    start_date=datetime(2022, 5, 4),
) as dag:
    download = PythonOperator(
        task_id='download',
        python_callable=download,
    )

