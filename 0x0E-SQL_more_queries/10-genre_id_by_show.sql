-- List all shows that have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres
JOIN tv_genres ON tv_genres.id = tv_show_genres.genres_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title AND tv_show_genres.genre_id;
