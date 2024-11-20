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

# Load transaction data into a pandas DataFrame
transaction_df = pd.read_csv(StringIO(transaction_data))

# Convert the date column to datetime
transaction_df['date'] = pd.to_datetime(transaction_df['date'], format='%d/%m/%y')

# Create SQLite database (in mempry)
conn = sqlite3.connect(":memory:")

# Load the transaction data into an SQLite table
transaction_df.to_sql('transaction_table', conn, index=False, if_exists='replace')

# SQL query to calculate total transaction amounts grouped by date
query_test = """
SELECT 
    STRFTIME('%Y-%m-%d', date) AS transaction_date,
    SUM(prod_price * prod_qty) AS total_amount
FROM transaction_table
WHERE STRFTIME('%Y-%m-%d', date) BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY transaction_date
ORDER BY transaction_date;
"""

# Execute the query and fetch the results into a pandas DataFrame
result = pd.read_sql(query_test, conn)

# Display the result of the SQL query
print(result)

# Close the SQLite connection
conn.close()
