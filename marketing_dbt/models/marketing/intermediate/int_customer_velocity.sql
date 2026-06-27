WITH first_clicks AS (
    SELECT 
        user_id, 
        MIN(clicked_at) AS first_click_at
    FROM {{ ref('stg_web_clicks') }}
    GROUP BY user_id
),

first_purchases AS (
    SELECT 
        user_id, 
        MIN(purchased_at) AS first_purchase_at
    FROM {{ ref('stg_transactions') }}
    GROUP BY user_id
)

SELECT 
    c.user_id,
    c.first_click_at,
    p.first_purchase_at,
    DATE_DIFF('second', c.first_click_at, p.first_purchase_at) / 86400.0 AS days_to_conversion
FROM first_clicks c
INNER JOIN first_purchases p 
    ON c.user_id = p.user_id
WHERE p.first_purchase_at >= c.first_click_at