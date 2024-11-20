SELECT 
    STR_TO_DATE(date, '%d/%m/%y') AS transaction_date,
    SUM(prod_price * prod_qty) AS total_amount
FROM transaction_table
WHERE STR_TO_DATE(date, '%d/%m/%y') BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY transaction_date
ORDER BY transaction_date;