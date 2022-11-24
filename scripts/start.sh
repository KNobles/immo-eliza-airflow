#!/bin/bash

# Build Docker images
docker build -f dags/immo-eliza/scraper/Dockerfile -t airflow_scraper:latest ./dags/immo-eliza/scraper;
docker build -f dags/immo-eliza/scraper/Dockerfile -t airflow_train:latest ./dags/immo-eliza/scraper_train_model;
docker build -f dags/immo-eliza/scraper/Dockerfile -t airflow_dashboard:latest ./dags/immo-eliza/Dashboard;

# Init Airflow
docker-compose up airflow-init;
# Run Airflow
docker-compose --env-file .env up;