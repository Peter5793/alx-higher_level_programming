-- write script to convert database to utf8mb
USE `hbtn_0c_0`
ALTER `first_table`
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
