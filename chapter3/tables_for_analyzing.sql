-------------------------------------------------------------------------------
-- chapter3/tables_for_analyzing.sql
-- 분석용 view 생성 
-------------------------------------------------------------------------------


-- 주문 정보 분석용 Table lh_order 생성 
CREATE TABLE lh_order AS 
SELECT jt.* 
FROM   order_ext, 
       json_table ( json_document, '$' COLUMNS ( user_name VARCHAR2 ( 300 ) path '$.user.user_name', job VARCHAR2 ( 300 ) path '$.user.job', client_ip VARCHAR2 ( 300 ) path '$.user.client_ip', user_agent VARCHAR2 ( 300 ) path '$.user.user_agent', birth VARCHAR2 ( 300 ) path '$.user.birth', order_time VARCHAR2 ( 300 ) path '$.order_time', nested path '$.orders[*]' COLUMNS ( title VARCHAR2 ( 300 ) path '$.title', author VARCHAR2 ( 300 ) path '$.author', publisher VARCHAR2 ( 300 ) path '$.publisher', price NUMBER path '$.price', img VARCHAR2 ( 300 ) path '$.img', cnt NUMBER path '$.cnt' ) ) ) jt
WHERE  publisher IS NOT NULL 
AND    price IS NOT NULL 
AND    img IS NOT NULL;
/

-- 도서 정보 분석용 Table lh_book 생성 
CREATE TABLE lh_book AS 
SELECT jt.*, 
       data_loaded load_time 
FROM   v_book, 
       json_table ( json_data, '$' COLUMNS ( title VARCHAR2 ( 300 ) path '$.title', author VARCHAR2 ( 300 ) path '$.author', publisher VARCHAR2 ( 300 ) path '$.publisher', price NUMBER path '$.price', img VARCHAR2 ( 300 ) path '$.img' ) ) jt
WHERE  publisher IS NOT NULL 
AND    price IS NOT NULL 
AND    img IS NOT NULL;
/

-- 사용자 정보 분석용 Table lh_user 생성 
CREATE TABLE lh_user AS 
  SELECT user_name, 
         job, 
         client_ip, 
         user_agent, 
         birth, 
         last_conn_date 
  FROM   v_users;
/
