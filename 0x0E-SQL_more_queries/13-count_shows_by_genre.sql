-- Lists all genres and displays the number of shows linked to each
SELECT tv_genres.name AS genre, SUM(tv_show_genres.show_id) AS number_of_shows FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.id = tv_show_genres.genre_id GROUP BY genre ORDER BY number_of_shows DESC;
