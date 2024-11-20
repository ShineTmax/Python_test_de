import sqlite3
import pandas as pd
from io import StringIO

# Transaction Data sample
transaction_data = """
date,order_id,client_id,prod_id,prod_price,prod_qty
01/01/20,1234,999,490756,50,1
01/01/20,1234,999,389728,3.56,4
01/01/20,3456,845,490756,50,2
01/01/20,3456,845,549380,300,1
01/01/20,3456,845,293718,10,6
"""

# Product Data sample
product_data = """
product_id,product_type,product_name
490756,MEUBLE,Chaise
389728,DECO,Boule de Noël
549380,MEUBLE,Canapé
293718,DECO,Mug
"""

# Load transaction and product data into DataFrames
transaction_df = pd.read_csv(StringIO(transaction_data))
product_df = pd.read_csv(StringIO(product_data))

# Convert the date column to datetime
transaction_df['date'] = pd.to_datetime(transaction_df['date'], format='%d/%m/%y')

# Create SQLite database (in mempry)
conn = sqlite3.connect(":memory:")

# Load the DataFrames into the SQLite database
transaction_df.to_sql('transaction_table', conn, index=False, if_exists='replace')
product_df.to_sql('product_table', conn, index=False, if_exists='replace')

# SQL query to calculate sales by product type and client
query_test = """
SELECT 
    t.client_id,
    SUM(CASE WHEN p.product_type = 'MEUBLE' THEN t.prod_price * t.prod_qty ELSE 0 END) AS ventes_meuble,
    SUM(CASE WHEN p.product_type = 'DECO' THEN t.prod_price * t.prod_qty ELSE 0 END) AS ventes_deco
FROM
    transaction_table t
LEFT JOIN product_table p
ON t.prod_id = p.product_id
WHERE 
    STRFTIME('%Y-%m-%d', date) BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY client_id
"""

# Execute the query and load results into a DataFrame
result = pd.read_sql(query_test, conn)

# Print the query results
print(result)

# Close the SQLite connection
conn.close()
