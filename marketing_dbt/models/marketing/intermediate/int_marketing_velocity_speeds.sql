SELECT 
    clicks.utm_source_key,
    clicks.utm_source,
    AVG(velocity.days_to_conversion) AS avg_days_to_conversion
FROM {{ ref('int_customer_velocity') }} AS velocity
INNER JOIN {{ ref('stg_web_clicks') }} AS clicks
    ON velocity.user_id = clicks.user_id
GROUP BY 
    clicks.utm_source_key,
    clicks.utm_source