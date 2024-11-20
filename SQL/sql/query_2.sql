SELECT 
    t.client_id,
    SUM(CASE WHEN p.product_type = 'MEUBLE' THEN t.prod_price * t.prod_qty ELSE 0 END) AS ventes_meuble,
    SUM(CASE WHEN p.product_type = 'DECO' THEN t.prod_price * t.prod_qty ELSE 0 END) AS ventes_deco
FROM
    transaction_table t
LEFT JOIN product_table p
    ON t.prod_id = p.product_id
WHERE 
    STR_TO_DATE(date, '%d/%m/%y') BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY client_id