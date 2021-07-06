# import io
# from datetime import datetime, time, timedelta
# from time import sleep

# import pandas as pd
# import requests
# from airflow import DAG
# from airflow.operators.bash_operator import BashOperator
# from airflow.operators.python_operator import PythonOperator


# def _get_current_epoch():
#     current = datetime.combine(datetime.today(), time.min)
#     return int(current.timestamp())


# def _get_previous_epoch_days(days):
#     current_datetime = datetime.combine(datetime.today(), time.min)
#     prev_datetime = current_datetime - timedelta(days=days)
#     return int(prev_datetime.timestamp())


# def stock_retrieve(stock, period1=None, period2=None, interval="1d", events="history", **kwargs):
#     period1 = _get_previous_epoch_days(7) if not period1 else period1
#     period2 = _get_current_epoch() if not period2 else period2

#     print(
#         f"[DataRetriever] Getting data for: stock {stock}, {period1} to {period2}, interval: {interval}, events: {events}..."
#     )

#     stock = stock.strip()
#     url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={period1}&period2={period2}&interval={interval}&events={events}"
#     response = requests.get(url)

#     if not response.ok:
#         # Retry one time due to page not found
#         print("[DataRetriever] Failure occurred, waiting 10 seconds then retrying once...")
#         sleep(10)

#         response = requests.get(url)
#         if not response.ok:
#             raise Exception(f"[DataRetriever] Yahoo request error. Response: {response.text}")

#     data = response.content.decode("utf8")
#     df_history = pd.read_csv(io.StringIO(data))
#     print(df_history)


# # Default parameters
# default_args = {
#     "owner": "airflow",
#     "depends_on_past": False,
#     "start_date": datetime(2021, 7, 5),
#     "retries": 1,
#     "retry_delay": timedelta(minutes=2),
# }


# # Declare dag, tasks and dependencies
# schedule = "0 6 * * *"
# dag = DAG("stock_retrieve", default_args=default_args, schedule_interval=schedule)
# t1 = BashOperator(task_id="print_date", bash_command="date", dag=dag)
# t2 = BashOperator(task_id="sleep", bash_command="sleep 1", dag=dag)
# t3 = PythonOperator(
#     task_id="stock_retrieve", python_callable=stock_retrieve, op_kwargs={"stock": "GOOGL"}, dag=dag
# )
# t1 >> t2 >> t3
