# JavaScript기초2

## 함수

#### 함수 선언식

> 함수 이름과 함께 정의하는 방식

- 함수의 이름, 매개변수, body로 구성

```javascript
function name(args) {
    ...
}
```

```javascript
function add(num1, num2) {
    return num1 + num2
}

add(1, 2)
```



#### 함수 표현식

> 함수를 표현식 내에서 정의하는 방식

- 함수 이름을 생략하고 익명 함수(이름이 없는 함수)로 정의 가능
- 함수의 이름(생략 가능), 매개변수, body로 구성

```javascript
const name = function (args) {
    ...
}
```

```javascript
const add = function (num1, num2) {
    return num1 + num2
}

add(1, 2)
```

- `=` 뒤에 기본 인자 선언 가능

  ```javascript
  const greeting = function (name = 'Anonymous') {
      return `Hi, ${name}`
  }
  
  greeting()
  ```

- 매개변수와 인자의 개수가 달라도 사용 가능하다

  - 매개변수 < 인자의 개수

    ```javascript
    const args = function(arg1, arg2) {
        return [arg1, arg2]
    }
    
    args(1, 2, 3) // [1, 2]
    ```

  - 매개변수 > 인자의 개수

    ```javascript
    const args = function(arg1, arg2, arg3) {
        return [arg1, arg2, arg3]
    }
    
    args(1, 2) // [1, 2, undefined]
    ```

- Rest operator

  - `...` 사용 => 함수가 정해지지 않은 수의 매개변수를 배열로 받음

    ```javascript
    const restOpr = function (arg1, arg2, ...restArgs) {
        return [arg1, arg2, restArgs]
    }
    
    restArgs(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    restArgs(1, 2) // [1, 2, []]
    ```

- Spread operator

  - `...` 사용 => 배열 인자를 전개하여 전달 가능
  
    ```javascript
    const spreadOpr = function (arg1, arg2, arg3) {
        return arg1 + arg2 + arg3
    }
    const numbers = [1, 2, 3]
    spreadOpr(...numbers) // 6
    ```



#### 선언식 vs 표현식

- 공통점
  - 데이터 타입이 function으로 동일하다
  - 이름, 매개변수, body로 구성
- 차이점
  - 함수 표현식
    - 익명 함수 가능
    - 호이스팅 X
      - 함수 정의 전에 호출 시 에러가 발생함
      - 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따른다
    - Airbnb Style Guide 권장 방식



## Arrow Function

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 매개변수가 단 하나 뿐이라면 `()`도 생략 가능
- body가 표현식 하나라면, `{}`과 `return`도 생략 가능

```javascript
const arrow1 = function (name) {
    return `hello, ${name}`
}

// 1. function 키워드 생략 가능
const arrow2 = (name) => { return `hello, ${name}`}

// 2. 매개변수가 1개일 경우에 () 생략 가능
const arrow3 = name => { return `hello, ${name}`}

// 3. 함수 body가 표현식 1개일 경우 {} & return 삭제
const arrow4 = name => `hello, ${name}`
```

```javascript
const add = (a, b) => a + b
```



## String

#### 메서드

- str.includes(value)

  - 문자열에 value가 존재하는지 판별 후 참 또는 거짓 반환

- str.split(value)

  - value가 없을 경우 기존 문자열을 배열에 담아 반환

  - 빈 문자열일 경우 각 문자로 나눈 배열을 반환

  - 기타 문자열일 경우 해당 문자열로 나눈 배열을 반환

    ```javascript
    const str = 'a cup'
    
    str.split() // ['a cup']
    str.split('') // ['a', ' ', 'c', 'u', 'p']
    str.split(' ') // ['a', 'cup']
    ```

- replace

  - str.replace(from, to)
    - 문자열에 from값이 존재할 경우 1개만 to값으로 교체하여 반환
  - str.replaceAll(from, to)
    - 문자열에 from값이 존재할 경우 모두 to값으로 교체하여 반환

- trim

  - str.trim()
    - 문자열 시작과 끝의 모든 공백문자 제거한 문자열 반환
  - str.trimStart()
    - 문자열 시작의 공백문자 제거한 문자열 반환
  - str.trimEnd
    - 문자열 끝의 공백문자 제거한 문자열 반환



## Arrays

- 키와 속성들을 담고 있는 참조 타입의 **객체**
- 순서를 보장
- 주로 대괄호를 이용해 생성하고, 0을 포함한 야으이 정수 인덱스로 특정 값에 접근 가능



#### 메서드

- arr.reverse()

  - 원본 배열의 요소들 순서를 반대로 정렬

- arr.push()

  - 배열의 가장 뒤에 요소 추가

- arr.pop()

  - 배열의 마지막 요소 제거

- arr.unshift()

  - 배열의 가장 앞에 요소 추가

- arr.shift()

  - 배열의 첫번째 요소 제거

- arr.includes(value)

  - 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

- arr.indexOf(value)

  - 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
  - 해당 값이 없으면 -1 반환

- arr.join([seperator])

  - 배열의 모든 요소 연결하여 반환
  - seperator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

- Spread operator

  - 배열 내부에서 배열 전개 가능

  - 얕은 복사에 활용 가능

    ```javascript
    const arr = [1, 2, 3]
    const newarr = [0, ...arr, 4]
    ```



#### 심화 메서드(중요)

- array.forEach(callback(element[, index[, array]]))

  - 배열의 각 요소에  대해 콜백 함수를 한 번씩 실행
  - **반환 값이 없다**
  - 반복문 사용시 가장 많이 사용된다

  ```javascript
  const fruits = ['딸기', '수박', '사과', '체리']
  
  fruits.forEach((fruit, index) => {console.log(fruit, index)}) // 과일들이 차례로 나올 것
  ```

- array.map(callback(element[, index[, array]]))

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - **함수의 반환 값을 요소로 하는** 새로운 배열 반환

    ```javascript
    const rectangles = [
        {'width': 30, 'height': 20}, 
        {'width': 10, 'height': 20}
    ]
    // 넓이
    console.log(rectangles.map(x => x.width * x.height))
    console.log(rectangles.map(function (x) {return x.width + x.height}))
    ```

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    const doubleNums = numbers.map((num) => {return num*2})
    ```

- array.filter(callback(element[, index[, array]]))

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - **함수의 반환 값이 참인 요소들을** 모아 새로운 배열 반환

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    numbers.filter((num, index) => {return num % 2})
    numbers.filter(function (num) {return num % 2})
    ```

- array.reduce(callback(acc, element[, index[, array]])[, initialValue])

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 함수의 반환 값들을 **하나의 값에 누적** 후 반환

  - acc : 누적되는 변수

  - initialValue : 최초 함수 호출 시 acc에 할당되는 값

    ```javascript
    const numbers = [1, 2, 3, 4, 5]
    
    numbers.reduce((acc, num) => {return acc + num})
    numbers.reduce(function (acc, num) {return acc + num})
    ```

- array.find((element, index, array))

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
  - 함수의 반환 값이 참이면 **조건을 만족하는 첫번째 요소** 반환
  - 찾는 값이 배열에 없으면 undefined 반환

- array.some(callback(element[, index[, array]]))

  - 배열의 요소 중 하나라도 주어진 반별 함수를 통과하면 참을 반환

- array.every(callback(element[, index[, array]]))

  - 배열의 모든 요소가 주어진 반별 함수를 통과하면 참을 반환



## 객체(Objects)

> 속성의 집합이며, 중괄호 내부에 key와 value 쌍으로 표현

- key는 문자열 타입만, value는 모든 타입이 가능하다
- 메서드 : 객체의 속성이 참조하는 함수



#### 관련 문법

- 속성명 축약 (shorthand)

  ```javascript
  const url = 'https://test.com'
  const data = { message: 'Hello World!' }
  
  const request = { url: url, data: data }
  // 축약하면?
  const request = { url, data }
  ```

- 메서드명 축약 (shorthand)

  - 메서드 선언시 function 키워드 생략 가능

- 계산된 속성 (computed property name)

  - 객체 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

    ```javascript
    const key = 'regions'
    const value = ['서울', '대전', '구미']
    
    const ssafy = {
        [key]: value,
    }
    
    console.log(ssafy)
    console.log(ssafy.regions)
    ```

- 구조 분해 할당 (destructing assignment)

  - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있다

  ```javascript
  const data = {
      username: 'myName',
      password: 'myPassword',
      email: 'my@mail.com',
  }
  
  const username = data.username
  const password = data.password
  const email = data.email
  console.log(username, password, email)
  // 구조 분해하면?
  const { username, password, email } = data
  console.log(username, password, email)
  ```

- Spread operator

  - 객체 내부에서 객체 전개 가능

  ```javascript
  const defaultColors = ['red', 'green', 'blue']
  const palette = ['navy', 'black', 'gold', 'white', ...defaultColors]
  ```

  ```javascript
  const info = { name: 'Tom', age: 30 }
  const fullinfo = {isMarried: true, balance: 3000, ...info}
  ```

- JSON

  - key-value 쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
  - 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 메서드
    - JSON.parse()
      - JSON => 자바스크립트 객체
    - JSON.stringify()
      - 자바스크립트 객체 => JSON



## this

- 실행 문맥에 따라 다른 대상을 가리킴
  - class 내부의 생성자 함수
  - 메서드
  - 위의 두가지 경우를 제외하면 모두 최상위 객체(window)를 가리킴
- 함수 내부에 this 키워드가 존재할 경우
  - 화살표 함수와 function 키워드로 선언한 함수가 다르게 동작
- 함수 내부에 this 키워드가 존재하지 않을 경우
  - 화살표 함수와 function 키워드로 선언한 함수가 똑같이 동작

```javascript
function getFullName() {
    return this.firstName + this.lastName
}

const me = {
    firstName: 'John',
    lastName: 'Doe',
    getFullName: getFullName,
}

const you = {
    firstName: 'Jack',
    lastName: 'Lee',
    getFullName: getFullName,
}

me.getFullName()	// JohnDoe (this === me)
you.getFullName()	// JackLee (this === you)
getFullName()		// NaN (this === window)
```



## lodash

> 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리

- 함수 예시

  - reverse, sortBy, range, random, cloneDeep

- 사용법

  ```html
  <body>
    <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
    <script>
    ...
  ```
