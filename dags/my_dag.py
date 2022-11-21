from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from scraper.utils.url_scraper import Scraper

args = {
    'owner': 'admin',
    'start_date': days_ago(1) # make start date in the past
}

#defining the dag object
dag = DAG(
    dag_id='scrape-train-properties',
    default_args=args,
    schedule_interval='@daily' #to make this workflow happen every day
)

#assigning the task for our dag to do
with dag:
    scrape_urls = PythonOperator(
        task_id='scrape_urls',
        python_callable=Scraper.write_property_urls,
        # provide_context=True
    )