/*
  chapter2/book.sql
  오라클 데이터베이스에서 도서 정보를 관리하는 테이블
*/

CREATE TABLE book
(
        id varchar2(32) not null primary key,
        data_loaded timestamp,
        json_data varchar2(4000) 
        constraint ensure_json check (json_data is JSON)
) ;
