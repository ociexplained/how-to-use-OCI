#------------------------------------------------------------------------------
# chapter3/oci-demo-orderfn/func.py
# OCI func 주문 앱을 배포  
# API URL 정보를 실습환경에 맞춘 후 진행
#------------------------------------------------------------------------------

import io
import json
import logging
from datetime import datetime
from faker import Faker  
import requests, oci

from fdk import response

def handler(ctx, data: io.BytesIO = None):
    result = order()
    return response.Response(
        ctx, response_data=result,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )

def order():
    fake = Faker()
    #------------------------------------------------------------------------------
    # API URL 정보 (테스트 환경에 맞춰 변경할 것)
    #------------------------------------------------------------------------------
    BOOK_API_URL = "https://xxxxxxxxxxxxxx.apigateway.<region>.oci.customer-oci.com/v1/book"
    USER_API_URL = "https://xxxxxxxxxxxxxx.apigateway.<region>.oci.customer-oci.com/v1/user"
    signer = oci.auth.signers.get_resource_principals_signer()
    client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    namespace = client.get_namespace().data
    bucket_name = "oci-demo-bucket"

    try:
        user_resp = requests.get(USER_API_URL)
        book_resp = requests.get(BOOK_API_URL)
        user = user_resp.json()
        book = book_resp.json()

        #유저 정보 기록
        order = {}
        order['user'] = json.loads(user[0][0])
        order['order_time'] = dt = datetime.now().strftime('%Y%m%d_%H%M%S')
        order['orders'] = []

        #도서 주문 기록
        for x in book:
            rows_book = x
            for y in rows_book:
                rand_num = fake.pyint(min_value=1,max_value=3)
                #리스트를 딕셔너리로 변환
                row_book = json.loads(y)
                #구매 개수 추가
                row_book['cnt'] = rand_num
                order["orders"].append(row_book)

        result = json.dumps(order, default=str, ensure_ascii=False)
        file_nm = "order_" + dt + ".json"
        obj = client.put_object(namespace, bucket_name, file_nm, result.encode('utf-8'))
    except (Exception, ValueError) as ex:
        logging.getLogger().info('error parsing json payload: ' + str(ex))

    return result.encode('utf-8')
