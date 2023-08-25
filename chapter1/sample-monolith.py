#------------------------------------------------------------------------------
# chapter1/sample-monolith.py
# mysql을 활용한 모놀리식 아키텍처 기반 sample app
# DB 접속 정보를 실습환경에 맞춘 후 진행
#------------------------------------------------------------------------------

import logging, pymysql, json
from datetime import datetime
from flask import Flask
from faker import Faker 

app = Flask(__name__)

#로거 선언
logger = logging.getLogger() 
logger.setLevel(logging.INFO)

fake = Faker()

#------------------------------------------------------------------------------
# DB 접속 정보 (테스트 환경에 맞춰 변경할 것)
#------------------------------------------------------------------------------
mysql_db_host_ip = '10.0.1.xx'
mysql_db_user_name = 'root'
mysql_db_passwd = 'xxxxxxxxxx'
mysql_db_name = 'test'

#"/" 엔드포인트 HTTP GET 메소드응답  
@app.route('/', methods=['GET'])
def index():
    try:
        #mysqldb 접속
        mysql_conn = pymysql.connect(host=mysql_db_host_ip, user=mysql_db_user_name, password=mysql_db_passwd, db=mysql_db_name)
        
				#커서 생성 
        mysql_cursor = mysql_conn.cursor()
        
				#사용자의 접속이력을 기록 
        mysql_sql = "insert into users(user_name,job,client_ip,last_conn_date) values (%s,%s,%s,current_timestamp)"
        mysql_sql_val = (fake.name(),fake.job(),fake.ipv4_private())
        mysql_cursor.execute(mysql_sql,mysql_sql_val)
        
				#최종 접속 사용자를 조회 
        mysql_sql = "select user_name, job, client_ip, DATE_FORMAT(last_conn_date, '%Y-%m-%d %T.%f') from users order by last_conn_date desc limit 10"
        mysql_cursor.execute(mysql_sql)
        mysql_results = mysql_cursor.fetchall()
        
				#조회결과 json변환
        mysql_result = json.dumps(mysql_results, default=str)
        
				#commit 
        mysql_conn.commit()
        
				#db연결 해제 
        mysql_conn.close()

    except Exception as e:
        logger.error("mysql error : could not fecth data")
        logger.error(e)

    logger.info("success : querying data succeeded.")

    return mysql_result

@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, OCI!'
