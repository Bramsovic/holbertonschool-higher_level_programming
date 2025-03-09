-- Select the 'id' and 'name' of cities along with the corresponding state name
-- Use INNER JOIN to match cities with their respective states based on 'state_id'
-- Order the results by 'cities.id' in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
