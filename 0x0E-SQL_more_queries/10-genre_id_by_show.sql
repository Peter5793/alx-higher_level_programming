-- list all the shows contained in hbtn_tv_shows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER by tv_shows.title, tv_show_genres.genre_id;
