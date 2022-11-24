#!/bin/bash

# Build Docker images
docker build -f dags/scraper/Dockerfile -t airflow_scraper:latest ./dags/scraper;

# Init Airflow
docker-compose up airflow-init;
# Run Airflow
docker-compose up;