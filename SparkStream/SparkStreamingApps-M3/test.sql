DROP TABLE Pictures;
DROP TABLE Users;
DROP SEQUENCE Pictures_picture_id_seq;
DROP SEQUENCE Users_user_id_seq;

CREATE SEQUENCE Pictures_picture_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 14
  CACHE 1;

CREATE TABLE Pictures
(
  picture_id int4 NOT NULL DEFAULT nextval('Pictures_picture_id_seq'),
  caption varchar(255) NOT NULL,
  imgdata bytea NOT NULL,
  size int4 NOT NULL,
  content_type varchar(255) NOT NULL,
  thumbdata bytea NOT NULL,
  CONSTRAINT pictures_pk PRIMARY KEY (picture_id)
);

CREATE SEQUENCE Users_user_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 14
  CACHE 1;

CREATE TABLE Users
(
  user_id int4 NOT NULL DEFAULT nextval('Users_user_id_seq'),
  email varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  role_name varchar(255) NOT NULL DEFAULT 'RegisteredUser',
  CONSTRAINT users_pk PRIMARY KEY (user_id)
);

INSERT INTO Users (email, password) VALUES ('test@bu.edu', 'test');