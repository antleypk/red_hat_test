CREATE OR REPLACE USER 'svc_user'@'%' IDENTIFIED BY '';
UPDATE mysql.user SET Password = PASSWORD('fr1edchik3n') WHERE User = 'svc_user';
GRANT ALL PRIVILEGES on rh_test.* TO 'svc_user'@'%';
GRANT ALL PRIVILEGES on test.* TO 'svc_user'@'%';
FLUSH PRIVILEGES;


