# Vue기초

> 사용자 인터페이스를 만들기 위한 진보적인 자바스크립트 프레임워크 by Evan You

## 사전 지식

- SPA
  - Single Page Application
  - 단일 페이지 애플리케이션
  - 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 어플리케이션, 사용자 경험(UX) 향상
- CSR
  - Client Side Rendering
  - 서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트에서 화면을 구성
  - 장점 : 서버와 클라이언트 간 트래픽 감소
  - 단점 : SSR에 비해 페이지 최종 렌더링 시점이 느림, 최적화에 어려움
- SSR
  - Server Side Rendering
  - 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
  - JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식
  - 장점 : 초기 구동 속도가 빠름, SEO(검색 엔진 최적화)에 적합
  - 단점 : 모든 요청마다 새로운 페이지를 구성하여 전달하므로 사용자 경험 떨어짐, 트래픽이 많아 서버에 부담
- CSR & SSR
  - 실제 브라우저에 그려질 HTML을 서버가 만든다면 SSR, 클라리언트가 만든다면 CSR 사용
  - 프로젝트 구성에 맞는 적절한 선택이 필요
- SEO
  - Search Engine Organization(검색 엔진 최적화)
  - 웹 페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성하여 검색 결과의 상위에 노출될 수 있도록 하는 작업
  - 구글 등장 이후 검색엔진들이 컨텐츠의 신뢰도를 파악하는 기초 지표로 사용



## Concepts of Vue.js

- MVVM Pattern
  - 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴
  - 구성 요소
    - Model : JavaScript Object이며 Vue Instance 내에서 data라는 이름으로 존재한다
    - View : JavaScript에서 DOM(HTML)이며 Data의 변화에 따라 바뀌는 대상
    - View Model : 모든 Vue Instance로 View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리



## Quick Start of Vue.js

> Data가 변화하면 DOM이 변경(Data 로직 작성 => DOM 작성)

1. CDN 작성

   ```html
   <!-- 1. Vue CDN -->
   <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
   ```

2. 선언적 렌더링

   ```html
   <body>
       <h2>선언적 렌더링</h2>
       <div id="app1">
           {{ message }}
       </div>
   ```

   ```javascript
   <script>
       const app1 = new Vue({
           el: '#app1'
           data: {
               message: '안녕하세요 Vue!'
           }
       })
   ```

3. Element 속성 바인딩

   ```html
   <h2>Element 속성 바인딩</h2>
   <div id="app2">
       {{ message }}
   </div>
   ```

   ```javascript
   const app2 = new Vue({
       el: '#app2',
       data: {
           message: `이 메시지는 ${new Date()} 에 로드됨!`
       }
   })
   ```

4. 조건문

   ```html
   <h2>조건</h2>
   <div id="app3">
       <p v-if="seen">보인다</p>
   </div>
   ```

   ```javascript
   const app3 = new Vue({
       el: '#app3',
       data: {
           seen: true,
       }
   })
   ```

5. 반복문

   ```html
   <h2>반복</h2>
   <div id="app4">
       <ol>
           <li v-for="todo in todos">
               {{ todo.text }}
           </li>
       </ol>
   </div>
   ```

   ```javascript
   const app4 = new Vue({
       el: '#app4',
       data: {
           todos: [
               { text: 'js 복습'},
               { text: 'vue 배우기'},
               { text: '멋진거 만들기'}
           ]
       }
   })
   ```

6. 사용자 입력 핸들링

   ```html
   <h2>사용자 입력 핸들링</h2>
   <div id="app5">
       <p>{{ message }}</p>
       <input v-model="message" type="text">
       <button v-on:click="reverseMessage">로꾸꺼</button>
   </div>
   ```

   ```javascript
   const obj = {
       el: '#app5',
       data: {
           message: '안녕하세요'
       },
       methods: {
           reverseMessage: function () {
               this.message = this.message.split('').reverse().join('')
           }
       }
   }
   ```

   

## Basic syntax of Vue.js

- Vue instance

  - 모든 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작

    ```javascript
    const app = new Vue({
        
    })
    ```

- `el`(Options/DOM)

  - Vue 인스턴스에 연결할 기존 DOM 요소, new를 이용한 인스턴스 생성 때만 사용

    ```javascript
    const app = new Vue({
        el: '#app'
    })
    ```

- `data`(Options/Data)

  - Vue 인스턴스의 데이터 객체로 인스턴스의 상태 데이터를 정의하는 곳

    ```javascript
    const app = new Vue({
        el: '#app',
        data: {
            message: 'Hello',
        }
    })
    ```

- `methods`(Options/Data)

  - Vue 인스턴스에 추가할 메서드

    ```javascript
    const app = New Vue({
        el: '#app',
        data: {
            message: 'Hello',
        },
        methods: {
            greeting: function () {
                console.log('hello')
            }
        }
    })
    ```

- `this`

  - Vue 함수 객체 내에서 vue 인스턴스를 가리킴

  - data, method 정의에서는 화살표 함수를 사용하면 안됨 this === window이니까

    ```javascript
    const app = New Vue({
        el: '#app',
        data: {
            a: 1,
        },
        methods: {
            myFunc: function () {
                console.log(this) // Vue instance
            }
            yourFunc: function () => {
        		console.log(this) // window
    		}
        }
    })
    ```



## Interpolation

- Text
  - `<span>메시지: {{ msg }}</span>`
- Raw HTML
  - `<span v-html="rawHtml"></span>`
- Attributes
  - `<div v-bind:id="dynamicId"></div>`
- JS 표현식
  - `{{ number + 1 }}`



## Directive

> v- 접두사가 있는 특수 속성으로 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 역할을 함

- v-text

  - 엘리먼트의 textContent를 업데이트

    ```html
    <body>
      <div id="app">
        <p>{{ message }}</p>
        <p v-text="message"></p>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            message: 'Hello'
          }
        })
      </script>
    </body>
    ```

- v-html

  - 엘리먼트의 innerHTML을 업데이트(XSS 공격에 취약)

    ```html
    <body>
      <div id="app">
        <p>{{ message }}</p>
        <p v-text="message"></p>
        <p v-html="message"></p>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            message: '<strong>강하닷</strong>'
          }
        })
      </script>
    </body>
    ```

- v-show

  - 조건부 렌더링 중 하나

  - 단순히 엘리먼트에 display CSS 속성을 토글하는 것

  - 요소는 항상 렌더링되고 DOM에 남아 있다

  - 조건이 바뀔 때마다 데이터는 항상 있고 번갈아 보여주는 느낌

  - Expensive initial load, Cheap toggle

  - 한 번만 렌더링되는 경우라면 v-if에 비해 렌더링 비용이 높지만 자주 변경되는 요소라면 보여주는지에 대한 여부만 판단하므로 토글 비용이 적다

    ```html
    <body>
      <div id="app">
        <p v-show="isTrue">TRUE</p>
        <p v-show="isFalse">FALSE</p>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            isTrue: true,
            isFalse: false,
          }
        })
      </script>
    </body>
    ```

- v-if

  - 조건부 렌더링 중 하나

  - 조건에 따라 요소를 렌더링(directive의 표현식이 true일 때만 렌더링)

  - 엘리먼트 및 포함된 directive는 토글하는 동안 삭제되고 다시 작성됨

  - 조건이 바뀔 때마다 새로 작성해서 보여주는 느낌

  - Cheap initial load, Expensive toggle

  - 한 번만 렌더링되는 경우라면 v-show에 비해 렌더링 비용이 낮지만 자주 변경되는 요소라면 계속 다시 렌더링 해야 하므로 토글 비용이 많다

    ```html
    <body>
      <div id="app">
        <p v-if="seen">seen is TRUE</p>
    
        <p v-if="myType === 'A'">A</p>
        <p v-else-if="myType === 'B'">B</p>
        <p v-else-if="myType === 'C'">C</p>
        <p v-else>NOT A/B/C</p>
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            seen: false,
            myType: 'A',
          }
        })
      </script>
    </body>
    ```

- v-for

  - 원본 데이터를 기반으로 엘리먼트 또는 템플릿 블록을 여러 번 렌더링

  - v-for 사용 시 반드시 key 속성을 각 요소에 작성(`:key=""`)

    ```html
    <body>
      <div id="app">
        <h2>String</h2>
          <div v-for="char in myStr">
            {{ char }}
          </div>
        <h2>Array</h2>
        <div v-for="fruit in fruits">
          {{ fruit }}
        </div>
        <div v-for="(fruit, idx) in fruits" :key="idx">
          {{ idx }} => {{ fruit }} 
        </div>
        
        <div v-for="todo in todos" :key="`todo-${todo.id}`">
          <p>{{ todo.title }} => {{ todo.completed }}</p>
        </div>
    
        <h2>Object</h2>
        <div v-for="value in myObj">
          {{ value }}
        </div>
        <div v-for="(value, key) in myObj">
          {{ key }} => {{ value }}
        </div>
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            myStr: 'Hello World!',
            fruits: ['apple', 'banana', 'coconut'],
            todos: [
              { id: 1, title: 'todo1', completed: true },
              { id: 2, title: 'todo2', completed: false },
              { id: 3, title: 'todo3', completed: true },
            ],
            myObj: {
              name: 'kim',
              age: 100,
            }
          }
        }) 
      </script>
    </body>
    ```

- v-on

  - 엘리먼트에 이벤트 리스너를 연결

  - 특정 이벤트 발생 시 주어진 코드 실행

  - 약어(click을 예시로)

    - @click
    - v-on:click

    ```html
    <body>
      <div id="app">
        <!-- 메서드 핸들러 -->
        <button v-on:click="alertHello">Button</button>
        <button @click="alertHello">Button</button>
        <!-- 기본 동작 방지 -->
        <form action="" @submit.prevent="alertHello">
          <button>GoGo</button>
        </form>
    
        <!-- 키 별칭을 이용한 키 입력 수식어 -->
        <input type="text" @keyup.enter="log"> 
        <!-- cb 함수에서 특수문법 () -->
        <input type="text" @keyup.enter="log('ssafy')"> 
        
        <p>{{ message }}</p>
        <button @click="changeMessage">change message</button>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          // 값
          data: {
            message: 'Hello Vue',
          },
          // 행동(함수)
          methods: {
            alertHello: function () {
              alert('hello')
            },
            log: function (something) {
              console.log(something)
            },
            changeMessage() {
              this.message = 'New message!!!'
            },
          }
    
        })
      </script>
    </body>
    ```

- v-bind

  - HTML 요소의 속성에 Vue 상태 데이터를 값으로 할당

  - 약어(href를 예시로)

    - :href
    - v-bind:href

    ```html
    <body>
      <div id="app">
        <!-- 속성 바인딩 -->
        <img v-bind:src="imageSrc" :alt="altMsg">
        <img :src="imageSrc" alt="altMsg">
        <hr>
    
        <!-- 클래스 바인딩 -->
        <div :class="{ active: isRed }">
          클래스 바인딩
        </div>
    
        <h3 :class="[activeRed, myBackground]">
          hello vue
        </h3>
        <hr>
    
        <!-- 스타일 바인딩 -->
        <p :style="{ fontSize: fontSize + 'px' }">
          this is paragraph
        </p>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            fontSize: 16,
            altMsg: 'this is image',
            imageSrc: 'https://picsum.photos/200/300/',
            isRed: true,
            activeRed: 'active',
            myBackground: 'my-background-color',
          }
        })
        const myName = 'asdf'
    
      </script>
    </body>
    ```

- v-model

  - HTML form 요소의 값과 data를 양방향 바인딩

  - 수식어에는 `.lazy`, `.number`, `.trim`이 있다고 한다 => 나중에 자세히 배울 예정

    ```html
    <body>
      <div id="app">
        <h2>Input -> Data 단방향</h2>
        <p>{{ msg1 }}</p>
        <input type="text" @input="onInputChange">
        <hr>
        <h2>Input <-> Data 양방향</h2>
        <p>{{ msg2 }}</p>
        <input type="text" v-model="msg2">
        <hr>
        쳌! <input id="box" type="checkbox" v-model="checked">
        <label for="box">{{ checked }}</label>
    
    
      </div>
    
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            msg1: '111',
            msg2: '222',
            checked: true,
          },
          methods: {
            onInputChange (event) {
              this.msg1 = event.target.value
            }
          },
    
        })
      </script>
    </body>
    ```

    

## Advanced syntac of Vue.JS

> [methods](#basic-syntax-of-vue.js)와의 비교를 중심으로

- `computed`(Options/Data)

  - 데이터를 기반으로 계산된 속성

  - 함수의 형태로 정의하지만 함수가 아닌 함수의 반환 값이 바인딩됨

  - **종속된 데이터가 변경될 때만 함수를 실행!**

  - 반드시 **반환값**이 있어야 함(Return이 있는 것이 핵심)

  - 가장 효율적으로 함수를 다루는 방법으로, 가장 많이 쓰인다.

    ```html
    <body>
      <div id="app">
        <input v-model="r" type="text">
        <p>{{ r }}</p>
        <p>{{ area }}</p>
        <p>{{ perim }}</p>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            r: 2,
          },
          computed: {
            area: function () {
              return this.r ** 2 * 3.14
            },
            perim: function () {
              return this.r * 2 * 3.14
            }
          }
        })
      </script>
    </body>
    ```

- `watch`(Options/Data)

  - 데이터를 감시하다 데이터의 변화가 일어났을 때 실행되는 함수

  - 코드가 지저분해지므로 잘 안쓰게 된다

    ```html
    <body>
      <div id="app">
        <p>{{ num }}</p>
        <button @click="num += 1">add 1</button>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            num: 2,
          },
          watch: {
            num: function () {
              console.log(`${this.num}이 변경되었습니다.`)
            }
          },
        })
      </script>
    </body>
    ```

- `filters`(Options/Assets)

  - 텍스트 형식화를 적용할 수 있는 필터
  - interpolation 혹은 v-bind를 이용할 때 사용 가능
  - 필터는 자바스크립트 표현식 마지막에 "|"와 함께 추가되어야 함
  - chaining하여 이어 사용 가능



#### vs "computed"

- "methods" vs "computed"

  - 값이 변경되면 함수를 실행하는 것은 같다

  - methods는 data를 바꾸는 로직, computed는 data를 통한 값을 얻음

  - computed는 종속된 대상이 변경되지 않으면 작성된 함수를 여러 번 호출해도 계산을 다시 하지 않고 계산되어 있던 결과를 반환

  - methods는 호출하면 렌더링을 다시 할 때마다 항상 함수를 실행

  - ex) 함수에서 대상이 되는 값(this.~)이 아닌 다른 값(other)이 변경된다면 computed는 계산을 다시 하지 않지만 methods는 다시 하게 됨

    ```html
    <body>
      <div id="app">
        <div>
          <input type="text" v-model="message">
        </div>
        {{ other }}
        <p>Original: <strong>{{ message }}</strong></p>
        <p>Reverse by Method: <strong>{{ reverseMessage() }}</strong></p>
        <p>Reverse by Computed: <strong>{{ reversedMessage }}</strong></p>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const app = new Vue({
          el: '#app',
          data: {
            sessionid: 'asdf',
            message: 'Original',
            other: 'asdf'
          },
          // data를 바꾸는 로직 위주! (setter 함수들)
          methods: {
            reverseMessage() {
              console.log('method!!')
              return this.message.split('').reverse().join('')
            },
          },
          // data를 통한 값을 얻음! (getter 함수들)
          computed: {
            // (data에 의존하는)계산된 값
            reversedMessage() {
              console.log('computed!!')
              return this.message.split('').reverse().join('')
            },
            isLoggedIn() {
              return this.sessionid ? true : false
            }
          }
        })
      </script>
    </body>
    ```

- "watch" vs "computed"

  - watch
    - 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용
    - 명령형 프로그래밍 방식(감시할 데이터를 지정하고 그 데이터가 바뀌면 특정 함수 실행)
    - "특정 값이 변동하면 다른 작업을 한다"
  - computed
    - 특정 데이터를 직접적으로 사용/가공하여 다른 값으로 만들 때 사용
    - 선언형 프로그래밍 방식(계산해야 하는 목표 데이터를 정의)
    - "특정 값이 변동하면 해당 값을 다시 계산하여 보여준다"
  - 어떤 것이 더 우수하다기보단 사용하는 목적과 상황이 다르지만 computed를 쓰는 경우가 대부분일 것



## Lifecycle Hooks

- 각 Vue 인스턴스는 생성될 때 일련의 초기화 단계를 거침

  - 데이터 관찰 설정이 필요한 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM을 업데이트하는 경우 등

- created

  - 외부 api에서 애플리케이션의 초기 데이터를 받아올 때 

  - vue 인스턴스가 생성된 후에 호출됨

    ```html
    <body>
      <div id="app">
        <img v-if="imgSrc" :src="imgSrc" alt="sample img">
        <button @click="getImg">GetDog</button>
      </div>
      
      <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
      <script>
        const API_URL = 'https://dog.ceo/api/breeds/image/random'
        const app = new Vue({
          el: '#app',
          data: {
            imgSrc: '',
          },
          methods: {
            getImg: function () {
              axios.get(API_URL)
                .then(response => {
                  this.imgSrc = response.data.message
                })
            }
          },
          // 외부 API에서 초기 데이터 받아오기
          created: function () {
            this.getImg()
          }
        })
      </script>
    </body>
    ```

- 그 외에 mounted, updated 등이 있지만 주로 created만 사용될 것임