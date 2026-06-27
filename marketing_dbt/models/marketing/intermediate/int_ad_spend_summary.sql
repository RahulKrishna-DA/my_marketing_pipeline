WITH ad_spend AS (
    SELECT * FROM {{ ref('stg_ad_spend') }}
)

SELECT 
    utm_source_key,
    utm_source,
    COUNT(campaign_id) AS total_campaigns,
    SUM(spend_usd) AS total_spend
FROM ad_spend
GROUP BY utm_source_key, utm_source