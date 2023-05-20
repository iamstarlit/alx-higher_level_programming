-- lists all genre from the database with number of shows.
SELECT g.name,
       COUNT(*) AS number_of_shows
FROM tv_genres g
INNER JOIN tv_show_genres t
ON g.id = t.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;

