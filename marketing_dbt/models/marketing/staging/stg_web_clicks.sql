SELECT
    click_id AS session_id,
    timestamp AS clicked_at,  -- Map raw timestamp to clicked_at
    {{ dbt_utils.generate_surrogate_key(['utm_source']) }} AS utm_source_key,
    utm_source,
    visitor_id AS user_id  -- Map raw visitor_id to user_id
FROM {{ source('marketing', 'raw_web_clicks') }}