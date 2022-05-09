# VueCLI

## SFC

- Component
  - 기본 HTML 엘리먼트를 확장하여 재사용 가능한 코드를 캡슐화하는데 도움을 줌
  - CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
  - 유지보수를 쉽게 만들어 줄 뿐만 아니라, 재사용성의 측면에서도 매우 강력한 기능 제공
  - Vue 컴포넌트 === Vue 인스턴스
- SFC(Single File Component)
  - 하나의 컴포넌트는 .vue 확장자를 가진 파일 하나에서 작성되는 코드의 결과물
  - Vue의 한 부품으로 그 안에 HTML, CSS, JS 코드가 있다
  - .vue 확장자를 가진 싱글 파일 컴포넌트를 통해 개발하는 방식
  - Vue 컴포넌트 === Vue 인스턴스 === .vue 파일
- Component 예시
  - 단일 파일에서 관리한다면 코드의 양이 많아질 경우 유지보수에 많은 비용이 발생할 것
  - 페이스북의 뉴스피드, 게시물, 활동 상태 등 한 화면을 구성하는 여러 컴포넌트가 있음
  - 각 기능 별로 파일을 나누어 개발하면 기능 별 유지보수에 용이하다
  - Vue 컴포넌트는 const app = new Vue({...})의 app을 의미하며 이는 Vue 인스턴스
    - 컴포넌트 기반의 개발이 반드시 파일 단위로 구분되어야하는 것은 아니다!
- 정리
  1. Vue 컴포넌트는 Vue 인스턴스이기도 하며
  2. Vue 인스턴스는 .vue 파일 안에 작성된 코드의 집합이고
  3. HTML, CSS, JS를 .vue라는 확장자를 가진 파일 안에서 관리하며 개발



## Vue CLI

> Vue.js 개발을 위한 표준 도구

- Node.js

  - 자바스크립트를 브라우저가 아닌 환경에서도 구동할 수 있도록 하는 자바스크립트 런타임 환경

- NPM(Node Package Manage)

  - 자바스크립트 언어를 위한 패키지 관리자

  - Python : pip = Node.js : NPM

  - 다양한 의존성 패키지 관리

  - Node.js 설치 시 함께 설치됨

    ```bash
    $ npm install -g @vue/cli # 설치(-g는 가이드에서 쓰라고 하는 것들만 써주면 됨)
    
    $ vue --version # 버젼 확인
    
    $ vue create my-first-app # 프로젝트 생성(vscode terminal로 진행하여 Vue 2 선택)
    
    $ cd my-first-app # 프로젝트 디렉토리 이동
    
    $ npm run serve # 서버 실행
    ```



## Babel & Webpack

> Vue CLI는 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음

- Babel
  - **자바스크립트의 ECMAScript 2015+ 코드를 이전 버전으로 번역/변환해 주는 도구**

- Webpack
  - Static Module Bundler
    - 모듈은 단지 파일 하나를 의미
    - JS와 애플리케이션이 복잡해지고 커지자 전역 scope를 공유하는 기존 개발 방식의 한계점으로 등장
    - 모듈 시스템 : **ESM**, AMD, CommonJS, UMD

  - **모듈 간의 의존성 문제를 해결하기 위한 도구**
    - 기존에 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려웠음
    - bundler : 모듈 의존성 문제를 해결해주는 도구

  - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함




#### Vue 프로젝트 구조

- node_modules
  - node.js 환경의 여러 의존성 모듈
- public/index.html
  - Vue 앱의 뼈대가 되는 파일
  - 실제 제공되는 단일 html 파일
- src/assets
  - webpack에 의해 빌드된 정적 파일
- src/components
  - 하위 컴포넌트들이 위치
- arc/App.vue
  - 최상위 컴포넌트
- src/main.js
  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - 실제 단일 파일에서 DOM과 data를 연결했던 것과 동일한 작업이 이루어지는 곳
  - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일
- babel.config.js
  - babel 관련 설정이 작성된 파일
- package.json
  - 프로젝트 종속성 목록과 지원되는 브라우저에 대한 구성 옵션이 포함
- package-lock.json
  - node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리
  - 팀원 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
  - 사용할 패키지 버전 고정
  - 개발 과정 간 의존성 패키지 충돌 방지



## Props & Emit

> 부모는 자식에게 "데이터"를 전달 => Pass props
>
> 자식은 자신에게 일어난 일을 부모에게 "알림" => Emit event

- props는 아래로, emit event는 위로
- 컴포넌트 구조
  - 템플릿(HTML)
    - HTML의 body 부분
    - 각 컴포넌트 작성
  - 스크립트(JavaScript)
    - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨
  - 스타일(CSS)
    - CSS가 작성되며 컴포넌트의 스타일을 담당
- 컴포넌트 등록
  1. 불러오기(import)
  2. 등록하기(register)
  3. 보여주기(print)



#### Props

```vue
<!-- App.vue -->

<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <the-about 
      my-message='This is prop data'  
      :parent-data="parentData" 
    >
    </the-about>
      <!-- 1. my-message : 자식에 보낼 prop 데이터 선언 -->
      <!-- 2. parent-data : 부모의 데이터 props를 dynamic하게 바인딩 -->
  </div>
</template>

<script>
import TheAbout from './components/TheAbout.vue'

export default {
  name: 'App',
  components: {
    TheAbout,
  },
  data: function () {
    return {
      parentData: 'This is parent data to child component'
    } <!-- 2. Dynamic Props : paraentData를 적고 template에서 바인딩하여 사용 가능 -->
  },
}
</script>
```

```vue
<!-- components/TheAbout.vue -->

<template>
  <div>
    <h1>{{ myMessage }}</h1>  <!-- 1-2. 수신한 prop 데이터 -->
    <h2>{{ parentData }}</h2> <!-- 2. Dynamic Prop 데이터 -->
  </div>
</template>

<script>
export default {
  name: 'TheAbout',
  props: {
    myMessage: String,
  } <!-- 1. 수신할 prop 데이터 -->
}
</script>
```

- 선언 시 camelCase, HTML에서는 kebab-case
- 컴포넌트의 'data'는 반드시 함수여야 함(새로운 data  객체를 반환)
- 숫자 전달 시 v-bind 필요
- 하위 속성과 상위 속성 사이의 단방향 바인딩 형성



#### Emit event

> Listening to Child Components Events

- $emit(eventName)

  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스너의 콜백 함수로 전달

- 부모 컴포넌트는 자식 컴포넌트가 사용되는 템플릿에서 v-on을 사용하여 자식 컴포넌트가 보낸 이벤트 청취

  ```vue
  <!-- components/TheAbout.vue -->
  
  <template>
    <div>
      <h1>{{ myMessage }}</h1>
      <h2>{{ parentData }}</h2>
      <input 
        type="text"
        v-model="childInputData"
        @keyup.enter="childInputChange"
      > <!-- 1. 귀를 열어 enter키가 눌렸다 올라가면 childInputChange를 실행하겠다 -->
    </div>
  </template>
  
  <script>
  export default {
    name: 'TheAbout',
    props: {
      myMessage: String,
    },
    methods: {
      childInputChange: function () {
        console.log('Child!!', this.childInputData)
        this.$emit('child-input-change', this.childInputData)
      } <!-- 2. $emit에 의해 child-input-change 이벤트 발생 -->
    },
  }
  </script>
  ```

  ```vue
  <!-- App.vue -->
  
  <template>
    <div id="app">
      <img alt="Vue logo" src="./assets/logo.png">
      <the-about 
        my-message='This is prop data'  
        :parent-data="parentData"
        @child-input-change="parentGetChange"
      > <!-- 2. 귀를 열어 child-input-change 이벤트가 발생하면 parentGetChange를 하겠다 -->
      </the-about>
    </div>
  </template>
  
  <script>
  import TheAbout from './components/TheAbout.vue'
  
  export default {
    name: 'App',
    components: {
      TheAbout,
    },
    data: function () {
      return {
        parentData: 'This is parent data to child component'
      }
    },
    methods: {
      parentGetChange: function (inputData) {
        console.log('Boss: 들리는군..', inputData)
      } <!-- 1. 이벤트에 의해 실행되는 parentGetChange 함수 정의 -->
    }
  }
  </script>
  ```

- event 이름은 대소문자 변환 X, **항상 kebab-case 사용 권장**
