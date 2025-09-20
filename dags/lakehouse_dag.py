from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'tercio',
    'depends_on_past': False,
    'start_date': datetime(2024, 9, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'lakehouse_pipeline',
    default_args=default_args,
    description='Pipeline completo do Lakehouse',
    schedule_interval=timedelta(days=1),
)

# Tasks
generate_data = BashOperator(
    task_id='gerar_dados',
    bash_command='cd /home/jovyan/scripts && python data_generator.py',
    dag=dag,
)

bronze_to_silver = BashOperator(
    task_id='bronze_para_silver',
    bash_command='cd /home/jovyan/work && python -m nbconvert --execute 01_bronze_to_silver.ipynb',
    dag=dag,
)

silver_to_gold = BashOperator(
    task_id='silver_para_gold',
    bash_command='cd /home/jovyan/work && python -m nbconvert --execute 02_silver_to_gold.ipynb',
    dag=dag,
)

# Ordem de execução
generate_data >> bronze_to_silver >> silver_to_gold
