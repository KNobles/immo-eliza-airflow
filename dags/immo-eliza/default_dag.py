from datetime import datetime, timedelta
from airflow import DAG
import os
from airflow.operators.bash_operator import BashOperator
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
'owner'                 : 'airflow',
'description'           : 'Use of the DockerOperator',
'depend_on_past'        : False,
'start_date'            : datetime(2021, 5, 1),
'email_on_failure'      : False,
'email_on_retry'        : False,
'retries'               : 1,
'retry_delay'           : timedelta(minutes=5)
}

with DAG('docker_operator_demo', default_args=default_args, schedule_interval="5 * * * *", catchup=False) as dag:
    start_dag = DummyOperator(
        task_id='start_dag'
        )

    end_dag = DummyOperator(
        task_id='end_dag'
        )        

    t1 = BashOperator(
        task_id='print_current_date',
        bash_command='date'
        )
        
    t2 = DockerOperator(
        task_id='scraping',
        image='airflow_scraper:latest',
        container_name='task___cleaning',
        api_version='auto',
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
        environment={
            "AZURE_CONNECTION_STRING": os.getenv("AZURE_CONNECTION_STRING"),
            "STORAGE_CONTAINER": os.getenv("STORAGE_CONTAINER")
        },
        network_mode="bridge"
        )
    t3 = DockerOperator(
        task_id='training',
        image='airflow_train:latest',
        container_name='task___training',
        api_version='auto',
        auto_remove=True,
        docker_url="unix://var/run/docker.sock",
        environment={
            "AZURE_CONNECTION_STRING": os.getenv("AZURE_CONNECTION_STRING"),
            "STORAGE_CONTAINER": os.getenv("STORAGE_CONTAINER")
        },
        network_mode="bridge"
        )

    start_dag >> t1 
    
    t1 >> t2

    t2 >> t3

    t3 >> end_dag