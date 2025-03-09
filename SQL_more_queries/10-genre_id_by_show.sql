-- Select the title of TV shows along with their corresponding genre ID
-- Use INNER JOIN to link 'tv_show_genres' with 'tv_shows' and 'tv_genres'
-- Order the results by TV show title in ascending order, then by genre ID in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
