SELECT 
    campaign_id,
    ad_date AS date_day,
    -- Strip 'ads' and 'paid' directly using simple replace combos
    {{ dbt_utils.generate_surrogate_key(["TRIM(REPLACE(REPLACE(LOWER(channel), 'ads', ''), 'paid', ''))"]) }} AS utm_source_key,
    TRIM(REPLACE(REPLACE(LOWER(channel), 'ads', ''), 'paid', '')) AS utm_source,
    daily_spend AS spend_usd,
    impressions,
    clicks
FROM {{ source('marketing', 'raw_ad_spend') }}