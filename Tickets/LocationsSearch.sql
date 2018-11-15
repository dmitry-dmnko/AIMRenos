SELECT
bc_status
,mail_code
, *
FROM locations
WHERE state = 'NY'
AND city = 'New York'
ORDER BY address
