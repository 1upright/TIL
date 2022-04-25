# JavaScript기초

## Browser

- DOM 조작(Document Object Model)
  - 문서 조작
  - 해석
    - 파싱 : 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
  - 조작
    - 콘솔 창에서 조작 가능
- BOM 조작(Browser Object Model)
  - navigator, screen, location, frames, history, XHR
- JavaScript Core(ECMAScript)
  - Data Structure(Object, Array), Conditional Expression, Iteration
  - ECMA : 정보 통신에 대한 표준을 제정하는 비영리 표준화 기구
  - ECMAScript는 ECMA-262 규격에 따라 정의한 언어
  - ECMAScript6는 ECMA에서 제안하는 6번째 표준 명세



## 스타일

- 세미콜론 써도 되고 안써도 되는데 요즘은 안쓰는 추세 => 수업에서 계속 안쓸 예정
- 수업에서는 Airbnb Style Guide 중심으로 사용
- 카멜 케이스(camelCase) : 변수, 객체, 함수
- 파스칼 케이스(PascalCase) : 클래스, 생성자
- 대문자 스네이크 케이스(SNAKE_CASE) : 상수



## 변수 선언

- let

  - 재할당할 예정인 변수 선언시 사용
  - 변수 재선언 불가능

- const

  - 재할당할 예정이 없는 변수 선언시 사용
  - 변수 재선언 불가능

- var

  - 재선언, 재할당 모두 가능

  - 호이스팅되는 특성으로 인해 예기치 못한 문제 발생이 가능해서 ES6 이후부터는 var 대신 const와 let을 사용하는 것이 권장된다

    - 호이스팅 : 변수를 선언 이전에 참조할 수 있는 현상, 변수 선언 이전의 위치에서 접근시 undefined를 반환
    - var로 쓴 것이 호이스팅되면 코드가 복잡해질 때 안정성이 떨어져서 사용이 지양됨

  - 함수 스코프

    - 함수의 중괄호 내부를 가리킴

    - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

      ```javascript
      function foo() {
          var x = 5
          console.log(x) // 5
      }
      
      console.log(x) // ReferenceError: x is not defined
      ```



## 출력

> console.log(x)



## 데이터 타입

- 원시 타입 : 객체가 아닌 기본 타입
  - 숫자 타입
    - 양의 정수, 음의 정수, 실수
    - 거듭제곱(ex. 2.99e8)
    - 양의 무한대, 음의 무한대(Infinity, -Infinity)
    - 산술 연산 불가(NaN)
  - 문자열 타입
    - &{ expression }으로 표현식 삽입 가능
  - undefined
    - 변수의 값이 없음을 나타내는 데이터 타입
    - 직접 값을 할당하지 않으면 자동으로 undefined가 할당됨
  - null
    - 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입
    - 개발자가 의도적으로 필요한 경우 할당
  - Boolean
    - 논리적 참 또는 거짓을 나타내는 타입
- 참조 타입 : 객체 타입의 자료형



## 연산자

- 할당 연산자

  ```javascript
  x += 10
  x -= 10
  x *= 10
  x /= 10
  x++ // x += 1과 동일하게 연산되지만 Airbnb Style Guide에서는 +=와 같이 더 분명하게 적을 것을 권장
  x-- // 마찬가지
  ```

- 비교 연산자

  - 피연산자들 비교하여 boolean값으로 반환

- 동등 비교 연산자(`==`)

  - 예상치 못한 결과가 발생할 수 있어 거의 사용하지 않음

- 일치 비교 연산자(`===`)

  - 두 피연산자가 같은 값으로 평가되는지 비교하여 boolean값으로 반환
  - 엄격한 비교 : 두 비교 대상의 타입과 값 모두 같은지 비교

- 논리 연산자

  - `&&` : and 연산
  - `||` : or 연산
  - `!` : not 연산

- 삼항 연산자

  - 세 개의 피연산자를 사용하여 조건에 따라 값 반환

    ```javascript
    result = a > b ? 'a가 더 큽니다' : 'b가 더 크거나 같습니다'
    console.log(result)
    ```



## 조건문

- 'if' statement

  - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단

    ```javascript
    const nation = 'Korea'
    
    if (nation === 'Korea') {
        console.log('안녕')
    } else if (nation === 'France') {
        console.log('Bonjour!')
    } else {
        console.log('Hi')
    }
    ```

- 'switch' statement

  - 조건 표현식의 결과값이 어느 값에 해당하는지 판별

  - break를 안써주면 그 위치부터 아래 것들이 다 출력됨

    ```javascript
    switch(nation) {
        case 'Korea': {
            console.log('안녕')
            break
        }
        case 'France' {
            console.log('Bonjour!')
            break
    	}
    	default: {
            consol.log('Hello!')
        }
    }
    ```

    

## 반복문

- while : 조건문이 참인 동안 반복 시행

  ```javascript
  let i = 0
  
  while (i < 6) {
      console.log(i)
      i += 1
  }
  ```

- for : 세미콜론으로 구분되는 세 부분으로 구성

  - initialization : 최초 반복문 진입 시 1회만 실행
  - condition : 매 반복 시행 전 평가되는 부분
  - expression : 매 반복 시행 이후 평가되는 부분

  ```javascript
  for (let i = 0; i < 6, i++) {
      console.log(i)
  }
  ```

- for...in : 객체(object)의 속성(key)들을 순회할 때 사용, 배열도 순회 가능하지만 권장되지 않음

  - 객체 순회에 적합

  ```javascript
  const capitals = {
      korea: 'seoul',
      france: 'paris',
      usa: 'washington'
  }
  
  for (let capital in capitals) {
      console.log(capital)
  }
  ```

- for...of : 반복 가능한 객체를 순회하며 값을 꺼낼 때 사용

  - 배열 순회에 적합

  ```javascript
  const fruits = ['딸기', '바나나', '메론']
  
  for (let fruit of fruits) {
      fruit = fruit + '!'
      console.log(fruit)
  }
  ```