#flask를 이용한 book 관리 
import logging, cx_Oracle, json
from datetime import datetime
from flask import Flask
from flask_restx import Api, Resource 
from faker import Faker, Reponse #샘플 데이터 생성용 모듈
from faker_datasets import Provider, add_dataset

app = Flask(__name__)
api = Api(app, version='1.0', title='도서 관리 API', description='도서 등록,조회 API입니다') 
api = api.namespace('v1/book', description='도서 등록, 조회') 
logger = logging.getLogger() #로거 선언
logger.setLevel(logging.INFO)

@add_dataset("books", "books.json", picker="book")
class Books(Provider):
    pass
fake = Faker()
fake.add_provider(Books)

#DB 접속 정보 
bookpdb_host_ip = 'oci-demo-msadb-scan.sub05220430511.ocidemo.oraclevcn.com'
bookpdb_svc_name = 'bookpdb.sub05220430511.ocidemo.oraclevcn.com'
bookpdb_user_name = 'system'
bookpdb_passwd = 'MSAdb##01'
bookpdb_port = 1521

@api.route('/')  
class book(Resource):
    def post(self):
        '''상품 정보를 등록한다'''
        try:
            #데이터 생성 
            book = fake.book()
            book_data ={}
            book_data['title'] = '{TITLE_NM}'.format(**book)
            book_data['author'] = '{AUTHR_NM}'.format(**book)
            book_data['publisher'] = '{PUBLISHER_NM}'.format(**book)
            book_data['price'] = '{PRC_VALUE}'.format(**book)
            book_data['img'] = '{IMAGE_URL}'.format(**book)

            #oracle db 접속
            oradb_conn = cx_Oracle.connect(bookpdb_user_name, bookpdb_passwd, bookpdb_host_ip + '/' + bookpdb_svc_name,encoding='UTF-8' )

            #상품 등록 이력을 기록 
            oradb_sql_val = json.dumps(book_data,ensure_ascii=False,default=str)
            oradb_sql = "insert into book (id, data_loaded,json_data) values (sys_guid(),systimestamp,'"+ oradb_sql_val + "')"
            oradb_conn.cursor().execute(oradb_sql)
            oradb_conn.commit()
            #db연결 해제 
            oradb_conn.close()
        except Exception as e:
            logger.error("oracle db error : could not insert data")
            logger.error(e)
        logger.info("success : inserting data succeeded.")
        return Response(json.dumps(oradb_sql_val, ensure_ascii=False).encode('utf-8'), status=200, content_type='application/json; charset=utf-8')

    def get(self):  
        '''상품 정보를 조회한다'''
        try:
            #oracle db 접속
            oradb_conn = cx_Oracle.connect(bookpdb_user_name, bookpdb_passwd, bookpdb_host_ip + '/' + bookpdb_svc_name)
            #최종 접속 유저를 조회 
            oradb_sql = "select json_object(*)  from book order by data_loaded desc fetch first 10 rows only"
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
