# E-COMMERCE STUDY
## About
Looking for ways to identify key customers and success factors on a platform to identify patterns and replicate actions for the entire base, we made this initial study to show insights based on colleted data. 

### Questions:

1) What are the 10 stores with the highest revenue in orders? Summarize this store's data
showing the following fields:
    - StoreId
    - Total volume of items sold
    - Total value sold
2) What is the average monthly ticket of the requests submitted? What is the average monthly volume of
sales (all stores)?
3) What is the most sold and least sold item in the country with the highest sales volume?

## Data dictionary:

The original CSV file: 
| InvoiceNumber | StoreID | StockCode | Description | Quantity | InvoiceDate | UnitPrice | CustomerId | Country
|:-------------:|:-------:|:--------:|:----------:| :-------:| :----------:| :--------:| :---------:|:------:|
|Order registration number|Store registration number|In-stock product id|Product description|Product quantity on order|Request Date|Product unit price|Customer identification|Country of purchase registration


## Files
This project contains the following files:

- __data_analysis.ipynb__: a Jupyter file with a preliminary analysis of the data in the original CSV
- __sql_queries.py__: a Python file with SQL queries. This file is imported by _etl.py_
- __etl.py__: the main script of project where the data is extracted, transformed and loaded to MySQL database
- __scripts.sql__: SQL queries of the questions made
- __Data file__: a folder with the original CSV and where the new CSV is saved.


## Report
In the preliminary analysis, quantitative data fields with negative values were found. In this case these fields must be eliminated so as not to influence the final results.

Some stock identifiers (_stock_code_) reference discounts and shipping amounts (alphanumeric or letter-only stock codes). Such values were also discarded.

The column names were also modified to avoid problems in database queries, replacing "_camelCase_" with "_snake_case_".

All those modifications above are made in "_etl.py_", where are made the connections and the necessary queries to database MySQL, and the table inserts.