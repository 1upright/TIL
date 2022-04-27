# JavaScript심화

## DOM 조작

> 선택(Select) => 변경(Manipulation)

#### 상속 구조

- EventTarget => Node => Element/Document => HTMLElement
- EventTarget
  - Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
- Node
  - 여러 가지 DOM 타입들이 상속하는 인터페이스
- Element
  - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  - 부모인 Node와 그 부모인 EventTarget의 속성을 상속
- Document
  - 브라우저가 불러온 웹 페이지를 나타냄
  - DOM 트리의 진입점 역할을 수행
- HTMLElement
  - 모든 종류의 HTML 요소
  - 부모 element의 속성 상속



#### 메서드 - DOM 선택

- document.querySelector(selector)
  - 제공한 선택자와 일치하는 element 하나 선택
  - 제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환(없다면 null)
- document.querySelectorAll(selector)
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 유효한 CSS selector를 문자열로 받음
  - 지정된 셀렉터에 일치하는 NodeList를 반환
- 그외
  - getElementById(id)
  - getElementByTagName(name)
  - getElemntByClassName(names)
- querySelector(), querySelectorAll()
  - id, class, tag 선택자 등 모두 사용이 가능해 더 구체적이고 유연하게 선택할 수 있기 때문에 사용
  - querySelector()는 단일 element, querySelectorAll()는 NodeList를 반환



- HTMLCollection
  - name, id, index 속성으로 각 항목에 접근 가능
- NodeList
  - index로만 각 항목에 접근 가능
  - HTMLCollection과는 달리 배열에서 사용하는 forEach 메서드 및 다양한 메서드 사용 가능
- 둘 다 Live Collection으로 DOM의 변경사항을 실시간으로 반영하지만 querySelectorAll()에 의해 반환되는 NodeList는 Static Collection으로 실시간으로 반영되지 않음
  - Live Collection
    - 문서가 바뀔 때 실시간으로 업데이트됨
    - DOM의 변경사항을 실시간으로 collection에 반영
    - ex) HTMLCollection, NodeList
  - Static Collection
    - DOM이 변경되어도 collection 내용에는 영향을 주지 않음
    - querySelectorAll()의 반환 NodeList만 static collection



#### 메서드 - DOM 변경

- document.createElement()
  - 작성한 태그명의 HTML 요소를 생성하여 반환
- Element.append()
  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  - 여러 개의 Node 객체, DOMString을 추가할 수 있음
  - 반환 값이 없음
- Node.appendChild()
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입(Node만 추가 가능)
  - 한번에 하나의 Node만 추가할 수 있음
  - 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동
- ParentNode.append() vs Node.appendChild()
  - append()는 DOMString 객체 추가할 수 있지만, appendChild()는 Node 객체만 허용
  - append()는 반환 값이 없지만, appendChild()는 추가된 Node 객체 반환
  - append()는 여러 Node 객체와 문자열을 추가할 수 있지만
  - appendChild()는 하나의 Node 객체만 추가할 수 있음



- Node.innerText
  - Node 객체와 그 자손의 텍스트 컨텐츠를 표현
  - 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
- Element.innerHTML
  - 요소 내에 포함된 HTML 마크업을 반환
  - XSS 공격에 취약하므로 안 쓴다고 보면 됨
    - 공격자가 입력요소를 사용하여 웹 사이트 클라이언트 측 코드에 악성 스크립트를 삽입해 공격



##### 실습

```javascript
// ul 안에 새로운 '새로운 리스트 태그'라는 이름의 li를 집어 넣으려면?
const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')
newLiTag.innerText = '새로운 리스트 태그'
ulTag.append(newLiTag)
ulTag.append('문자열도 추가 가능')

// appendChild 버전으로
const ulTag = document.querySelector('ul')
const newLiTag = document.createElement('li')
newLiTag.innerText = '새로운 리스트 태그'
ulTag.appendChild(newLiTag)
ulTag.append('문자열은 추가 불가')
```



#### 메서드 - DOM 삭제

- ChildNode.remove()
  - Node가 속한 트리에서 해당 Node를 제거
- Node.removeChild()
  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  - Node는 인자로 들어가는 자식 Node의 부모 Node



##### 실습

```javascript
// 'my-id'라는 아이디로 된 태그 지우기
const myId = document.querySelector('#my-id')
myId.remove()

// ul 안의 li 지우기
const parent document.querySelector('ul')
const child document.querySelector('ul > li')
const removedChild = parent.removeChild(child)
console.log(removedChild)

// + 지운 후 맨 밑에 붙여 순서를 바꾼 것처럼 만드려면?
parent.append(child)
```



#### 메서드 - DOM 속성

- Element.setAttribute(name, value)
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신하고, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가
- Element.getAttribute(attributeName)
  - 해당 요소의 지정된 값(문자열) 반환
  - 인자(attibuteName)는 값을 얻고자 하는 속성의 이름



##### 실습

```javascript
// 'my-id'라는 아이디로 된 태그에 'my-class'라는 클래스를 넣고 싶다
const myId = document.queryselector('#my-id')
myId.setAttribute('class', 'my-class')

// 'my-class'라고 된 태그들의 'class'와 'style'에 지정된 값을 가져오자
const getAttr = document.querySelector('.my-class')
getAttr.getAtrribute('class')
getAttr.getAttribute('style')
```



## Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체

- 마우스 클릭이나 키보드 입력 등 사용자 행동으로 발생할 수 있음
- 특정 메서드를 호출하여 프로그래밍적으로도 만들어낼 수 있음

```markdown
~ 하면 ~ 한다
`클릭`하면 `경고창을 띄운`다
`특정 이벤트가 발생`하면 `할일을 등록`한다
```



#### addEventListener

- EventTarget.addEventListener()

  - 지정한 이벤트가 대상에 전달될 때마다 호출할 함수 설정
  - 이벤트를 지원하는 모든 객체를 대상으로 지정 가능

- target.addEventListener(type, listener[, options])

  - type : 반응할 이벤트 유형(대소문자 구분 문자열)

  - listener : 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체

    ```markdown
    `대상`에 `특정 이벤트`가 발생하면, `할 일`을 등록한다
    `EventTarget`.addEventListener(`type`, `listener`)
    ```

  - 실습

    ```javascript
    // myButton에 click이 발생하면 alertMessage 함수를 실행한다
    const alertMessage = function () {
        alert('메롱!!')
    }
    const myButton = document.querySelector('#my-button')
    myButton.addEventListener('click', alertMessage)
    
    
    // id:my-text-input인 myTextInput에 input이 발생하면 "input된 내용을 id:my-paragraph에 innerText하는 함수"를 실행한다
    const myTextInput = document.querySelector('#my-text-input')
    const myP = document.querySelector('#my-paragraph')
    
    myTextInput.addEventListener('input', function (event) {
        myP.innerText = event.target.value // event.target은 myTextinput이라고 볼 수 있다
    })
    
    
    // id:change-color-input인 colorInput에 input이 발생하면 "h2 태그의 스타일 중 color를 input된 color(red, yellow, crimson 등)으로 바꿔주는 함수"를 실행한다
    const h2Tag = document.querySelector('h2')
    const onColorInput = function (event) {
        const userInput = event.target.value
        h2Tag.style.color = userInput
    }
    const colorInput = document.querySelector('#change-color-input')
    
    colorInput.addEventListener('input', onColorInput)
    ```

  

#### Event 취소

- event.preventDefault()

- 현재 이벤트의 HTML 기본 동작을 작동하지 않게 중단시킴

  - 클릭 시 링크로 이동하는 a 태그, form 데이터를 전송하는 form 태그 등

- 실습

  ```javascript
  // checkbox 클릭이 안되도록
  const checkBox = document.querySelector('#my-checkbox')
  
  checkBox.addEventListener('click', function (event) {
      event.preventDefault()
      console.log(event)
  })
  
  // form의 submit을 누르면 써진 것들이 초기화되도록
  const formTag = document.querySelector('#my-form')
  
  formTag.addEventListener('submit', function (event) {
      console.log(event)
      event.preventDefault()
      event.target.reset()
  })
  
  // a 태그 링크 클릭이 안되도록
  const aTag = document.querySelector('#my-link')
  
  aTag.addEventListener('click', function (event) {
      console.log(event)
      event.preventDefault()
  })
  
  // scroll 안되도록
  document.addEventListener('scroll', function (event) {
      console.log(event)
      event.preventDefault()
  })
  ```



#### Event 종합 실습

```javascript
// 1. 사용자의 입력을 받아서 form이 제출(submit event) 될 때,
const form = document.querySelector('#form')
const todoInput = document.querySelector('#todo')
const todos = document.querySelector('#todos')

form.addEventListener('submit', function (event) {
    // 2. 실제 제출(요청)은 하지 않고
    event.preventDefault()
    // 3. ul 태그 아래에 li 태그로 append
    const li = document.createElement('li')
    // 비어있는 li 태그에 내용 채우기
    li.innerText = todoInput.value
    todos.appendChild(li)
    event.target.reset()
})
```
