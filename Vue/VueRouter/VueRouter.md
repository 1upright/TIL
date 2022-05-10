# VueRouter

> Vue.js 공식 라우터

- 라우터
  -  위치에 대한 최적의 경로를 지정하며, 이 경로를 따라 데이터를 다음 장치로 전향시키는 장치
- 라우트에 컴포넌트를 매핑한 후, 어떤 주소에서 렌더링할지 알려줌
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능 제공



## Router 시작

```bash
# 1. 프로젝트 생성 및 이동
$ vue create my-router-app
$ cd my-router-app

# 2. Vue Router Plugin 설치
$ vue add router

# 3. commit 여부 Yes
# 4. History mode 사용 여부 Yes
```

#### Router로 인한 변화

1. App.vue 코드

   ```vue
   <!-- App.vue -->
   
   <template>
     <div id="app">
       <nav>
         <router-link :to="{ name: 'home' }">Home</router-link> |
         <router-link :to="{ name: 'about' }">About</router-link> <!-- 1. -->
       </nav>
       <p>
         <router-view/> <!-- 2. -->
       </p>
     </div>
   </template>
   ```
   - `<router-link>`
     - 사용자 네비게이션을 가능하게 하는 컴포넌트
     - 목표 경로는 'to' prop으로 지정됨
     - 클릭 이벤트 차단하여 브라우저가 페이지를 다시 로드하지 않도록 함
     - 기본 GET 요청을 보내는 이벤트를 제거한 형태의 a 태그 기능
   - `<router-view>`
     - 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
     - 실제 component가 DOM에 부착되어 보이는 자리를 의미
     - router-link를 클릭하면 해당 경로와 연결되어 있는 index.js에 정의한 컴포넌트가 위치

2. router/index.js 생성

   ```javascript
   // router/index.js
   import Vue from 'vue'
   import VueRouter from 'vue-router'
   import HomeView from '../views/HomeView.vue'
   
   Vue.use(VueRouter)
   
   const routes = [
     {
       path: '/',
       name: 'home',
       component: HomeView
     },
     {
       path: '/about',
       name: 'about',
       component: () => import('../views/AboutView.vue')
     },
   ]
   ```

   - 라우트에 관련된 정보 및 설정이 작성되는 곳

3. view 디렉토리 생성

   - AboutView.vue
   - HomeView.vue



#### History mode

- HTML History API를 사용해서 router 구현한 것
- 페이지를 다시 로드하지 않고 URL 탐색
- History API : vue 기능이 아닌 브라우저 기능, 중요 X



## 그 외 설명

#### Named Routes

- 이름을 가지는 라우트

- 명명된 경로로 이동하려면 객체를 vue-router 컴포넌트 요소의 prop에 전달

  ```javascript
  // router/index.js
  
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  import HomeView from '../views/HomeView.vue'
  import AboutView from '../views/AboutView.vue'
  
  Vue.use(VueRouter)
  
  const routes = [
    {
      path: '/',
      name: 'home', // Named Route
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about', // Named Route
      component: AboutView,
    },
  ]
  ```

  ```vue
  <!-- App.vue -->
  
  <template>
    <div id="app">
      <nav>
        <router-link :to="{ name: 'home' }">Home</router-link> | <!-- 경로 -->
        <router-link :to="{ name: 'about' }">About</router-link> <!-- 경로 -->
      </nav>
      <p>
        <router-view/>
      </p>
    </div>
  </template>
  ```



#### 프로그래밍 방식 네비게이션

>  router-link를 사용하는 선언적 방식 외에도 router의 인스턴스 메서드를 사용하여 프로그래밍 방식으로 같은 작업 수행 가능 => `$router.push(...)`

- Vue 인스턴스 내부에서 라우터 인스턴스에 $router로 접근할 수 있음

- 다른 URL로 이동하려면 this.$router.push 호출 가능

- router-link를 클릭할 때 내부적으로 호출되는 메서드이므로 `<router-link :to="...">`를 클릭하면 `router.push(...)`를 호출하는 것과 같음

  ```vue
  <!-- AboutView.vue -->
  
  <template>
    <div class="about">
      <h1>This is an about page</h1>
      <button @click="moveToHome">To Home</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutView',
    methods: {
      moveToHome() {
        this.$router.push({ name: 'home' }) // 이 부분
      },
    },
  }
  </script>
  ```



#### Dynamic Route Matching

- 동적 인자 전달

- 주어진 패턴을 가진 라우트를 동일한 컴포넌트에 매핑해야 하는 경우

  ```javascript
  // router/index.js
  
  const routes = [
    {
      path: '/user/:userId/:username/:major',
      name: 'profile',
      component: UserProfile
    }
  ]
  ```

- 컴포넌트에서 this.$route.params로 사용 가능



## Vue Router가 필요한 이유

1. SPA 등장 이전
   - 서버가 모든 라우팅 통제
   - 요청 경로에 맞는 HTML 제공
2. SPA 등장 이후
   - 서버는 index.html 하나만 제공
   - 이후 모든 처리는 HTML 위에서 JS 코드 활용해 진행
   - 요청에 대한 처리를 더 이상 서버가 하지 않음
3. 라우팅 처리 차이
   - SSR
     - 라우팅에 대한 결정권을 서버가 가짐
   - CSR
     - 클라이언트는 더 이상 서버로 요청을 보내지 않고 응답받은 HTML 문서안에서 주소가 변경되면 특정 주소에 맞는 컴포넌트를 렌더링
     - 라우팅에 대한 결정권을 클라이언트가 가짐
   - 결국 Vue Rourter는 라우팅의 결정권을 가진 Vue.js에서 라우팅을 편리하게 할 수 있는 Tool을 제공해주는 라이브러리
