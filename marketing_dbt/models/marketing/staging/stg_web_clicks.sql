SELECT 
    session_id,
    user_id, 
    click_timestamp AS clicked_at,
    {{ dbt_utils.generate_surrogate_key(["TRIM(LOWER(utm_source))"]) }} AS utm_source_key,
    TRIM(LOWER(utm_source)) AS utm_source,
    LOWER(TRIM(utm_medium)) AS utm_medium,
    LOWER(TRIM(page_url)) AS page_url
FROM {{ source('marketing', 'raw_web_clicks') }}