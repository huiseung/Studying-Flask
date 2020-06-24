## Requirement
- editor: pycharm
- Flask 1.1.2

## Pycharm에서 Flask 프로젝트 진행하기
- pycharm community버전에서는 flask웹이 동작을 위해 추가 설정을 해야한다.
- 메뉴의 Run- Edit Configuration 클릭
  - script라 되어 있는걸 Module name으로 교체후 flask라 적는다.
  - parameters: run
  - Environment variables 다음을 추가 
    - FLASK_APP = 'name'
    - FLASK_DEBUG = 1

## windows에 httpie 설치
- http 요청을 디버깅할 수 있는 툴
- pip install -U httpie
- 플라스크 app을 실행시킨후 커맨드에 다음을 입력
  - `http -v 메소드 http://localhost:5000/엔드포인트_고유주소`

## simple_API
- simple_API.py
- 환경 구축 테스트
- pong을 리턴하는 엔드포인드만 있는 단순 app


## Mini Twitter
- minitwitter.py
- 트위터의 몇몇 기능들을 API형태로 구현해보자
  - 회원가입
  - 로그인
  - 트윗
  - 팔로우
  - 언팔로우
  - 타임라인
- 실제 서비스는 상당한 수의 동시 접속자를 처리하기 위해 많은것을 고려한다.
- 본 프로젝트는 API개발 입문 목적으로 그러한 것을 고려하지 않는다.
