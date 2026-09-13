SELECT 
    campaign_id,
    ad_date AS date_day,
    {{ dbt_utils.generate_surrogate_key(['campaign_id']) }} AS utm_source_key,
    channel AS utm_source,
    daily_spend AS spend_usd,
    impressions,
    clicks
FROM {{ source('marketing', 'raw_ad_spend') }}