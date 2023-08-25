-------------------------------------------------------------------------------
-- chapter3/dc_book.sql
-- 데이터 카탈로그에서 도서 서비스 저장소 조회하기 위한 DB유저 생성
-------------------------------------------------------------------------------

drop user datacat cascade;
create user datacat identified by xxxxxxxxxx;
grant connect,resource to datacat;
grant select on book to datacat;
create or replace view datacat.v_book as select * from system.book;
