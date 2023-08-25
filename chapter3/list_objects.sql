-------------------------------------------------------------------------------
-- chapter3/list_objects.sql
-- 오브젝트 버킷의 파일 조회
-- 오브젝트 스토리지 주소 및 json 파일 명은 실습환경에 맞춰 변경 후 진행
-------------------------------------------------------------------------------

select object_name
from   dbms_cloud.list_objects(
         'ocidemoextcred',
          ----------------------------------------------------------------------------
          -- 오브젝트 스토리지 주소 및 json 파일 명 변경
          ----------------------------------------------------------------------------
         'https://objectstorage.ap-chuncheon-1.oraclecloud.com/n/ociexplained/b/oci-demo-bucket/o/')
where object_name like 'order_2023%';
