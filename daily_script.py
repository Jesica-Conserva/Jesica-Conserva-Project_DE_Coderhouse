from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 1),  # Ajusta esta fecha según sea necesario
    'schedule' : "@daily",
    'end_date' : None,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_script_execution',
    default_args=default_args,
    description='DAG para ejecutar el script diariamente',
    schedule_interval=timedelta(days=1),
)

def main():
    from main import main
    return main()

run_script = PythonOperator(
    task_id='run_daily_script',
    python_callable=main,
    dag=dag,
)
