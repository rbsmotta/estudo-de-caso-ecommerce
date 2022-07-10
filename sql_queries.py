# dropping database if exists
drop_ecommerce = "DROP DATABASE IF EXISTS ecommerce"

# creating database
create_ecommerce = "CREATE DATABASE ecommerce"

# changing to created database
use_ecommerce = "USE ecommerce"

# dropping table
drop_sales_table = "DROP TABLE IF EXISTS ecommerce"

# creating table
create_sales_table = ("""
    CREATE TABLE IF NOT EXISTS sales (
        invoice_number VARCHAR(20) NOT NULL,
        store_id VARCHAR(20) NOT NULL,
        stock_code VARCHAR(20) NOT NULL,
        description VARCHAR(256),
        quantity INT NOT NULL,
        invoice_date DATETIME,
        unit_price FLOAT,
        customer_id VARCHAR(20),
        country VARCHAR(100)
    );

""")

# data insert
sales_insert = ("""
    INSERT INTO sales (invoice_number, store_id, stock_code, description, quantity, invoice_date, unit_price, customer_id, country)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)

""")
