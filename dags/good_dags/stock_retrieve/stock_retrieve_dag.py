from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from good_dags.stock_retrieve.lib.stock_history import StockHistory

# Default parameters
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 7, 5),
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}


# Declare dag, tasks and dependencies
schedule = "0 6 * * *"
dag = DAG("stock_retrieve", default_args=default_args, schedule_interval=schedule)
t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)
t2 = BashOperator(task_id="sleep", bash_command="sleep 1", dag=dag)
t3 = PythonOperator(
    task_id="stock_retrieve",
    python_callable=StockHistory().stock_retrieve,
    op_kwargs={"stock": "GOOGL"},
    dag=dag,
)
t1 >> t2 >> t3
