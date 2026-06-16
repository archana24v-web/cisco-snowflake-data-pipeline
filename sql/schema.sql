CREATE OR REPLACE TABLE raw_sales_campaign (
    customer_id NUMBER,
    customer_name STRING,
    email STRING,
    region STRING,
    campaign_id STRING,
    spend NUMBER,
    revenue NUMBER,
    converted NUMBER,
    event_date DATE
);

CREATE OR REPLACE TABLE dim_customer (
    customer_key NUMBER AUTOINCREMENT,
    customer_id NUMBER,
    customer_name STRING,
    email_masked STRING,
    region STRING
);

CREATE OR REPLACE TABLE dim_campaign (
    campaign_key NUMBER AUTOINCREMENT,
    campaign_id STRING,
    campaign_type STRING
);

CREATE OR REPLACE TABLE fact_sales_kpi (
    customer_id NUMBER,
    campaign_id STRING,
    spend NUMBER,
    revenue NUMBER,
    converted NUMBER,
    event_date DATE,
    roi NUMBER,
    conversion_flag NUMBER
);
