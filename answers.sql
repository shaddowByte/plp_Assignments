
-- Query to retrieve checkNumber, paymentDate, and amount from the payments table
SELECT checkNumber, paymentDate, amount
FROM payments;


-- Query to retrieve orderDate, requiredDate, and status for orders that are 'In Process'
SELECT orderDate, requiredDate, status
FROM orders
WHERE status = 'In Process'
ORDER BY orderDate DESC;



-- Query to retrieve firstName, lastName, and email of employees with job title 'Sales Rep'
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
ORDER BY employeeNumber DESC;


-- Query to retrieve all columns and records from the offices table
SELECT * FROM offices;




-- Query to fetch productName and quantityInStock from the products table
SELECT productName, quantityInStock
FROM products
ORDER BY buyPrice ASC
LIMIT 5;
