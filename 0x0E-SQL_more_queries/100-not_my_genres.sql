-- script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter

SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
LEFT JOIN `tv_show_genres` AS sg ON g.`id` = sg.`genre_id`
LEFT JOIN `tv_shows` AS s ON sg.`show_id` = s.`id`
WHERE s.`title` = 'Dexter' AND sg.`show_id` IS NULL
ORDER BY g.`name`;
