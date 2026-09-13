SELECT
    click_id AS session_id,      -- Maps the python script's column
    click_timestamp AS clicked_at,
    {{ dbt_utils.generate_surrogate_key(['utm_source']) }} AS utm_source_key,
    utm_source,
    user_id
FROM {{ source('marketing', 'raw_web_clicks') }}