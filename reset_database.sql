
#CREATE database  blog_site;
USE blog_site;
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS users;
SET FOREIGN_KEY_CHECKS=1;
-- ************************************** users

CREATE TABLE IF NOT EXISTS users
(
 user_id       VARCHAR(32) NOT NULL UNIQUE,
 password_hash VARBINARY(255) NOT NULL ,
 password_salt VARBINARY(255) NOT NULL,
 email         VARCHAR(128) NOT NULL ,
 role          VARCHAR(128) NOT NULL ,
 email_verification VARCHAR(255), # if null, email verified

PRIMARY KEY (user_id)
) ENGINE = InnoDB;
-- ************************************** posts

CREATE TABLE IF NOT EXISTS posts
(
 post_id      INT NOT NULL AUTO_INCREMENT,
 title        VARCHAR(100) NOT NULL ,
 date_created DATETIME NOT NULL ,
 preview      VARCHAR(100) ,
 user_id      VARCHAR(32) NOT NULL,
 post_content TEXT NOT NULL ,

PRIMARY KEY (post_id),
CONSTRAINT fk_user_post FOREIGN KEY (user_id)
REFERENCES users(user_id)
 ON DELETE CASCADE
 ON UPDATE RESTRICT
) ENGINE = InnoDB;
-- ************************************** post_content
