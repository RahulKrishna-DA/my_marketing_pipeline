SELECT
    transaction_id AS order_id,  -- Maps the python script's column
    user_id,
    purchase_timestamp AS purchased_at,
    order_amount AS amount_usd
FROM {{ source('marketing', 'raw_transactions') }}