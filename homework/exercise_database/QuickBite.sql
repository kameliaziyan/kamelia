-- Part 4 — Queries

-- query 1
-- Select all restaurants sorted by name alphabetically.

SELECT *
FROM restaurants
ORDER BY name ASC;


-- query 2
-- Select all menu items that cost more than ₪40, sorted by price descending.

SELECT *
FROM menu
WHERE price > 40
ORDER BY price DESC;


-- query 3 
-- Find all restaurants whose name contains "burger" (case-insensitive).

SELECT *
FROM restaurants
WHERE name LIKE '%Burger%';


-- query 4 
-- Select all orders with status `delivered` or `cancelled`.

SELECT *
FROM orders
WHERE status ='delivered' or status = 'cancelled';


-- query 5
-- Find all menu items in the `Dessert` category, sorted by price ascending.

SELECT *
FROM menu
WHERE category = 'Dessert'
ORDER BY price ASC;


-- query 6
-- Select all customers who registered in 2024.

SELECT *
FROM customers
WHERE year(registration_date) = 2024;


-- query 7
-- Find all restaurants with a rating of 4.0 or higher that are active.

SELECT *
FROM restaurants
WHERE rating >=4 AND is_active =1;


-- query 8
-- Show all orders with the customer name and restaurant name.

SELECT o.i AS order_id , c.name AS customer_name , r.name AS retaurant_name
FROM orders o JOIN customers c ON o.customer_id = c.id JOIN restaurants r ON o.restaurant_id = r.id;


-- query 9 
-- For each restaurant, show how many menu items they have. Sort by count descending.

SELECT r.name AS 'restaurant name', COUNT(m.id) AS 'total menu items'
FROM restaurants r LEFT JOIN menu m ON r.id = m.restaurant_id
GROUP BY r.id, r.name
ORDER BY COUNT(m.id) DESC;


-- query 10
-- Show all reviews alongside the customer name and restaurant name.

SELECT rev.comment AS 'review comment', rev.rating AS 'review rating', res.name AS 'restaurant name', c.name AS 'customer name'
FROM review rev JOIN customers c on rev.customer_id = c.id JOIN restaurants res  on rev.restaurant_id = res.id;



-- query 11
-- For each order, calculate the **total price** (sum of item price × quantity). 
-- Show the order ID, customer name, restaurant name, and total.

SELECT o.id AS 'order id', c.name AS 'customer name', r.name AS 'restaurant name ', SUM(m.price * oi.quantity) AS 'total price' 
FROM orders o JOIN customers c on o.customer_id = c.id JOIN restaurants r  on o.restaurant_id = r.id 
JOIN order_items oi on o.id = oi.order_id JOIN menu m on oi.menu_item_id = m.id
GROUP BY o.id,c.name,r.name;


-- query 12
-- Find the **most expensive menu item** for each restaurant. Show restaurant name, item name, and price.

SELECT R.name AS 'Restaurant Name', M.item_name AS 'Item Name', M.price AS 'MAX Price' 
FROM menu M JOIN restaurants R ON M.restaurant_id = R.id
WHERE M.price = (
	SELECT MAX(price)
	FROM menu
	WHERE restaurant_id = R.id
);


-- qurery 13 
-- Show the **number of orders per status** (how many pending, how many delivered, etc.).

SELECT status, count(*) AS 'total orders'
FROM orders
GROUP BY status;


-- query 14
-- List all customers who have **never placed an order**.

SELECT c.id AS 'customer id', c.name AS 'customer name'
FROM customers c LEFT JOIN orders o on c.id = o.customer_id
WHERE o.id is NULL ;



-- query 15
-- For each restaurant, show the **average review rating**. 
-- Only include restaurants with **3 or more reviews**. Sort by average rating descending.

SELECT res.id AS "restaurant id", res.name AS "restaurant name", AVG(rev.rating) AS "average rating", count(rev.id) AS "total reviews" 
FROM restaurants res JOIN review rev ON res.id = rev.restaurant_id
GROUP BY res.id , res.name
HAVING COUNT(rev.id)>=3
ORDER BY AVG(rev.rating) DESC;


-- query 16
-- Find the **top 3 customers** by total amount spent across all their orders.

SELECT c.id AS "customer id", c.name AS "customer name", SUM(m.price * oi.quantity) AS "total spent"
FROM customers c JOIN orders o on c.id = o.customer_id JOIN order_items oi on o.id = oi.order_id JOIN menu m on oi.menu_item_id = m.id
GROUP BY c.id, c.name
ORDER BY SUM(m.price * oi.quantity) DESC
LIMIT 3; 


-- query 17
-- Find customers who have ordered from **more than 3 different restaurants**.

SELECT c.id AS "customer id", c.name AS "customer name", COUNT(distinct o.restaurant_id) AS "number of restaurants"
FROM customers c JOIN orders o ON c.id = o.customer_id 
GROUP BY c.id, c.name
HAVING COUNT(DISTINCT o.restaurant_id) > 3;



-- query 18
-- Write a single query that shows a **"platform dashboard"**:
-- Total active restaurants
-- Total customers
-- Total delivered orders this month
-- Total revenue this month
-- Average order value this month
-- The cuisine type with the highest revenue this month

SELECT "Total active restaurants" AS "description" , count(*) AS "value"
FROM restaurants
WHERE is_active = 1
UNION
SELECT "Total Customers" AS "description" ,count(*) AS "value"
FROM customers
UNION 
SELECT "Total delivered orders this month" AS "description", COUNT(*) AS "value"
FROM orders
WHERE year(date) = year(curdate()) and month(date) = month(curdate())
UNION
SELECT "Total revenue this month" AS "description", sum(m.price * oi.quantity) AS "value"
FROM orders o JOIN order_items oi on o.id = oi.order_id JOIN menu m on oi.menu_item_id = m.id 
WHERE o.status = "delivered" and year(o.date) = year(curdate()) and month(date) = month(curdate())
UNION
SELECT "Average order value this month" AS "description", AVG(order_total) AS "value"
FROM( 
SELECT o.id, SUM(m.price * oi.quantity) AS "order_total"
FROM orders o JOIN order_items oi on o.id = oi.order_id JOIN menu m on oi.menu_item_id = m.id 
WHERE o.status = "delivered" and year(o.date) = year(curdate()) and month(date) = month(curdate())
GROUP BY o.id
)result
UNION
SELECT "description" , "value"
FROM (
SELECT  "The cuisine type with the highest revenue this month" AS "description", r.cuisine_type AS "value"
FROM orders o JOIN order_items oi on o.id = oi.order_id JOIN menu m on oi.menu_item_id = m.id JOIN restaurants r on o.restaurant_id = r.id 
WHERE o.status = "delivered" and year(o.date) = year(curdate()) and month(date) = month(curdate())
GROUP BY r.cuisine_type
ORDER BY SUM(m.price * oi.quantity) DESC
LIMIT 1
) result ;

