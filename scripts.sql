/*
1) What are the 10 stores with the highest revenue in orders? Summarize this store's data
showing the following fields:
- StoreId
- Total volume of items sold
- Total value sold
2) What is the average monthly ticket of the requests submitted? What is the average monthly volume of
sales (all stores)?
3) What is the most sold and least sold item in the country with the highest sales volume?
*/
use ecommerce;

-- 1
SELECT store_id, 
	sum(quantity), 
    sum(quantity * unit_price) as total_volume
FROM sales
GROUP BY store_id
ORDER BY total_volum DESC
LIMIT 10;

-- 2
SELECT 
	month(invoice_date) as month, 
    sum(quantity*unit_price)/sum(quantity) as ticket_monthly, 
    sum(quantity)/12 as average_volume
FROM sales
GROUP BY month(invoice_date)
ORDER BY month(invoice_date);

-- 3
-- country with the highest sales volume:
SELECT 
	country, 
    sum(quantity) AS total_sales
FROM sales
GROUP BY country
ORDER BY total_sales DESC
LIMIT 1;

-- most sold item in this country:
SELECT 
	stock_code, 
	sum(quantity) as total_sales
FROM sales
WHERE country = 'United Kingdom'
GROUP BY stock_code
ORDER BY total_sales DESC
LIMIT 1;

-- least sold item in this country:
SELECT 
	stock_code, 
	sum(quantity) as total_sales
FROM sales
WHERE country = 'United Kingdom'
GROUP BY stock_code
ORDER BY total_sales ASC
LIMIT 1;

