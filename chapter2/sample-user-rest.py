#------------------------------------------------------------------------------
# chapter2/sample-user-rest.py
# oracle의 테이블 기반으로 restful 서비스를 구현
# GET, POST를 제공
# DB 접속 정보를 실습환경에 맞춘 후 진행
#------------------------------------------------------------------------------

import logging, cx_Oracle, json
from datetime import datetime
from flask import Flask, Response
from flask_restx import Api, Resource 
from faker import Faker #샘플 데이터 생성용 모듈

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
api = Api(app, version='1.0', title='사용자 관리 API', description='사용자 등록,조회 API입니다') 
api = api.namespace('v1/user', description='사용자 등록, 조회') 

logger = logging.getLogger() #로거 선언
logger.setLevel(logging.INFO)
fake = Faker("ko_KR")

#------------------------------------------------------------------------------
# DB 접속 정보 (테스트 환경에 맞춰 변경할 것)
#------------------------------------------------------------------------------
userpdb_host_ip = 'oci-demo-msadb-scan.xxxxxxxxxx.ocidemo.oraclevcn.com'
userpdb_svc_name = 'userpdb.xxxxxxxxxxx.ocidemo.oraclevcn.com'
userpdb_user_name = 'system'
userpdb_passwd = 'xxxxxxxxx'
userpdb_port = 1521

@api.route('/')  
class user(Resource):
    def post(self):
        '''사용자 정보를 등록한다'''
        try:
            #oracle db 접속
            oradb_conn = cx_Oracle.connect(userpdb_user_name, userpdb_passwd, userpdb_host_ip + '/' + userpdb_svc_name)
            
            #사용자의 접속이력을 기록 
            oradb_sql = "insert into users(user_name,job,client_ip,last_conn_date) values (:1,:2,:3,systimestamp)"
            oradb_sql_val = (fake.name(),fake.job(),fake.ipv4_private())
            oradb_conn.cursor().execute(oradb_sql,oradb_sql_val)
            oradb_conn.commit()
            
            #db연결 해제 
            oradb_conn.close()
        except Exception as e:
            logger.error("oracle db error : could not insert data")
            logger.error(e)
        logger.info("success : inserting data succeeded.")
        return oradb_sql_val, 200, { "success" : "inserting data succeeded." }

    def get(self):  
        '''사용자 정보를 조회한다'''
        try:
            #oracle db 접속
            oradb_conn = cx_Oracle.connect(userpdb_user_name, userpdb_passwd, userpdb_host_ip + '/' + userpdb_svc_name)
           
            #최종 접속 유저를 조회 
            oradb_sql = "select json_object(user_name,job,last_conn_date) from users order by last_conn_date desc fetch first 10 rows only"
            oradb_results = oradb_conn.cursor().execute(oradb_sql).fetchall()
            
            #db연결 해제 
            oradb_conn.close()
        except Exception as e:
            logger.error("oracle db error : could not fecth data")
            logger.error(e)
        logger.info("success : querying data succeeded.")
        return Response(json.dumps(oradb_results, ensure_ascii=False).encode('utf-8'), status=200, content_type='application/json; charset=utf-8')

@api.route('/hello')  
class hello(Resource):
    def get(self):  
        '''hello를 조회한다'''
        return "Hello, OCI!", 200, { "success" : "hello" } 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=False)
