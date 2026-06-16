# Cisco Snowflake Data Pipeline Project

An end-to-end data engineering portfolio project tailored to Cisco's job requirements.

## Project Overview
This project simulates a modern sales analytics platform that:
- Ingests raw campaign and sales data using Python
- Loads curated data into Snowflake-style warehouse layers
- Orchestrates ETL pipelines with Airflow
- Applies dimensional data modeling for analytics
- Tracks KPI metrics through dashboard-ready tables
- Incorporates privacy-aware handling for PII/GDPR-sensitive fields
- Uses Git-based version control and cloud-native deployment patterns

## Tech Stack
- Python
- SQL
- Snowflake
- Apache Airflow
- Docker
- GitHub Actions
- Pandas
- dbt-style SQL modeling concepts

## Repository Structure
- `data/` sample raw datasets
- `sql/` warehouse schema and transformation SQL
- `src/` Python ETL pipeline
- `airflow/` DAG definitions
- `docs/` architecture, data dictionary, and privacy notes

## Business Use Case
A Cisco sales analytics team needs reliable campaign/program KPI reporting across multiple regions. This project builds a pipeline that ingests raw sales and campaign data, transforms it into analytics-ready warehouse tables, and enables downstream dashboards for operational visibility.

## KPIs
- Campaign ROI
- Pipeline conversion rate
- Revenue by region
- Program engagement trend
- Sales rep performance summary

## Resume Value
This project demonstrates:
- Python-based data pipeline development
- Snowflake-oriented warehouse design
- Data modeling and ETL best practices
- Reporting and KPI data preparation
- Privacy-conscious engineering design

## Next Improvements
- Add Kubernetes deployment manifests
- Add Gradle-based job packaging
- Add BI dashboard screenshots
- Connect to live Snowflake account
