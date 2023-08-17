-- Lists all Comedy shows in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title.
-- You can use only one SELECT statement.
SELECT DISTINCT ts.`title`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg ON ts.`id` = tsg.`show_id`
INNER JOIN `tv_genres` AS tg ON tg.`id` = tsg.`genre_id`
WHERE tg.`name` = 'Comedy'
ORDER BY ts.`title`;
