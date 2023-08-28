CREATE TABLE book
(
        id varchar2(32) not null primary key,
        data_loaded timestamp,
        json_data varchar2(4000) 
        constraint ensure_json check (json_data is JSON)
) ;
