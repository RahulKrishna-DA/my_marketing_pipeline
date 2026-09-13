SELECT 
    click_id,
    timestamp AS clicked_at,
    {{ dbt_utils.generate_surrogate_key(['campaign_id']) }} AS utm_source_key,
    campaign_id AS utm_source,
    visitor_id AS user_id,
    converted
FROM {{ source('marketing', 'raw_web_clicks') }}