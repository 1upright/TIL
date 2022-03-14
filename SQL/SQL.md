# SQL

## Database(DB)

- 체계화된 데이터의 모임
- 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합
- 논리적으로 연관된 하나 이상의 자료 모음으로 그 내용을 고도로 구조화 함으로써 검색과 갱신의 효율과를 꾀한 것
- 몇개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억시켜 놓은 자료의 집합체
- 얻는 장점
  - 데이터 중복 최소화
  - 데이터 무결성
  - 데이터 일관성
  - 데이터 독립성
  - 데이터 표준화
  - 데이터 보안 유지



#### 관계형 데이터베이스(RDB)

> 키와 값들의 간단한 관계를 표 형태로 정리한 데이터 베이스

- 스키마 : 데이터베이스에서 자료의 구조, 표현방법, 관계 등 전반적인 명세를 기술한 것

  | column  | datatype |
  | ------- | -------- |
  | id      | INT      |
  | name    | TEXT     |
  | address | TEXT     |
  | age     | INT      |

  

- 테이블 : 열(컬럼/필드)과 행(레코드/값)의 모델을 사용해 조직된 데이터 요소들의 집합

  | id   | name   | address | age  |
  | ---- | ------ | ------- | ---- |
  | 1    | 홍길동 | 제주    | 20   |
  | 2    | 김길동 | 서울    | 30   |
  | 3    | 박길동 | 독도    | 40   |

- 열 : 각 열에는 고유한 데이터 형식이 지정됨

  - ex) name이란 필드에 고객의 이름(TEXT) 정보가 저장됨

- 행 : 실제 데이터가 저장되는 형태

  - ex) 위 테이블에는 (1, 홍길동, 제주, 20)과 같은 형태로 3명의 고객정보가 저장되어 있음

- 기본키 : 각 행의 고유 값

  - 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정 시 주요하게 활용됨



#### 관계형 데이터베이스 관리 시스템(RDBMS)

> 관계형 모델을 기반으로 하는 데이터베이스 관리시스템

- SQLite : 서버가 아닌 파일 형식으로 응용프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스
  - Data Type
    - NULL
    - INTEGER
    - REAL
    - TEXT
    - BLOB : 입력된 그대로 정확히 저장된 데이터(별다른 타입 없이 저장)
  - Type Affinity : 특정 컬럼에 저장하도록 권장하는 데이터 타입
    - INTEGER
    - TEXT
    - BLOB
    - REAL
    - NUMERIC



## SQL

> 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적 프로그래밍 언어

#### 분류

- DDL(Data Definition Language) - 데이터 정의 언어
  - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어
  - CREATE, DROP, ALTER 등
- DML(Data Manipulation Language) - 데이터 조작 언어
  - 데이터를 저장, 조회, 수정, 삭제 등 하기 위한 명령어
  - INSERT, SELECT, UPDATE, DELETE
- DCL(Data Control Language) - 데이터 제어 언어
  - 데이터베이스 사용자의 권한 제어를 위해 사용하는 명령어
  - GRANT, REVOKE, COMMIT, ROLLBACK



## Database 생성

> `.`으로 시작하는 명령어는 SQLite에서 데이터베이스를 조금 더 편리하게 다루기 위해 제공하는 명령어로, SQL 문법에 속하지 않는다

- 데이터베이스 생성 : 해당하는 데이터베이스 파일이 있으면 콘솔로 열고, 없다면 새로 생성한 후 콘솔로 연다

  ```bash
  $ sqlite3 tutorial.sqlite3
  sqlite> .database
  ```

- CSV 파일을 table로 만들기

  ```bash
  sqlite> .mode csv
  sqlite> .import hellodb.csv examples # CSV 파일 불러오기
  sqlite> .tables
  examples
  ```

- SELECT 확인 및 터미널 view 변경

  ```bash
  sqlite> SELECT * FROM examples;
  # 1, "길동", "홍", 600, "충청도", 010-0000-0000
  sqlite> .headers on
  sqlite> SELECT * FROM examples;
  # id, first_name, last_name, age, country, phone
  # 1, "길동", "홍", 600, "충청도", 010-0000-0000
  sqlite> .mode column
  sqlite> SELECT * FROM examples;
  # id first_name last_name age country phone
  # -- ---------- --------- --- ------- -------------
  # 1  길동          홈        600 충청도     010-0000-0000
  ```

  

## 테이블 생성 및 삭제

> [SQLite3 공식문서](https://sqlite.org/datatype3.html)
>
> sql 파일에서 주석처리 :  `--` 



#### 테이블 생성(CREATE)

```sql
CREATE TABLE classmates (
  id INTEGER PRIMARY KEY,
  name TEXT
);
```



#### 테이블 및 schema 조회 명령어

```bash
sqlite> .tables			# 테이블 목록 조회
sqlit> .schema table	# 특정 테이블 스키마 조회
```



#### 테이블 제거(DROP)

```sql
DROP TABLE classmates;
```

```bash
sqlite> DROP TABLE classmates;
sqlite> .tables
examples
```





## SQL에서의 CRUD

#### CREATE - INSERT(추가)

```sql
INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2, ...);

INSERT INTO classmates VALUES (값1, 값2, 값3); -- 모든 열에 데이터가 있는 경우 --
```

- 예제

  > 1. classmates 테이블에 이름이 홍길동이고 나이가 23인 데이터 넣기
  > 2. 이름이 홍길동이고, 나이가 30이고, 주소가 서울인 데이터 넣기

  ```sql
  INSERT INTO classmates (name, age) VALUES ('홍길동', 23);
  INSERT INTO classmates VALUES ('홍길동', 30, '서울');
  ```

- 그 외 알아두어야할 점

  - SQLite에서는 따로 PRIMARY KEY 속성의 컬럼을 작성하지 않으면 값이 자동으로 증가하는 PK 옵션을 가진 rowid 컬럼을 정의

    ```bash
    sqlite> SELECT * FROM classmates;
    홍길동|23|
    홍길동|30|서울
    ```

  - 위의 홍길동은 주소가 비어있는데 이것이 꼭 필요한 정보라면?

    - 공백으로 비워두면 안된다 => NOT NULL 설정 필요

    - 지우고 새로 만들기

      ```sql
      DROP TABLE classmates;
      CREATE TABLE classmates (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INT NOT NULL,
        address TEXT NOT NULL
      )
      ```

      - INSERT 하면?

        ```sql
        INSERT INTO classmates VALUES ('홍길동', 30, '서울');
        # Error: table classmates has 4 columns but 3 values were supplied
        ```

        - 해결 방법

          1. id를 포함한 모든 value 작성

             ```sql
             INSERT INTO classmates VALUES (1, '홍길동', 30, '서울');
             ```

          2. 각 value에 맞는 column들을 명시적으로 작성

             ```sql
             INSERT INTO classmates (name, age, address) VALUES ('홍길동', 30, '서울');
             ```

  - 한번에 INSERT하기

    ```sql
    INSERT INTO classmates VALUES
    ('홍길동', 30, '서울'),
    ('김철수', 30, '대전'),
    ('이싸피', 26, '광주'),
    ('박삼성', 29, '구미'),
    ('최전자', 28, '부산');
    ```



#### READ - SELECT(조회)

> 예시는 위에서 한번에 INSERT한 것 기준

```sql
-- 모든 컬럼 가져오기 --
SELECT * FROM table;

-- 특정 컬럼 가져오기 --
SELECT 컬럼1, 컬럼2 FROM 테이블이름;
SELECT rowid, name FROM classmates; -- 1, 홍길동 ~ 5, 최전자가 출력될 것 --


-- LIMIT: 원하는 개수(num)만큼 가져오기 --
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자;
SELECT rowid, name FROM classmates LIMIT 1; -- 1, 홍길동이 출력될 것 --

-- OFFSET: 특정 위치에서부터 가져올 때(맨 위부터 num만큼 떨어진 값부터 가져옴) --
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 LIMIT 숫자 OFFSET 숫자;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2; -- 3, 이싸피가 출력될 것 --

-- WHERE: 조건을 통해 값 가져오기 --
SELECT 컬럼1, 컬럼2, ... FROM 테이블이름 WHERE 조건;
SELECT rowid, name FROM classmates WHERE address='서울'; -- 1, 홍길동이 출력될 것 --

-- DISTINCT: 중복없이 가져오기 --
SELECT DISTINCT 컬럼 FROM 테이블이름;
SELECT DISTINCT age FROM classmates; -- 30, 26, 29, 28이 출력될 것 --
```



#### DELETE(삭제)

```sql
DELETE FROM 테이블이름 WHERE 조건;

ex)
DELETE FROM classmates WHERE rowid=5; -- id가 5인 데이터 삭제 --
```

- 다시 데이터를 추가하면 id를 재사용한다(django와의 차이점)

- 재사용 없이 다음 행 값을 사용하게 하려면?

  - 테이블 생성 단계에서 AUTOINCREMENT 설정

    ```sql
    CREATE TABLE 테이블이름 (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      ...
    );
    ```



#### UPDATE(수정)

```sql
UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2, ... WHERE 조건;

ex)
UPDATE classmates SET name='홍길동', address='제주' WHERE rowid=5; -- 다섯 번째 데이터의 이름이 홍길동으로, 주소는 제주로 바뀔 것 --
```



#### 정리

| 구문 | 예시   |                                                              |
| ---- | ------ | ------------------------------------------------------------ |
| C    | INSERT | INSERT INTO 테이블이름 (컬럼1, 컬럼2, ...) VALUES (값1, 값2); |
| R    | SELECT | SELECT * FROM 테이블이름 WHERE 조건;                         |
| U    | UPDATE | UPDATE 테이블이름 SET 컬럼1=값1, 컬럼2=값2 WHERE 조건;       |
| D    | DELETE | DELETE FROM 테이블이름 WHERE 조건;                           |



#### WHERE문 심화

- users 테이블에서 age가 30 이상인 유저의 모든 컬럼 정보 조회

  ```sql
  SELECT * FROM users WHERE age >= 30;
  ```

- users 테이블에서 age가 30 이상인 유저의 이름만 조회

  ```sql
  SELECT first_name FROM users WHERE age >= 30;
  ```

- users 테이블에서 age가 30 이상이고 성이 '김'인 사람의 나이와 성만 조회

  ```sql
  SELECT age, last_name FROM users WHERE age >= 30 and last_name='김';
  ```

  

## 심화 SQL문

#### SQLite Aggregate Functions

- COUNT : 레코드 값들의 개수 반환

  ```sql
  -- users 테이블의 레코드 총 개수 조회 --
  SELECT COUNT(*) FROM users;
  ```

- AVG : 레코드 값들의 평균값 반환

  ```sql
  -- users 테이블의 30세 이상인 사람들 평균 나이 --
  SELECT AVG(age) FROM users WHERE age>=30;
  ```

- MAX : 레코드 값들의 최대값 반환

  ```sql
  -- 계좌 잔액(balance)이 가장 높은 사람과 그 액수 조회 --
  SELECT name, MAX(balance) FROM users;
  ```

- MIN : 레코드 값들의 최소값 반환

- SUM : 레코드 값들의 합 반환



#### LIKE

> 두 가지 와일드카드(`%`, `-`)와 함께 동작

- `-` : 반드시 이 자리에 한 개의 문자가 존재해야 한다

  ```sql
  -- 20대인 사람들만 가져올 때 --
  SELECT * FROM users WHERE age LIKE '2_';
  ```

- `%` : 이 자리에 문자열이 0개 이상이다

  ```sql
  -- 지역번호가 02인 사람만 가져올 때 --
  SELECT * FROM users WHERE phone LIKE '02-%';
  ```

- 두 개를 조합하여 사용 가능

  ```sql
  -- 핸드폰 중간 번호가 4자리이면서 511로 시작되는 사람들 --
  SELECT * FROM users WHERE phone LIKE '%-511_-%'
  ```

  ```sql
  -- 2로 시작하고 적어도 3자리인 값 --
  ... '2_%_%'
  ... '2__%'
  ```



#### ORDER BY

> 특정 컬럼을 기준으로 데이터를 정렬해서 조회

- ASC : 오름차순

  ```sql
  -- 나이, 성 순으로 오름차순 정렬하여 상위 10개만 조회 --
  SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
  ```

- DESC : 내림차순

  ```sql
  -- 계좌 잔액 순으로 내림차순 정렬하여 해당 유저의 성과 이름을 10개만 조회 --
  SELECT last_name, first_name FROM users ORDER BY balance DESC LIMIT 10;
  ```



#### GROUP BY

> 지정된 기준에 따라 행 세트를 그룹으로 결합(데이터를 요약할 때 주로 사용)

```sql
SELECT 컬럼1, aggregate_function(컬럼2) FROM 테이블 GROUP BY 컬럼1, 컬럼2;
```

- 예시

  ```sql
  -- users에서 각 성씨가 몇 명씩 있는지 조회 --
  SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
  -- 컬럼 명 바꿔서 조회 --
  SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
  ```



#### ALTER

- 테이블명 변경

  ```SQL
  ALTER TABLE 기존테이블명 RENAME TO 새로운테이블명;
  ```

- 새로운 컬럼 추가

  ```sql
  ALTER TABLE 테이블이름 ADD COLUMN 컬럼이름 데이터타입;
  -- 예시 --
  ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
  -- 결과 --
  # Error: Cannot add a NOT NULL column with default value NULL
  ```

  - 이유 : 새로 추가할 필드에 대한 정보가 없어서

  - 해결 방법

    - NOT NULL 설정 없이 추가하기

      ```sql
      ALTER TABLE news ADD COLUMN created_at TEXT;
      ```

    - 기본 값(DEFAULT 설정하기)

      ```sql
      ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목':
      ```

- 참고 : 장고에서 테이블 열을 추가하려면? 새로운 표를 만들고 원래있던 표를 지우고 새로운 표의 이름을 바꾸는 방식