WITH ad_spend AS (
    SELECT 
        date_day AS ad_date,
        utm_source_key,
        utm_source,
        spend_usd,
        impressions,
        clicks
    FROM {{ ref('stg_ad_spend') }}
),

web_revenue AS (
    SELECT 
        ad_date,
        utm_source_key,
        utm_source,
        total_revenue,
        total_orders
    FROM {{ ref('int_web_clicks_attributed') }}
)

SELECT 
    COALESCE(r.ad_date, s.ad_date) AS ad_date,
    COALESCE(r.utm_source_key, s.utm_source_key) AS utm_source_key,
    COALESCE(r.utm_source, s.utm_source) AS utm_source,
    s.spend_usd,
    s.impressions,
    s.clicks,
    r.total_revenue,
    r.total_orders
FROM ad_spend s
FULL OUTER JOIN web_revenue r
    ON s.utm_source_key = r.utm_source_key
    AND s.ad_date = r.ad_date