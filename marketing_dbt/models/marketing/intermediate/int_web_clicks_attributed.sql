WITH web_clicks AS (
    SELECT 
        clicked_at::date AS ad_date,
        utm_source_key,
        utm_source,
        user_id
    FROM {{ ref('stg_web_clicks') }}
),

transactions AS (
    SELECT 
        purchased_at::date AS ad_date,
        user_id,
        order_id,
        amount_usd
    FROM {{ ref('stg_transactions') }}
)

SELECT 
    wb.ad_date,
    wb.utm_source_key,
    wb.utm_source,
    SUM(st.amount_usd) AS total_revenue,
    COUNT(st.order_id) AS total_orders
FROM web_clicks wb
LEFT JOIN transactions st
    ON wb.user_id = st.user_id
    AND wb.ad_date = st.ad_date
GROUP BY wb.ad_date, wb.utm_source_key, wb.utm_source