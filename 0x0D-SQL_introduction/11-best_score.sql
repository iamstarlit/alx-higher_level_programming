-- lists all records oreder by top scores >= 10.
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC, name ASC;

