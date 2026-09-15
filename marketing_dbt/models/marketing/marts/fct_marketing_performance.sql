SELECT
    ad_date,
    utm_source_key,
    utm_source,
    COALESCE(spend_usd, 0.0) AS spend,
    COALESCE(impressions, 0) AS impressions,
    COALESCE(clicks, 0) AS clicks,
    COALESCE(total_revenue, 0.0) AS total_revenue,
    COALESCE(total_orders, 0) AS total_orders
FROM {{ ref('int_marketing_channel_performance') }}