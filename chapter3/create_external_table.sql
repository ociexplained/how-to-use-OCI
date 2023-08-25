-------------------------------------------------------------------------------
-- chapter3/create_external_table.sql
-- exteral table 생성 
-- 오브젝트 스토리지 주소 및 파일 명은 실습환경에 맞춰 변경 후 진행
-------------------------------------------------------------------------------


BEGIN
  DBMS_CLOUD.CREATE_EXTERNAL_TABLE (
   table_name =>'order_ext',
   credential_name =>'ocidemoextcred',
   ----------------------------------------------------------------------------
   -- 오브젝트 스토리지 주소 및 json 파일 명 변경
   ----------------------------------------------------------------------------
   file_uri_list =>'https://objectstorage.ap-chuncheon-1.oraclecloud.com/n/ociexplained/b/oci-demo-bucket/o/order_2023*.json',
   column_list => 'json_document VARCHAR2(4000)',
   field_list => 'json_document CHAR(5000)'
);
END;
