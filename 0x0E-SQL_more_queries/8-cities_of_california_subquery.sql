-- script that lists all the cities of California that can be found in the database hbtn_0d_usa
-- the result retrevied ordered by ascending order
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	        FROM `states`
	       WHERE `name` = "California")
ORDER BY `id`;
