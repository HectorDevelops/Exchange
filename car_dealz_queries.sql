	-- SELECT queries
SELECT * FROM users;
SELECT * FROM car_dealz;

-- get_all car_dealz and who they belong to 
SELECT * FROM car_dealz
JOIN users 
WHERE users.id = car_dealz.user_id;

-- Get party and the user (show one)
SELECT * FROM car_dealz
JOIN users 
ON users.id = car_dealz.user_id
WHERE car_dealz.user_id = 3;

	-- INSERT queries
-- create @classmethod 
INSERT INTO car_dealz (price, model, make, year, description, user_id)
VALUES (27000, 'Camaro', 'Chevy', 2023 , 'One of the best coupe cars!', 1);

INSERT INTO car_dealz (price, model, make, year, description, user_id)
VALUES (218000, 'Porsche', '911 GT3 Coupe', 2018 , 'Woooo, speedy speed!', 2);

	-- UPDATE queries
-- UPDATE table_name
-- SET column1 = value1, column2 = value2, ...
-- WHERE condition;
UPDATE car_dealz 
SET price = 10000, model = 'Passat', make = 'VW', year = 2016, description = "Gray Sedan"
WHERE id = 1;

	-- DELETE queries
-- DELETE FROM table_name WHERE condition;

	-- DELETE enable 
-- SET SQL_SAFE_UPDATES = 0;