# 바로쓰는 오라클 클라우드 (부제 : Build and Deploy Modern Apps with Oracle Cloud)

- 이 책은 오라클 클라우드와 오픈 소스 기술을 중점으로 다루는 실습 중심 도서입니다.
- 실제 클라우드 환경에서 유용한 서비스를 구현하면서 오라클 클라우드의 활용법을 익히는 데 초점이 맞춰져 있으며, 독자가 미래 업무 요구 사항에 맞게 더 정교한 시스템을 구성하는 데 도움을 주기 위한 자료로 구성되었습니다.
- 이 책에서는 웹 애플리케이션부터 쿠버네티스 기반의 마이크로서비스, 서버리스 애플리케이션, 데이터 레이크하우스, 그리고 머신러닝 시스템과 같은 다양한 서비스를 클라우드 환경에서 구현하는 과정을 상세히 다룰 것입니다.
- 이를 통해 클라우드를 처음 접하는 독자들도 초보자에서 중급자 수준까지 스스로 성장할 수 있는 기회를 얻게 될 것입니다. 



- 이 저장소는 바로쓰는 오라클 클라우드 (Build and Deploy Modern Apps with Oracle Cloud)의 전체 소스코드를 제공합니다.
- 책의 오류를 발견하시면 ociexplained@gmail.com 으로 보내주시면 감사하겠습니다.
- 책 구매 링크 : TBD

---

## 책의 특징

- 국내 최초로 발간되는 한국어로 된 오라클 클라우드 기술 활용서로, 실무에서 바로 활용 가능한 내용을 제공
- 오라클 클라우드 뿐만 아니라, 전반적인 클라우드 기반 기술과 오픈 소스 기술에 대한 핵심 개념을 간결하게 설명
- 책 내에는 120여 개의 도해와 그림이 포함되어 있어 복잡한 시스템 구성도를 한눈에 이해할 수 있으며, 쉽게 따라하면서 오라클 클라우드 기술을 습득할 수 있도록 안내
- 실습을 통해 3-Tier 웹 애플리케이션을 구현하는 과정을 통해 컴퓨트 인스턴스에서부터 오토 스케일링까지 오라클 클라우드의 사용법을 쉽게 설명
- 쿠버네티스 환경에서 모노리식 애플리케이션을 마이크로서비스로 변환하고 CI/CD 구축부터 서비스 메시까지 구현하는 방법을 안내
- 서버리스 기술을 활용하여 저장된 애플리케이션 데이터를 데이터 카탈로그와 ETL 프로세스를 활용하여 데이터 레이크하우스를 쉽게 구축하는 방법과 오픈 서치 기술 활용법을 제시
- 파이썬 기반의 머신러닝부터 오라클 데이터베이스 내장 알고리즘을 활용한 머신 러닝 분석에 이르기까지 다양한 주제를 경험

---

## 대상 독자

- 클라우드와 오픈소스 기술에 처음 접하는 학생이나 기초를 쌓고자 하는 분들
- 오라클 클라우드의 전체 기술 스택을 이해하고자 하는 클라우드 사용자
- 클라우드 자격증을 준비하며 클라우드 관련 지식을 쌓으려는 독자

---

## 도와주신 분들

- 베타 리뷰어 : 정다혜, 김태완, 김동후
- 저술관련 스폰서십 : 이경희, 홍기현

---

## 목차

### 1 장 오라클 클라우드로 구현해 보는 웹 애플리케이션 시스템

1.1 사전 지식

### 1.2 이 장의 실습

1.2.1 가상 클라우드 네트워크 구성

1.2.2 가상 머신 생성

1.2.3 Bastion 서비스 생성

1.2.4 통신을 위한 네트워크 설정

1.2.5 데이터베이스 설치 및 구성

1.2.6 애플리케이션 배포

1.2.7 HTTPS 연결 설정

1.2.8 로드밸런서, 오토스케일링 설정

1.2.9 OCI CLI 를 활용한 자원 정리

1.3 이 장의 요약

### 2 장. 오라클 클라우드로 구현해 보는 마이크로서비스

2.1 사전 지식

2.1.1 도커

2.1.2 쿠버네티스

2.1.3 마이크로서비스

2.1.4 서비스 메시, 이스티오

### 2.2 이 장의 실습

2.2.1 개발 환경 가상 머신 생성 및 도커 실습

2.2.2 데이터베이스 서비스 인스턴스 생성

2.2.3 멀티테넌트 데이터베이스 구성

2.2.4 샘플 마이크로서비스 개발

2.2.5 OCI 쿠버네티스 배포

2.2.6 OCI 쿠버네티스 접속 환경 설정

2.2.7 쿠버네티스 환경 웹서버 배포 테스트

2.2.8 샘플 마이크로서비스 컨테이너 이미지 생성

2.2.9 OCI 레지스트리 배포

2.2.10 마이크로서비스 쿠버네티스 환경 배포

2.2.11 젠킨스를 통한 CI/CD 구현

2.2.12 이스티오를 이용한 서비스 메시 구성

2.2.13 애플리케이션 모니터링 구성

2.2.14 쿠버네티스 파드 오토스케일링 구성

2.2.15 실습 자원 정리

2.3 이 장의 요약

### 3 장 오라클 클라우드로 구현해 보는 데이터 레이크하우스

3.1 사전 지식

### 3.2 이 장의 실습

3.2.1 마이크로서비스의 서버리스 Function 전환

3.2.2 API 게이트웨이를 통한 서비스 통합

3.2.3 신규 업무 서버리스 Function 개발

3.2.4 데이터 카탈로그로 메타데이터 식별

3.2.5 데이터 레이크하우스 DB 생성

3.2.6 ETL, 익스터널 테이블 을 이용한 데이터 통합

3.2.7 오라클 Analytics 를 활용한 데이터 분석

3.2.8 오픈서치를 이용한 로그 분석

3.2.9 실습 자원 정리

3.3 이 장의 요약

### 4장 오라클 클라우드로 구현해 보는 데이터 머신 러닝

4.1 사전 지식

### 4.2 이 장의 실습

4.2.1 데이터 사이언스 활용한 머신 러닝 분석

4.2.2 OML4SQL 을 활용한 머신 러닝 분석

4.2.3 실습 자원 정리

4.3 이 장의 요약

부록. Oracle Cloud Free Tier 생성

참고 문헌
