# AsynchoronousJavaScript

## AJAX

> Asynchronous JavaScript And XML(비동기식 JavaScript와 XML)

- 서버와 통신하기 위해 XMLHttpRequest 객체 활용
- 특징
  - JSON, XML, HTML 그리고 일반 텍스트 형식 등을 포함한 다양한 포맷을 주고 받을 수 있다
  - 비동기성 : 페이지 전체를 reload 하지 않고서도 수행된다
  - 이 두가지 특징을 활용해 가능한 작업
    - 페이지 새로 고침 없이 서버에 요청
    - 서버로부터 데이터를 받고 작업을 수행



#### XMLHttpReqeust

- 서버와 상호작용하기 위해 사용되며 전체 페이지의 새로고침 없이 데이터를 받아올 수 있음

- 사용자의 작업을 방해하지 않으면서 페이지 일부를 업데이트 할 수 있음

- AJAX 프로그래밍에 주로 사용

- XML 뿐 아니라 모든 종류의 데이터를 받아올 수 있음

- 생성자 : XMLHttpRequest()

  ```javascript
  const request = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/1/'
  
  request.open('GET', URL)
  request.send() // 이 응답을 기다리지 않고
  
  const todo = request.response
  console.log(`data: ${todo}`) // 여기가 먼저 실행되기 때문에 console에 todo 데이터가 출력되지 않는다
  ```



## Asynchronous JavaScript

- 동기식
  - 순차적, 직렬적 Task 수행
  - 요청을 보낸 후 응답을 받아야만 다음 동작이 이루어짐
- 비동기식
  - 병렬적 Task 수행
  - 요청을 보낸 후 응답을 기다리지 않고 다음 동작이 이루어짐
  - JavaScript는 single threaded이기 때문에
    - 컴퓨터가 여러 개의 CPU를 가지고 있어도 main thread라 불리는 단일 스레드에서만 작업 수행
    - 즉, JavaScript는 이벤트를 처리하는 Call Stack이 하나인 언어
      1. 즉시 처리하지 못하는 이벤트들을 다른 곳(Wev API)으로 보내서 처리
      2. 처리된 이벤트들은 처리된 순서대로 대기실(Task Queue)에 줄을 세우고
      3. Call Stack이 비면 담당자(Event Loop)가 대기 줄에서 가장 오래된 이벤트를 Call Stack으로 보냄



#### 왜 Asynchronous 방식인가?

- 큰 데이터를 동반하는 앱에서 동기식 코드를 사용한다면 데이터를 불러오기까지 앱이 멈춘 것처럼 보일 것이고 그동안  화면이 멈추고 응답하지 않는 것 같은 사용자 경험을 제공할 수 있기 때문
- "human-centered design with UX"
  - 인간 중심으로 설계된 사용자 경험을 위해



#### Concurrency model

> Event loop를 기반으로 하는 동시성 모델(Concurrency model)

- Call Stack

  - 요청이 들어올 때마다 해당 요청을 순차적으로 처리하는 Stack(LIFO) 형태의 자료 구조

- Web API

  - JavaScript 엔진이 아닌 브라우저 영역에서 제공하는 API
  - **setTimeout() 등 시간 관련, DOM events, AJAX로 데이터를 가져오는 시간이 소요되는 일**들을 처리
    - 이들은 비동기 방식으로 동작하게 되며, 언제 끝날지 모른다는 공통점을 가짐

- Task Queue

  - 비동기 처리된 callback 함수가 대기하는 Queue(FIFO) 형태의 자료 구조
  - main thread가 끝난 후 실행되어 후속 JavaScript 코드가 차단되는 것을 방지

- Event Loop

  - Call Stack이 비어 있는지 확인
  - 비어 있는 경우 Task Queue에서 실행 대기 중인 callback 함수가 있는지 확인
  - Task Queue에서 대기 중인 callback 함수가 있다면 가장 앞에 있는 callback 함수를 Call Stack으로 push

- 예시

  ```javascript
  console.log('HI')
  
  setTimeout(function saffy() {
      console.log('SSAFY')
  })
  
  console.log('BYE')
  ```

  1. "Hi 출력"이 Call Stack에 요청된 후 처리됨
  2. "3초 후 SSAFY 출력"이 Call Stack에 요청된 후 Web API에 넘겨짐
  3. "BYE 출력"이 Call Stack에 요청된 후 처리됨
  4. 3초 후 "SSAFY 출력"이 Task Queue에 넘겨짐
  5. Call Stack이 비어 있으므로 "SSAFY 출력"이 Call Stack에 요청된 후 처리됨

- 이는 0초의 delay를 가진 요청이어도 같은 순서로 이루어질 것

  - delay는 JavaScript가 요청을 처리하는데 필요한 최소 시간일 뿐 대기 중인 메시지의 모든 코드가 완료될 때까지 대기해야 하는 것은 마찬가지



#### 순간적인 비동기 처리하기

> 어떤 이벤트가 먼저 처리되느냐가 중요하기 때문에 실행 순서가 불명확하다. 이를 해결할 수 있는 방법은?

1. Async callbacks
   - 백그라운드에서 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
2. promise-style
   - XMLHttpRequest 객체를 사용하는 구조보다 조금 더 현대적인 버전



## Callback function

- 다른 함수에 인자로 전달된 함수

- 외부 함수 내에서 호출되어 일종의 루틴 또는 작업을 완료

- 동기식, 비동기식 모두 사용됨

- 비동기 작업이 완료된 후 코드 실행을 계속하는 데 사용되는 경우를 비동기 콜백(asynchronous callback)이라고 함

- JavaScript의 함수는 "일급 객체"니깐!

- 사용 예시

  ```javascript
  // JavaScript
  
  const btn = document.querySelector('button')
  
  btn.addEventListener('click', function () { // 여기서 함수
      alert('Completed')
  })
  ```

  ```python
  # Python
  
  def add_one(number):
      return number+1
  
  print(map(add_one, numbers)) # 여기서 add_one 함수
  ```

  ```python
  # Django(urls.py)
  
  from django.urls import path
  from . import views
  
  urlpatterns = [
      path('', views.index), # 여기서 views.index
  ]
  ```



#### Async callbacks

- 백그라운드에서 코드 실행을 시작할 함수를 호출할 때 인자로 지정된 함수
- 백그라운드 코드 실행이 끝나면 callback 함수를 호출하여 작업이 완료되었음을 알리거나, 다음 작업을 실행하게 할 수 있음
  - addEventListener()의 두 번째 매개변수처럼
- callback 함수를 다른 함수의 인수로 전달할 때, 함수의 참조를 인수로 전달할 뿐이지 즉시 실행되지 않고, 함수의 body에서 "called back"됨
- 정의된 함수는 때가 되면 callback 함수를 실행



#### 왜 callback을 쓰는데?

- callback 함수는 명시적인 호출이 아닌 특정 루틴 혹은 action에 의해 호출되는 함수
- Django의 경우 "요청이 들어오면", event의 경우 "특정 이벤트가 발생하면"이라는 조건으로 함수를 호출할 수 있었던건 "Callback function" 개념 덕분이었다
- 비동기 로직을 수행할 때 callback 함수는 필수
  - 명시적인 호출이 아니라 해당 함수 내에서 "특정 시점"에 호출하는 것이 목표니까!



#### callback Hell

- 순차적인 연쇄 비동기 작업을 처리하기 위해 "callback 함수를 호출하고, 그 다음 callback 함수를 호출하고..."의 패턴이 지속적으로 반복될 수 밖에 없다
- 즉, 여러 개의 연쇄 비동기 작업을 할 때 마주하는 상황
- 이를 callback Hell(콜백 지옥) 혹은 pyramid of doom(파멸의 피라미드)이라고 함
- 해결 방법
  - 뻔한 방법들 : 코드의 깊이를 얕게, 모듈화, 모든 단일 오류 처리
  - **Promise callbacks**(Promise 콜백 방식 사용)



## Promise

#### Promise object

> 비동기 작업의 최종 완료 또는 실패를 나타내는 객체

- 성공(이행)에 대한 약속 : `.then()`
- 실패(거절)에 대한 약속 : `.catch()`



#### Promise method

- `.then(callback)`

  - 이전 작업이 성공했을 때 수행할 작업을 나타내는 callback 함수
  - 각 callback 함수는 이전 작업의 성공 결과를 인자로 전달받음
  - 성공했을 때의 코드를 callback 함수 안에 작성
  - 각각의 .then 블록은 서로 다른 promise를 반환
    - 즉 then()을 여러개 사용하여 연쇄적인 작업을 수행할 수 있음 => 여러 비동기 작업을 차례로 수행할 수 있음
    - 반환하는 내용이 다음 것이 전달 받는 인자가 된다

- `.catch(callback)`

  - .then이 하나라도 실패하면 동작(try-except문과 유사)
  - 이전 작업의 실패로 인해 생성된 error 객체는 catch 블록 안에서 사용 가능
  - .then()과 .catch() 모두 promise를 반환하기 때문에 chaining이 가능하다

- 둘다 반환 값이 반드시 있어야 한다

  - 없으면 callback 함수가 이전의 promise 결과를 받을 수 없음

- `.finally(callback)`

  - promise 객체를 반환
  - 결과와 상관없이 무조건 지정된 callback 함수가 실행
  - 어떠한 인자도 전달받지 않음(promise가 성공했는지 실패했는지 판단이 불가능하므로)
  - 무조건 실행되어야 하는 절에서 활용

- 예시

  ```javascript
  // callback Hell
  work1(function(result1) {
  	work2(result1, function(result2) {
  		work3(result2, function(result3) {
              console.log('최종 결과 : ' + result3)
          })
  	})
  })
  
  // Promise로 고치면?
  work1().then(function(result1) {
      return work2(result1)
  })
  .then(function(result2) {
      return work3(result2)
  })
  .then(function(result3) {
      console.log('최종 결과 : ' + result3)
  })
  .catch(failureCallback)
  ```

  

#### Promise가 보장하는 것

> Async callback 작성 스타일과 달리 Promise가 보장하는 특징

- callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음
- 비동기 작업이 성공하거나 실패한 뒤에 .then() 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작
- .then()을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음(Chaining)
  - 각각의 callback은 주어진 순서대로 하나하나 실행하게 되며 이 Chaining은 Promise의 가장 뛰어난 장점



## Axios

> 기존 AJAX 요청을 처리하는데 활용되던 "XHR"이라는 브라우저 내장 객체를 대신해 편리한 요청이 가능하도록 도움을 주는 Promise 기반의 클라이언트

```javascript
const URL = 'https://jsonplaceholder.typicode.com/todos/'

axios.get(URL)
	.then(function (response) {
        console.log(response)
        return response.data
	})
	.then(function (data) {
        return data.title
	})
	.then(function (title) {
        console.log(title)
	})
	.catch(function (error) {
        console.log(error)
	})
	.finally(function() {
        console.log('이건 무조건 실행됩니다')
	})
```

```javascript
const URL = 'https://jsonplaceholder.typicode.com/todos/'

axios.get(URL)  // Promise 리턴
// .then(res => res.data)
// .then(todo => todo.title)
// .then(title => console.log( title ))
    .then(res => console.log(res.data.title))
    .catch(err => {
        if (err.response.status === 404) {
            alert('그딴건 없다.')
    	}
	})
    .finally(() => console.log('어쨋든 끝!'))
```

- 만약 같은걸 XMLHttpRequest로 했다면?

  ```javascript
  const xhr = new XMLHttpRequest()
  const URL = 'https://jsonplaceholder.typicode.com/todos/'
  
  xhr.open('GET', URL)
  xhr.send()
  
  xhr.onreadystatechange = function (event) {
      if (xhr.readyState === XMLHttpRequest.DONE) {
          if (status === 0 || (status >= 200 && status < 400)) {
              const res = event.target.response
              const data = JSON.parse(res)
              console.log(data.title)
          } elif (status === 404) {
              alert('그딴건 없다.')
          }
      }
  }
  ```

  

## async & await

> ES8에서 등장한 비동기 코드를 작성하는 새로운 방법

- 기존 Promise 시스템 위에 구축된 Syntactic sugar
  - Promise 구조의 then chaining 제거
  - 비동기 코드를 좀 더 동기 코드처럼 표현
  - Syntactic sugar
    - 더 쉽게 읽고 표현할 수 있도록 설계된 프로그래밍 언어 내의 구문
    - 문법적 기능은 그대로 유지하되 사용자가 직관적으로 코드를 읽을 수 있게 만듦
  - then을 자유자재로 쓸 수 있을 때 쓰는 것을 추천

```javascript
const URL = 'https://dog.ceo/api'

function fetchDogImages() {
    axios.get(URL + '/breeds/list/all')
        .then(res => {
            const breedObj= res.data.message
            const breedArray = Object.keys(breedObj)
            const breed = breedArray[0]  // 아펜핀셔
            return axios.get(URL + `/breed/${breed}/images`)
    	})
        .then(res => console.log(res.data))
        .catch(err => console.error(err))
}

fetchDogImages()
```

