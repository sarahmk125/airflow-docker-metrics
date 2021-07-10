from good_dags.dag_factory import add_bash_task, add_python_task, create_dag
from good_dags.stock_retrieve.lib.stock_history import StockHistory

schedule = "0 6 * * *"
dag = create_dag(name="stock_retrieve", schedule=schedule)
bash_1 = add_bash_task(name="print_date", command="date", dag=dag)
bash_2 = add_bash_task(name="sleep", command="sleep 1", dag=dag)
python_3 = add_python_task(
    name="stock_retrieve_task",
    function=StockHistory().stock_retrieve,
    kwargs={"stock": "GOOGL"},
    dag=dag
)

bash_1 >> bash_2 >> python_3


