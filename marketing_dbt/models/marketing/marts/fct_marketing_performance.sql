SELECT
    ad_date,
    utm_source_key,
    utm_source,
    spend_usd AS spend,  -- Map spend_usd here so the mart matches your column expectations
    impressions,
    clicks,
    total_revenue,
    total_orders
FROM {{ ref('int_marketing_channel_performance') }}