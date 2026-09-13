SELECT
    click_id AS session_id,
    click_timestamp AS clicked_at,
    campaign_id,
    {{ dbt_utils.generate_surrogate_key(['campaign_id']) }} AS utm_source_key,
    campaign_id AS utm_source,
    visitor_id AS user_id,
    converted
FROM {{ source('marketing', 'raw_web_clicks') }}