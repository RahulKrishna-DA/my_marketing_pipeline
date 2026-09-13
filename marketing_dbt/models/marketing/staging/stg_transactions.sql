SELECT
    order_id,
    user_id,                  -- <-- Make sure user_id is right here
    purchase_timestamp AS purchased_at,
    order_amount AS amount_usd
FROM {{ source('marketing', 'raw_transactions') }}