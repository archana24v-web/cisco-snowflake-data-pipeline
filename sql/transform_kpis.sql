INSERT INTO fact_sales_kpi
SELECT
    customer_id,
    campaign_id,
    spend,
    revenue,
    converted,
    event_date,
    ROUND((revenue - spend) / NULLIF(spend, 0), 2) AS roi,
    CASE WHEN converted = 1 THEN 1 ELSE 0 END AS conversion_flag
FROM raw_sales_campaign;
