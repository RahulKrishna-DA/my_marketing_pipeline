WITH revenue_side AS (
    SELECT * FROM {{ ref('int_web_clicks_attributed') }}
),

spend_side AS (
    SELECT * FROM {{ ref('int_ad_spend_summary') }}
)

SELECT 
    r.utm_source_key,
    r.utm_source,
    r.total_revenue as revenue,
    r.total_orders,
    s.total_campaigns,
    s.total_spend as spend,
    (r.total_revenue / NULLIF(s.total_spend, 0)) AS roas
FROM revenue_side r
LEFT JOIN spend_side s 
    ON r.utm_source_key = s.utm_source_key