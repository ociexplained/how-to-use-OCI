#------------------------------------------------------------------------------
# chapter3/oci-demo-userfn/func.py
# OCI func기반 사용자 앱
# DB 접속 정보를 실습환경에 맞춘 후 진행
#------------------------------------------------------------------------------

import io
import json
import logging
import cx_Oracle
from datetime import datetime
from faker import Faker

from fdk import response

def handler(ctx, data: io.BytesIO = None):
    oradb_results = user()
    return response.Response(
        ctx, response_data=json.dumps(oradb_results, ensure_ascii=False).encode('utf-8'),
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

def user():
    #------------------------------------------------------------------------------
    # DB 접속 정보 (테스트 환경에 맞춰 변경할 것)
    #------------------------------------------------------------------------------
    userpdb_host_ip = 'oci-demo-msadb-scan.xxxxxxxxxx.ocidemo.oraclevcn.com'
    userpdb_svc_name = 'userpdb.xxxxxxxxxxx.ocidemo.oraclevcn.com'
    userpdb_user_name = 'system'
    userpdb_passwd = 'xxxxxxxxxx'
    userpdb_port = 1521

    logging.getLogger('faker').setLevel(logging.ERROR)
    fake=Faker("ko_KR")

    try:
        #oracle db 접속
        oradb_conn = cx_Oracle.connect(userpdb_user_name, userpdb_passwd, userpdb_host_ip + '/' + userpdb_svc_name)
        
	#유저의 접속이력을 기록 
        oradb_sql = "insert into users(user_name,job,client_ip,user_agent,birth,last_conn_date) values (:1,:2,:3,:4,:5,systimestamp)"
        oradb_sql_val = (fake.name(),fake.job(),fake.ipv4_private(),fake.user_agent(),fake.date_of_birth())
        oradb_conn.cursor().execute(oradb_sql,oradb_sql_val)
        oradb_conn.commit()
        
        #랜덤 1 유저를 조회 
        oradb_sql = "select json_object(user_name,job,client_ip,user_agent,birth,last_conn_date) from users order by dbms_random.random Fetch first 1 rows only" 
        oradb_results = oradb_conn.cursor().execute(oradb_sql).fetchall()
        
	#db연결 해제 
        oradb_conn.close()

    except (Exception, ValueError) as ex:

        logging.getLogger().info('oracle db error : could not fecth data :' + str(ex))

    return oradb_results
