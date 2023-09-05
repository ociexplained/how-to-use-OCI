/*
  chapter1/mysql_schema.sql
  mysql에서 사용자 정보를 관리하는 테이블
*/

CREATE TABLE users
(
        user_id int,
        user_name VARCHAR(100),
        country VARCHAR(100),
        job VARCHAR(100),
        email VARCHAR(100),
        client_ip VARCHAR(100),
        last_conn_date timestamp
);
