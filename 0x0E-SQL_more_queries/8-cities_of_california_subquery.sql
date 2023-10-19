-- Complex selection from a relation
SELECT id, name FROM cities WHERE id = (
	SELECT id FROM states WHERE name = 'California'
);
