SELECT
    ad_date,
    utm_source_key,
    utm_source,
    spend_usd AS spend,  -- Map spend_usd here so the mart matches your column expectations
    impressions,
    clicks,
    COALESCE(total_revenue, 0.0) AS total_revenue,
    COALESCE(total_orders, 0) AS total_orders
FROM {{ ref('int_marketing_channel_performance') }}