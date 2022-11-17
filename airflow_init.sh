#!/bin/bash

export AIRFLOW_HOME="$(pwd)/airflow"

airflow db init &
airflow users create \
           --username admin \
           --firstname Admin \
           --lastname Istrator \
           --role Admin \
           --email admin@hotmail.com