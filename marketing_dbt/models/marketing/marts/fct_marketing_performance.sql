SELECT 
    -- 1. The Keys & Identifiers (For the database and BI tools)
    perf.utm_source_key,
    perf.utm_source,
    
    -- 2. Financial Power Metrics (The 'Money')
    perf.spend,
    perf.revenue,
    perf.roas,
    
    -- 3. Time Velocity Metrics (The 'Speed')
    speeds.avg_days_to_conversion

-- 4. Gather the primary financial records
FROM {{ ref('int_marketing_channel_performance') }} AS perf

-- 5. Staple the velocity records right next to them
LEFT JOIN {{ ref('int_marketing_velocity_speeds') }} AS speeds
    -- The bridge that aligns the rows perfectly:
    ON perf.utm_source_key = speeds.utm_source_key