from good_dags.dag_factory import add_bash_task, create_dag

schedule = "0 6 * * *"
dag = create_dag(name="sample", schedule=schedule)
bash_1 = add_bash_task(name="print_date", command="date", dag=dag)
bash_2 = add_bash_task(name="sleep", command="sleep 1", dag=dag)

bash_1 >> bash_2
