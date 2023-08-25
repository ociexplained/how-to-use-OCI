#------------------------------------------------------------------------------
# chapter3/oci-demo-bookfn/Dockerfile
# 도서 앱을 도커이미지로 빌드
#------------------------------------------------------------------------------

FROM oraclelinux:8-slim
COPY . /function
WORKDIR /function
RUN groupadd --gid 1000 fn && adduser --uid 1000 --gid fn fn

RUN microdnf install -y yum && \
    yum install -y python38 && \
    yum install -y oracle-instantclient-release-el8 && \
    yum install -y oracle-instantclient-basic && \
    yum clean all && \
    pip3 install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/fdk", "/function/func.py", "handler"]
