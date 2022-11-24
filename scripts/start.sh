#!/bin/bash

# Build Docker images
docker build -f dags/scraper/Dockerfile -t airflow_scraper:latest ./dags/scraper;
docker build -f dags/scraper/Dockerfile -t airflow_train:latest ./dags/scraper_train_model;
docker build -f dags/scraper/Dockerfile -t airflow_dashboard:latest ./dags/Dashboard;

# Init Airflow
docker-compose up airflow-init;
# Run Airflow
docker-compose up;