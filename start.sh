#!/bin/bash
airflow standalone

airflow db migrate

airflow users create \
    --username admin \
    --firstname jesica \
    --lastname conserva \
    --role Admin \
    --email jess.conserva@gmail.com 

airflow webserver --port 8080

airflow scheduler