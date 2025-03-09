-- Select the 'id' and 'name' of cities that belong to the state named 'California'
-- The subquery retrieves the 'id' of the state where the name is 'California'
SELECT cities.id, cities.name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE states.name = 'California'
);
