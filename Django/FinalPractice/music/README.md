# README

> 가수와 가수가 부른 노래를 Postman을 통해 저장할 수 있도록 하는 pjt

- pjt/artists/
  - GET : 모든 가수의 id와 name, 각각의 음악, 음악 수 JSON으로 응답
  - POST : 가수의 정보 생성
    - 생성 시 201
    - 검증 실패 시 400
- pjt/artists/<artist_pk>/
  - GET : 특정 가수의 모든 음악 정보 JSON으로 응답
- pjt/artists/<artist_pk>/music/
  - POST : 특정 가수의 음악 정보 생성
    - 생성 시 201
    - 검증 실패 시 400
- pjt/music/
  - GET : 모든 음악의 id와 title JSON으로 응답
- pjt/music/<music_pk>/
  - GET : 특정 음악의 모든 컬럼 JSON으로 응답
  - PUT : 특정 음악의 음악 정보 수정
    - 검증 실패 시 400
  - DELETE : 특정 음악 정보 삭제
    - 삭제 시 204