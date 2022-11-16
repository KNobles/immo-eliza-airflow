from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from operators.test import hello_world

args = {
    'owner': 'admin',
    'start_date': days_ago(1) # make start date in the past
}

#defining the dag object
dag = DAG(
    dag_id='crm-elastic-dag',
    default_args=args,
    schedule_interval='@daily' #to make this workflow happen every day
)

#assigning the task for our dag to do
with dag:
    hello_world = PythonOperator(
        task_id='test_dag_kev',
        python_callable=hello_world,
        # provide_context=True
    )
