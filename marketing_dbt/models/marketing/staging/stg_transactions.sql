SELECT
    transaction_id AS order_id,
    visitor_id AS user_id,
    timestamp AS purchased_at,
    amount AS amount_usd
FROM {{ source('marketing', 'raw_transactions') }}