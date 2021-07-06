# import io
# import time
# from datetime import datetime, timedelta
# from time import sleep

# import pandas as pd
# import requests
# from airflow import DAG
# from airflow.operators.bash_operator import BashOperator

# # Default parameters
# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "start_date": datetime(2020, 9, 1),
#     "retries": 1,
#     "retry_delay": timedelta(minutes=2),
# }


# # At 6am every day
# schedule = "0 6 * * *"


# # Declare dag
# dag = DAG("sample", default_args=default_args, schedule_interval=schedule)


# # Instantiate sample bash operator
# t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)
# t2 = BashOperator(task_id="sleep", bash_command="sleep 1", dag=dag)


# # Set dependencies
# t1 >> t2
