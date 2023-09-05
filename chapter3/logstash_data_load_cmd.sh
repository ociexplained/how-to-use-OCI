#------------------------------------------------------------------------------
# chapter3/logstash_data_load_cmd.sh
# OCI 로그를 opensearch 에 적재하는 스크립트
# 오픈서치 URL과 로그 경로를 변경한 후 진행
#------------------------------------------------------------------------------

#!/bin/bash
bin/logstash -e 'input { file {path=>["/home/opc/my-log-objects/**/*.log"] sincedb_path => "NULL" start_position => "beginning" codec => json } } output { stdout {codec => rubydebug} opensearch { hosts => "https://xxxxxxxxxxxxxx.opensearch.<region>.oci.oraclecloud.com:9200" user => "ocidemo" password => "xxxxxxxxx" index => "logstash-logs-%{+YYYY.MM.dd}" ssl_certificate_verification => false } }'
