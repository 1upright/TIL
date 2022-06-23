# WebMVC

## Spring Web MVC

#### MVC Pattern

- Model
  - 어플리케이션 상태의 캡슐화
  - 상태 쿼리에 대한 응답
  - 어플리케이션 기능 표현
  - 변경을 view에 통지
- View
  - 모델을 화면에 시각적으로 표현
  - 모델에게 업데이트 요청
  - 사용자의 입력을 컨트롤러에 전달
  - 컨트롤러가 view를 선택하도록 허용
- Controller
  - 어플리케이션의 행위 정의
  - 사용자 액션을 모델 업데이트와 mapping
  - 응답에 대한 view 선택
- 어플리케이션 확장을 위해 Model, View, Controller 세가지 영역으로 분리
- 컴포넌트 변경이 다른 영역 컴포넌트에 영향을 미치지 않음(유지보수 용이)
- 컴포넌트 간의 결합성이 낮아 프로그램 수정 용이(확장성 뛰어남)
- 장점
  - 화면과 비즈니스 로직을 분리해서 작업 가능
  - 영역별 개발로 인해 확장성 뛰어남
  - 표준화된 코드를 사용하므로 공동작업이 용이하고 유지보수성이 좋음
- 단점
  - 개발과정이 복잡해 초기 개발속도가 늦음
  - 초보자가 이해하고 개발하기 다소 어려움



#### Spring MVC

- 특징
  - Spring은 DI나 AOP 같은 기능 뿐만 아니라, Servlet 기반의 WEB 개발을 위한 MVC Framework 제공
  - Spring MVC는 Model2 Architecture와 Front Controller Pattern을 Framework 차원에서 제공
  - Spring MVC Framework는 Spring을 기반으로 하고 있기 때문에 Spring이 제공하는 Transaction 처리나 DI 및 AOP 등을 손쉽게 사용
  
- act(회원가입, 로그인 등 이런것좀 해줘) + data(id, 비밀번호, 회원정보 등 데이터) = controller
  - act는 자동으로 할 수 있을듯 = data를 위한 사전 준비 = Front controller
    - spring이 대신 해줌
  - data = controller(우리가 만들 부분)
  
- 구성 요소
  - DispatcherServlet(Front Controller)
    - 모든 클라이언트의 요청을 전달받음
    - Controller에게 클라이언트의 요청을 전달하고, Controller가 리턴한 결과값을 View에게 전달하여 알맞은 응답 생성
  - HandlerMapping
    - 클라이언트의 요청 URL을 어떤 Controller가 처리할지 결정
    - URL과 요청 정보를 기준으로 어떤 핸들러 객체를 사용할지 결정하는 객체이며, DispatcherServlet은 하나 이상의 핸들러 매핑을 가질 수 있음
  - Controller
    - 클라이언트의 요청을 처리한 뒤, Model을 호출하고 그 결과를 DispatcherServlet에 알려준다
  - ModelAndView
    - Controller가 처리한 데이터 및 화면에 대한 정보를 보유한 객체
  - ViewResolver
    - Controller가 리턴한 뷰 이름을 기반으로 Controller의 처리 결과를 보여줄 View 결정
  - View
    - Controller의 처리결과를 보여줄 응답화면 생성
  
- 요청흐름
  
  ![요청흐름](WebMVC.assets/%EC%9A%94%EC%B2%AD%ED%9D%90%EB%A6%84.PNG)
  
  - 우리가 만들건 Controller
  
- 실행 순서
  1. DispatcherServlet이 요청 수신
  2. DispatcherServlet이 HandlerMapping에 어느 컨트롤러  쓸건지 요청 후 처리 컨트롤러 리턴
  3. DispatcherServlet이 요청을 Controller에 전달하면 Controller는 처리 요청 후 결과 리턴
  4. ModelAndView Object에 수행결과가 포함되어 DispatcherServlet에 리턴
  5. ModelAndView는 실제 JSP 정보를 갖고 있지 않으며, ViewResolver가 논리적 이름을 실제 JSP이름으로 변환
  6. View는 결과정보를 사용하여 화면 표현



#### Spring MVC 구현

- Step

  - web.xml에 DispatcherServlet 등록 및 Spring 설정파일 등록
  - 설정 파일에 HandlerMapping 설정
  - Controller 구현 및 Context 설정 파일에 등록
  - Controller와 JSP의 연결을 위해 View Resolver 설정
  - JSP 코드 작성

- Cotnroller 작성

  - 좋은 디자인은 Controller가 많은 일을 하지 않고 Service에 처리 위임

- web.xml - DispatcherServlet 설정

  ```xml
  <servlet>
      <servlet-name>appServlet</servlet-name>
      <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
      <init-param> <!-- 이거 덕분에 xml 이름 정할 수 있음. 없으면 servlet-name에 구체적으로 적어줘야 함 -->
          <param-name>contextConfigLocation</param-name>
          <param-value>/WEB-INF/spring/appServlet/servlet-context.xml</param-value>
      </init-param>
      <load-on-startup>1</load-on-startup>
  </servlet>
  
  <servlet-mapping>
      <servlet-name>appServlet</servlet-name>
      <url-pattern>/</url-pattern>
  </servlet-mapping>
  ```

  - 여러 개 설정 가능
  - 각 DispatcherServle마다 각각의 ApplicationContext 생성

- Controller Class 작성(HomeController.java)

  ```java
  @Controller
  public class HomeController {
      private static final Logger Logger = LoggerFactory.getLogger(HomeController.class);
      
      @RequestMapping(value = "/", method = RequestMethod.GET)
      public string home(Locale locale, Model model) {
          logger.info("Welcome home! The client locale is {}.", locale);
          
          model.addAttribute("message", "안녕하세요 스프링!");
          
          return "index";
      }
  }
  ```

- Context 설정파일에 Controller 등록(servlet-context.xml)

  ```xml
  <beans:bean class="com.text.web.Homecontroller"/>
  ```

- Controller와 response page 연결을 위한 ViewResolver 설정(servlet-context.xml)

  ```xml
  <beans:bean class="com.text.web.Homecontroller"/>
  
  <beans:bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
      <beans:property naem="prefix" value="/WEB-INF/views/" />
      <beans:property naem="suffix" value=".jsp" />
  </beans:bean>
  ```

- JSP에 `${message}` 쓰면 message가 출력됨



#### 실제 구현 - hello_spring

- webapp 우클릭 - New - others - index.jsp - index.jsp에 내용 적고 F11 눌러서 tomcat으로 실행시키면 화면 나옴
  - 하지만 절대로 jsp를 직접 호출하지 않기로 했었음..
  - 항상 controller 들렀다 가기로 함
  - 사용자가 직접 jsp 직접 접근 못하게 막아야함
  - index.jsp를 WEB-INF로 집어넣으면 실행이 안됨(접근 못하는 장소임)
  - 그 안에 있는 views에다가 index.jsp를 집어넣음
- servlet-context.xml 들어가보면 /WEB-INF/views/에 들어가서 index를 고른 후 .jsp를 붙이라고 beans:property의 형태로 만들어져 있음
- 프로젝트 자체 실행시키면? 404에러 - home.jsp가 없으니까
  - HomeController.java에서 return "home";을 return "index";로 바꿔보면 잘 나옴(다시 실행시키거나 f5)
  - HomeController.java 밑에 `model.addAttribute("msg", "안녕 스프링이야 컨트롤러 당겨왔어!!" );` 써주고 index.jsp에서 `${msg}` 넣어주면 "안녕 스프링이야 컨트롤러 당겨왔어!!"가 localhost에 출력됨
- 프로젝트 실행하면?
  - web.xml 읽음 => Web에 관한 설정
    - dispatcher servlet이 있고 이를 tomcat에 올림
      - 올리자마자 servle-context.xml의 정보를 읽어옴
        - 그 안에는 controller에 대한 정보가 있음
  - 그렇다면 root-context.xml은? => Non-Web에 관한 설정
    - web.xml의 첫번째에 context-param에 읽는 부분이 있음
      - 따라서 servlet-context.xml보다 먼저 읽힘
      - Service, Dao, Data Source 등이 담김



#### 실제 구현 - spring_webmvc

- 나중 되면 springboot에서 pom.xml 대신 써줌

- 그냥 실행시키면 오류

  - HomeController.java의 public class 위에 @Controller 붙여주면 다시 작동됨

- 두번째거 Hello Spring Web MVC 클릭하면 서버오류

  - nullpoint에러 => HomeController 42번째 줄 =>  helloService가 null => `private HelloService helloService;`에서 주입이 안됐음
    - 위에 @Autowired
    - 근데 에러 해결안됨 이젠 실행도 안돼버림
    - helloservice bean을 찾을 수 없대 => component-scan을 안했으니까!
      - HelloServiceImpl.java의 public class 위에 @Service를 해줘라
      - **Class를 새로 만들면 만들자마자 바로 위에 @Service 박아라!**
      - helloDao에도 @Autowired 하고 HelloDaoimpl.java에도 @Repository 만들자마자 박아주고

- 세번째거

  - index.jsp 살펴보면 /parameter로 간대

  - HomeController.java에서 /parameter 살펴보면 step03/form으로 간대

  - single에서 /sendparm으로 간대

  - HomeController.java에서 /sendparam 살펴보면 GET이랑 POST 둘다 받음

    - 이름 같아도 요청 방식 다르면 쓸 수 있음

  - parameter로 이름 다르게 하고 싶으면 @RequestParam 이용해서 넘어오는 파라미터 명시해주면 됨

    - `public String parameterTest(@RequestParam("userid") String id, @RequestParam("username") String name, String area) {`

  - multi 부분 돌리면 리스트로 나옴

    ```java
    private String userid;
    private String username;
    private List<String> fruit;
    ```

    - 이렇게 받았지만 그게 싫으면?
      - map을 사용! => Dto를 대신할 수 있는 java의 객체



## Controller

- @Controller와 @RequestMapping 선언
  - method 단위의 mapping 가능
  - DefaultAnnotationHandlerMapping과 AnnotationHandlerAdapter 사용
    - spring 3.0부터는 기본
  - Controller Class는 Client의 요청 처리
  - @Controller 선언
    - Class 타입에 적용
  - 회원가입도 MemberController의 /register고 글쓰기도 BoardController의 /register면 에러를 띄워버림
    - 해결 방법 : /user/register, /board/register처럼 구분함
      - 이후 /board/delete, /board/list와 같이 해줘야함
      - 이럴 때 상단에다가 @RequestMapping("/reboard")처럼 뺄 수 있는 것!
- Parameter type
  - HttpServletRequest, HttpServletResponse, HttpSession : 필요시 Servlet API 사용할 수 있음
  - Java.util.Locale : 현재 요청에 대한 Locale
  - InputStream, Reader : 요청 컨텐츠에 직접 접근할 때 사용
  - OutputStream, Writer : 응답 컨텐츠를 생성할 때 사용
  - @PathVariable annotation 적용 파라미터 : URL 템플릿 변수에 접근할 때 사용
  - @RequestParam annotation 적용 파라미터 : HTTP 요청 파라미터 매핑
  - @RequestHeader annotation 적용 파라미터 : HTTP 요청 헤더 매핑
  - @CookieValue annotation 적용 파라미터 : HTTP 쿠키 매핑
  - @RequestBody annotation 적용 파라미터 : HTTP 요청의 body 내용에 접근할 때 사용
  - Map, Model, ModelMap : view에 전달할 model data를 설정할 때 사용
  - 커맨드 객체 : HTTP 요청 parameter를 저장한 객체, 기본적으로 클래스 이름을 모델명으로 사용, @ModelAttribute annotation 설정으로 모델명을 설정할 수 있음
  - Errors, BindingResult : HTTP 요청 파라미터를 커맨드 객체에 저장한 결과, 커맨드 객체를 위한 파라미터 바로 다음에 위치
  - SessionStatus : 폼 처리를 완료했음을 처리하기 위해 사용, @SessionAttributes annotation을 명시한 session속성을 제거하도록 이벤트를 발생시킨다
- @RequestBody, @ResponseBody => 비동기처리에서 중요하게 사용되나 나중에 다루기로..
- Servlet API : 필요에 따라서 쓸 수 있다
- Return Type
  - ModelAndView
  - Model
  - Map
  - String
  - View
  - void
    - method가 ServletResponse나 HttpServiceResponse 타입의 parameter를 갖는 경우 method가 직접 응답을 처리한다고 가정한다. 그렇지 않을 경우 요청 URL로부터 결정된 View를 보여준다
  - @ResponseBody Annotation 적용



## View

- View 지정
  - Controller에서는 처리 결과를 보여줄 View 이름이나 객체를 리턴하고, DispatcherServlet은 View이름이나 View 객체를 이용하여 view 생성
  - ViewResolver : 논리적 view와 실제 JSP파일 mapping
    - servlet-context.xml
  - View 이름 명시적 지정
    - ModelAndView와 String 리턴 타입
  - View 자동 지정
    - RequestToViewNameTranslator를 이용하여 URL로부터 view 이름 결정
    - 자동 지정 유형
      - return type이 Model이나 Map인 경우
      - return type이 void이면서 ServletResponse나 HttpServletResponse 타입의 parameter가 없는 경우
  - redirect view
    - View 이름에 "redirect:" 접두어를 붙이면, 지정한 페이지로 redirect됨
    - `redirect:/board/list.html?pg=1`
    - `redirect:http://localhost/board/list.html?pg=1`
    - 기본이 forward니까 redirect해야하는 경우에만 써주면 됨


## Model

> View에 전달하는 데이터

- Model 생성
  - Map, Model, ModelMap을 통한 설정
    - method의 argument로 받는 방식
  - Model Interface 주요 method
    - Model addAttribute(String name, Object value);
    - Model addAttribute(Object value);
    - Model addAllAttributes(Collection<?> values);
    - Model addAllAttributes(Map<String, ?> attributes);
    - Model mergeAttributes(Map<String, ?> attributes);
    - boolean containsAttribute(String name);
    - 어차피 spring이 다 자동완성시켜주긴 함
  - @ModelAttribute annotation을 이용한 model data 처리
    - @RequestMapping annotation이 적용되지 않은 별도 method로 모델이 추가될 객체를 생성
- 요청 URL 매칭
  - 전체 경로와 Servlet기반 경로 매칭
    - DispatcherServlet은 DefaultAnnotationHandlerMapping Class를 기본으로 HandlerMapping 구현체로 사용
    - Default로 Context 내의 경로가 아닌 Servlet 경로를 제외한 나머지 경로에 대해 mapping



## 총정리

1. 웹 어플리케이션이 실행되면 Tomcat(WAS)에 의해 web.xml이 loading
2. web.xml에 등록되어 있는 ContextLoaderListener(Java Class)가 생성. ContextLoaderListener class는 ServletContextListener interface를 구현하고 있으며, ApplicationContext를 생성하는 역할 수행
3. 생성된 ContextLoaderListener는 root-context.xml을 loading
4. root-context.xml에 등록되어 있는 Spring Container가 구동. 이 때 개발자가 작성한 Business Login(Service)에 대한 부분과 Database Logic(DAO), VO 객체들이 생성
5. Client로부터 요청(request)이 들어옴
6. DispatcherServlet이 생성. DispatcherServlet은 FrontController의 역할을 수행. Client로부터 요청 온 메시지를 분석하여 알맞은 PageController에게 전달하고 응답을 받아 요청에 따른 응답을 어떻게 할지 결정. 실질적인 작업은 PageController에서 이루어진다
7. DispatcherServlet은 servlet-context.xml을 loading
8. 두번째 Spring Container가 구동되며 응답에 맞는 PageController들이 동작. 이 때 첫번째 Spring Container가 구동되면서 생성된 DAO, VO, Service 클래스들과 협업하여 알맞은 작업 처리
