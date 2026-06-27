SELECT 
    order_id,
    user_id,
    purchase_timestamp AS purchased_at,
    order_amount AS amount_usd
FROM {{ source('marketing', 'raw_transactions') }}