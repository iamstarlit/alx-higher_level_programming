-- cretes root user with all privileges.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES TO 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd'
WITH GRANT OPTION;

