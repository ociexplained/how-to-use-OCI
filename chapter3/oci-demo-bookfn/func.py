#------------------------------------------------------------------------------
# chapter3/oci-demo-bookfn/func.py
# OCI func 도서 앱
# DB 접속 정보를 실습환경에 맞춘 후 진행
#------------------------------------------------------------------------------

import io
import json
import logging
import cx_Oracle
from faker import Faker
from faker_datasets import Provider, add_dataset

from fdk import response

def handler(ctx, data: io.BytesIO = None):
    oradb_results = book()
    return response.Response(
        ctx, response_data=json.dumps(oradb_results, ensure_ascii=False).encode('utf-8'),
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

def book():
    @add_dataset("books", "books.json", picker="book")
    class Books(Provider):
        pass
    logging.getLogger('faker').setLevel(logging.ERROR)
    fake = Faker()
    fake.add_provider(Books)

    #------------------------------------------------------------------------------
    # DB 접속 정보 (테스트 환경에 맞춰 변경할 것)
    #------------------------------------------------------------------------------
    bookpdb_host_ip = 'oci-demo-msadb-scan.xxxxxxxxxxxxxx.ocidemo.oraclevcn.com'
    bookpdb_svc_name = 'bookpdb.xxxxxxxxxxxx.ocidemo.oraclevcn.com'
    bookpdb_user_name = 'system'
    bookpdb_passwd = 'xxxxxxxxx'
    bookpdb_port = 1521

    #데이터 생성 
    book = fake.book()
    book_data ={}
    book_data['title'] = '{TITLE_NM}'.format(**book)
    book_data['author'] = '{AUTHR_NM}'.format(**book)
    book_data['publisher'] = '{PUBLISHER_NM}'.format(**book)
    book_data['price'] = '{PRC_VALUE}'.format(**book)
    book_data['img'] = '{IMAGE_URL}'.format(**book)
    try:
        oradb_conn = cx_Oracle.connect(bookpdb_user_name, bookpdb_passwd, bookpdb_host_ip + '/' + bookpdb_svc_name,encoding='UTF-8' )

        #상품 등록 이력을 기록 
        oradb_sql_val = json.dumps(book_data,ensure_ascii=False,default=str)
        oradb_sql_val = oradb_sql_val.replace("'","''")
        oradb_sql = "insert into book(id, data_loaded,json_data) values (sys_guid(),systimestamp,'"+ oradb_sql_val + "')"
        oradb_conn.cursor().execute(oradb_sql)
        oradb_conn.commit()

        #최근 등록 도서를 조회 
        rand_num = fake.pyint(min_value=1,max_value=10)
        oradb_sql = "select json_data from book order by dbms_random.random fetch first " + str(rand_num) + " rows only"
        oradb_results = oradb_conn.cursor().execute(oradb_sql).fetchall()

        #db연결 해제 
        oradb_conn.close()
    except (Exception, ValueError) as ex:
        logging.getLogger().info('oracle db error : could not fecth data :' + str(ex))
    return oradb_results
