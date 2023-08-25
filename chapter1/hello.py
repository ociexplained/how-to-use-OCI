#------------------------------------------------------------------------------
# chapter1/hello.py
# flask기반 sample app, Hello OCI!
#------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route('/')  # "/" 엔드포인트 
def hello_oci(): # HTTP 응답으로 반환하는 함수
    return 'Hello, OCI!'
