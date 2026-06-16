# Architecture Overview

## Flow
1. Source CSV simulates operational sales and campaign systems.
2. Python ETL validates and enriches records.
3. Sensitive email data is masked before analytics consumption.
4. Curated data is loaded into Snowflake raw/dimension/fact layers.
5. KPI-ready tables support dashboards and reporting.

## Components
- Ingestion: Python
- Orchestration: Airflow
- Warehouse: Snowflake
- Version Control: GitHub
- Reporting Layer: BI tool / dashboard consumer

## Privacy
- PII field identified: email
- Masking applied before broad analytical usage
- Supports GDPR/privacy-aware design concepts
