from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.utils.email import send_email
from airflow.exceptions import AirflowException
import os

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 9, 13),
    'schedule_interval': "@daily",
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'daily_script_execution',
    default_args=default_args,
    description='DAG para ejecutar el script diariamente',
)

def main():
    from main import main
    return main()

def send_status_email(**context):
    task_instance = context['task_instance']
    task_status = task_instance.current_state()

    subject = f"Airflow Task {task_instance.task_id} {task_status}"
    body = f"The task {task_instance.task_id} finished with status: {task_status}.\n\n" \
           f"Task execution date: {context['execution_date']}\n" \
           f"Log URL: {task_instance.log_url}\n\n"

    to_email = os.getenv('ALERT_EMAIL')

    try:
        send_email(to=to_email, subject=subject, html_content=body)
    except Exception as e:
        raise AirflowException(f"Fallo al enviar el correo electrónico: {str(e)}")

run_script = PythonOperator(
    task_id='run_daily_script',
    python_callable=main,
    dag=dag,
)

send_email_task = PythonOperator(
    task_id='send_email_task',
    python_callable=send_status_email,
    provide_context=True,
    trigger_rule='all_done',
    dag=dag
)

send_email_task.set_upstream(run_script)