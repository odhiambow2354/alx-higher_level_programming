-- script that creates a table with an id not null
CREATE TABLE IF NOT EXISTS `id_not_null` (
    `id`   INT          DEFAULT 1,
    `name` VARCHAR(256)
);
