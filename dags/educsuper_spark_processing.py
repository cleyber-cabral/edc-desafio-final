from airflow import DAG

from airflow.providers.cncf.kubernetes.operators.spark_kubernetes import SparkKubernetesOperator
from airflow.providers.cncf.kubernetes.sensors.spark_kubernetes import SparkKubernetesSensor
from airflow.operators.python_operator import PythonOperator
from airflow.models import Variable

from airflow.utils.dates import days_ago

from google.cloud import storage


client = storage.Client(project = 'edc-desafio-final')
bucket = client.get_bucket('desafio-igti')

with DAG(
    'educ_sup_spark_k8s',
    default_args={
        'owner': 'Cleyber',
        'depends_on_past': False,
        'max_active_runs': 1,
    },
    description='submit spark-pi as sparkApplication on kubernetes',
    schedule_interval="0 */2 * * *",
    start_date=days_ago(1),
    catchup=False,
    tags=['spark', 'kubernetes', 'batch', 'educação', 'superior'],
) as dag:
    converte_parquet = SparkKubernetesOperator(
        task_id='converte_parquet',
        namespace="airflow",
        application_file="converte_parquet.yaml",
        kubernetes_conn_id="kubernetes_default",
        do_xcom_push=True,   
    )

    converte_parquet_monitor = SparkKubernetesSensor(
        task_id='converte_parquet_monitor',
        namespace="airflow",
        application_name="{{ task_instance.xcom_pull(task_ids='converte_parquet')['metadata']['name'] }}",
        kubernetes_conn_id="kubernetes_default",
    )

converte_parquet >> converte_parquet_monitor