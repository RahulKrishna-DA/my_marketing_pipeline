WITH web_clicks AS (
    SELECT * FROM {{ ref('stg_web_clicks') }}
),

transactions AS (
    SELECT * FROM {{ ref('stg_transactions') }}
)

SELECT 
    wb.utm_source_key,
    wb.utm_source,
    SUM(st.amount_usd) AS total_revenue,
    COUNT(st.order_id) AS total_orders
FROM web_clicks wb 
LEFT JOIN transactions st 
    ON wb.user_id = st.user_id
GROUP BY wb.utm_source_key, wb.utm_source