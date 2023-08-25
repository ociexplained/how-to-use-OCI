-------------------------------------------------------------------------------
-- chapter3/dc_user.sql
-- 데이터 카탈로그에서 사용자 서비스 저장소 조회하기 위한 DB유저 생성
-------------------------------------------------------------------------------

drop user datacat cascade;
create user datacat identified by xxxxxxxxxx;
grant connect,resource to datacat;
grant select on users to datacat;
create or replace view datacat.v_users as select * from system.users;
