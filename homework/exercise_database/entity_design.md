# QuickBite Food Delivery Platform

## Initial table design<br>

**Restaurants**<br>
1. id
2. name
3. address
4. city
5. cuisine type (e.g., Italian, Japanese, Burgers)
6. rating (1–5)
7. whether they're currently active

**menu**<br>
1. id
2. resturant id
3. item name
4. description
5. price
6. category (e.g., Main, Side, Drink, Dessert).


**Customers**
1. id
2. name
3. email
4. phone number
5. city
6. registration date


**orders** <br>
1. id (order)
2. customer id
3. resturant id
4. date/time
5. status (`pending`, `preparing`, `delivering`, `delivered`, `cancelled`)
6. delivery address


**order items**??? <br>
1. id
2. order id
3. menu item id
4. quantuty

**review**
id
customer id
1. resturant id 
2. rating (1–5)
3. optional text comment.

---

## Relationships Between Tables <br>

Restaurant → Menu: One to Many<br>
One restaurant has many menu items. <br>
Customer → Orders: One to Many<br>
One customer can place many orders.<br>
Restaurant → Orders: One to Many<br>
One restaurant can receive many orders.<br>
Orders ↔ Menu: Many to Many<br>
An order can include many menu items, and a menu item can appear in many orders.<br>
This is handled by the order_items table.


---

## DDL exported from MySQL Workbench

CREATE TABLE `customers` ( <br>
  `id` int NOT NULL AUTO_INCREMENT,<br>
  `name` varchar(256) DEFAULT NULL,<br>
  `email` varchar(256) DEFAULT NULL,<br>
  `phone_number` varchar(256) DEFAULT NULL,<br>
  `city` varchar(256) DEFAULT NULL,<br>
  `registration_date` datetime DEFAULT NULL,<br>
  PRIMARY KEY (`id`),<br>
  CONSTRAINT `email` CHECK ((`email` like _utf8mb4'%_@_%._%')),<br>
  CONSTRAINT `email_format` CHECK ((`email` like _utf8mb4'%_@_%._%'))<br>
) <br><br>


CREATE TABLE `menu` (<br>
  `id` int NOT NULL AUTO_INCREMENT,<br>
  `restaurant_id` int DEFAULT NULL,<br>
  `item_name` varchar(256) DEFAULT NULL,<br>
  `description` varchar(256) DEFAULT NULL,<br>
  `price` decimal(5,2) DEFAULT NULL,<br>
  `category` varchar(256) DEFAULT NULL,<br>
  PRIMARY KEY (`id`),<br>
  KEY `fk_restaurant_idx` (`restaurant_id`),<br>
  CONSTRAINT `fk_menu_restaurant` FOREIGN KEY <br>(`restaurant_id`) REFERENCES `restaurants` (`id`)<br>
) <br><br>



CREATE TABLE `order_items` (<br>
  `order_id` int NOT NULL,<br>
  `menu_item_id` int NOT NULL,<br>
  `quantity` int DEFAULT NULL,<br>
  PRIMARY KEY (`order_id`,`menu_item_id`),<br>
  KEY `fk_menu_item_id_idx` (`menu_item_id`),<br>
  CONSTRAINT `fk_menu_item_id` FOREIGN KEY <br>(`menu_item_id`) REFERENCES `menu` (`id`),<br>
  CONSTRAINT `fk_order_id` FOREIGN KEY (`order_id`) <br>REFERENCES `orders` (`id`)<br>
)<br><br>


CREATE TABLE `orders` (<br>
  `id` int NOT NULL AUTO_INCREMENT,<br>
  `restaurant_id` int NOT NULL,<br>
  `customer_id` int NOT NULL,<br>
  `date` datetime DEFAULT NULL,<br>
  `status` enum('pending','preparing','delivering','delivered','cancelled') DEFAULT NULL,<br>
  `delivery_address` varchar(256) DEFAULT NULL,<br>
  PRIMARY KEY (`id`),<br>
  KEY `fk_restaurant_idx` (`restaurant_id`),<br>
  KEY `fk_order_customer` (`customer_id`),<br>
  CONSTRAINT `fk_order_customer` FOREIGN KEY <br>(`customer_id`) REFERENCES `customers` (`id`),<br>
  CONSTRAINT `fk_restaurant` FOREIGN KEY <br>(`restaurant_id`) REFERENCES `restaurants` (`id`)<br>
) <br><br>

CREATE TABLE `restaurants` (<br>
  `id` int NOT NULL AUTO_INCREMENT,<br>
  `name` varchar(256) DEFAULT NULL,<br>
  `address` varchar(256) DEFAULT NULL,<br>
  `city` varchar(256) DEFAULT NULL,<br>
  `cuisine_type` varchar(256) DEFAULT NULL,<br>
  `rating` int DEFAULT NULL,<br>
  `is_active` tinyint DEFAULT NULL,<br>
  PRIMARY KEY (`id`),<br>
  CONSTRAINT `rating_format` CHECK ((`rating` between 1 and 5)),<br>
  CONSTRAINT `resturant_rating` CHECK ((`rating` between 1 and 5))<br>
) <br><br>


CREATE TABLE `review` (<br>
  `id` int NOT NULL AUTO_INCREMENT,<br>
  `customer_id` int NOT NULL,<br>
  `restaurant_id` int NOT NULL,<br>
  `rating` int NOT NULL,<br>
  `comment` varchar(256) DEFAULT NULL,<br>
  PRIMARY KEY (`id`),<br>
  KEY `fk_restaurant_idx` (`restaurant_id`),<br>
  KEY `idx_customer_restaurant` (`customer_id`,`restaurant_id`),<br>
  CONSTRAINT `fk_review_customer` FOREIGN KEY <br>(`customer_id`) REFERENCES `customers` (`id`),<br>
  CONSTRAINT `fk_review_restaurant` FOREIGN KEY <br>(`restaurant_id`) REFERENCES `restaurants` (`id`),<br>
  CONSTRAINT `rating` CHECK ((`rating` between 1 and 5))<br>
) <br><br>

---



