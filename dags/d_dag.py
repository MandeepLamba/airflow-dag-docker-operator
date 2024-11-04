from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.decorators import dag, task
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'mndp'
}

@dag(dag_id='run_docker_image_dag', default_args=default_args, schedule_interval=None)
def run_docker_image_dag():

    @task()
    def pre():
        print("Pre")

    tast2 = DockerOperator(
        task_id='run_docker_image',
        image='test:v1',
        command='python -m work.main',
        docker_url='unix://var/run/docker.sock',
        auto_remove="never", # ["never", "success", "force"]
        network_mode='bridge',
    )

    @task()
    def post():
        print("Post")

    pre() >> tast2 >> post()

run_docker_image_dag()
