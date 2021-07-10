from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

DEFAULT_TRIGGER_RULE = "none_failed"
DEFAULT_RETRIES = 2


def create_dag(name, schedule, args=None):
    default_args = {
        "owner": "airflow",
        "catchup": False,
        "depends_on_past": False,
        "start_date": datetime(year=2021, month=7, day=1),
        "concurrency": 1,
        "retries": 1,
        "retry_delay": timedelta(minutes=2),
        "max_active_runs": 1,
    }
    args = args if args else default_args

    return DAG(dag_id=name, default_args=args, schedule_interval=schedule)


def add_python_task(
    dag, name, function, kwargs=None,
        trigger_rule=DEFAULT_TRIGGER_RULE, retries=DEFAULT_RETRIES):

    return PythonOperator(
        task_id=name,
        python_callable=function,
        op_args=kwargs,
        trigger_rule=trigger_rule,
        retries=retries,
        dag=dag
    )


def add_bash_task(
    dag, name, command,
        trigger_rule=DEFAULT_TRIGGER_RULE, retries=DEFAULT_RETRIES):

    return BashOperator(
        task_id=name,
        bash_command=command,
        trigger_rule=trigger_rule,
        retries=retries,
        dag=dag
    )


