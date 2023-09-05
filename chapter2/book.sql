-------------------------------------------------------------------------------
-- chapter2/book.sql
-- oracle에서 json 저장소로 도서정보를 관리, 스키마리스 저장소
-------------------------------------------------------------------------------

CREATE TABLE book
(
        id varchar2(32) not null primary key,
        data_loaded timestamp,
        json_data varchar2(4000) 
        constraint ensure_json check (json_data is JSON)
) ;
