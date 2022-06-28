# SpringBoot

## 특징

- Spring의 경우 Application을 개발하려면 사전에 많은 작업을 해야 했다
  - library 추가, dependency 설정, SpringFramework가 처리해야 하는 여러 가지 구성 및 설정파일
- SpringBoot의 장점
  - project에 따라 자주 사용되는 library들이 미리 조합되어 있다
  - 복잡한 설정을 자동으로 처리
  - 내장 서버를 포함해서 tomcat과 같은 WAS를 추가로 설치하지 않아도 개발 가능
  - WAS에 배포하지 않고도 실행할 수 있는 JAR파일로 Web Application을 개발할 수 있다



## 프로젝트 생성

- New > Spring Starter Project

  - Name 지정
  - Maven/jar/8/Java
  - Group 지정
  - Package 지정
  - Next해서 Dependency 설정
    - Spring Boot DevTools, Spring Web 추가
    - 그 외에 더 쓸거 있으면 추가
  - 확인 후 Finish

- project 생성 구조 및 주요 구성 폴더/파일

  - scr/main/java : java source directory
  - HelloSpringBootApplication.java : application을 시작할 수 있는 main method가 존재하는 스프링 구성 메인 클래스
  - static : css, js, img 등의 정적 resource directory
  - templates : SpringBoot에서 사용 가능한 여러가지 View Template(Thymeleaf, Velocity, FreeMarker등) 위치
  - apllication.properties : application 및 스프링의 설정 등에서 사용할 여러가지 property를 정의한 file
  - src/main : jsp 등의 리소드 directory

- 실행

  - src/main/resources에 application.properties에서 `server.port=80` 이런식으로 포트 지정
    - 포트 번호를 지정하고 싶다면
  - static에 index.html파일 만들어서 아무거나 쓰고 실행시켜보기(왼쪽아래 local 밑에 있는거 눌러도 실행됨)
    - 정상 출력 확인

- home.jsp

  - src/main에 webapp/WEB-INF/views/home.jsp 생성 후 간단 작성
    - 실행시켜서 localhost/home.jsp하면 안뜸

- Controller 만들고 다른 경로로 들어가보기

  - src/main/java 밑에 com.ssafy.hello.controller 클래스 만들기

  - HelloController.java에

    ```java
    package com.ssafy.hello.controller;
    
    import org.springframework.stereotype.Controller;
    import org.springframework.web.bind.annotation.GetMapping;
    
    @Controller
    public class HelloController {
    	
    	@GetMapping("/")
    	public String index() {
    		return "home";
    	}
    }
    ```

    - 그럼 "home"의 앞에 WEB-INF/views/에 해당하는 prefix를, home 뒤에는 home.jsp에 해당하는 suffix를 붙여야겠지?

    - application.properties

      ```properties
      server.port=80
      
      spring.mvc.view.prefix=/WEB-INF/views/
      spring.mvc.view.suffix=.jsp
      ```

      - 그래도 안됨

    - 여기서도 jsp 실행할 수 있게 하려면 pom.xml을 건드려야 함(내장 톰캣 부르기)

      ```xml
      	<dependency>
      		<groupId>javax.servlet</groupId>
      		<artifactId>jstl</artifactId>
      	</dependency>
      	
      	<dependency>
      		<groupId>org.apache.tomcat.embed</groupId>
      		<artifactId>tomcat-embed-jasper</artifactId>
      	</dependency>
      ```

    - 실행하면 정상작동

- index.html

  ```html
  <a href="/home">jsp gogo</a>
  <a href="/rest">REST gogo</a>
  ```

  - HelloController.java

    ```java
    	@GetMapping("/home")
    	public String index() {
    		return "home";
    	}
    ```

  - HelloRestController.java

    ```java
    	@GetMapping("/rest")
    	public String rest() {
    		return "Rest 데이터";
        }
    ```

- application.properties

  ```properties
  server.servlet.context-path=/ssafy
  ```

  - 이걸 붙이면 들어갈때 localhost/ssafy로 들어가야함



## guestbook_springboot 실습

- dependency에 mysql, mybatis 추가

- application.properties 세팅

  ```properties
  #server setting
  server.port=80
  
  #JSP Setting
  spring.mvc.view.prefix=/WEB-INF/views/
  spring.mvc.view.suffix=.jsp
  
  #DataBase Setting
  spring.datasource.driver-class-name=com.mysql.cj.jdbc.Driver
  spring.datasource.url=jdbc:mysql://127.0.0.1:3306/ssafyweb?serverTimezone=UTC&useUniCode=yes&characterEncoding=UTF-8
  spring.datasource.username=ssafy
  spring.datasource.password=ssafy
  
  #MyBatis Setting
  mybatis.type-aliases-package=com.ssafy.guestbook.model
  mybatis.mapper-locations=mapper/**/*.xml
  
  #File Upload size Setting
  spring.servlet.multipart.max-file-size=5MB
  spring.servlet.multipart.max-request-size=5MB
  
  #log level Setting
  logging.level.root=info
  logging.level.com.ssafy.guestbook.controller=debug
  
  #Failed to start bean 'documentationPluginsBootstrapper'; error
  #spring.mvc.pathmatch.matching-strategy = ANT_PATH_MATCHER
  ```

  - `mapper/**/*.xml` : mapper 밑에 폴더가 몇개든 상관없고 그 밑에 모든 xml을 가져올 것이다

- com.ssafy.guestbook.config/WebMvcConfiguration.java

  ```java
  @Configuration
  @EnableAspectJAutoProxy
  @MapperScan(basePackages = {"com.ssafy.**.mapper"})
  public class WebMvcConfiguration implements WebMvcConfigurer {
  
  	@Autowired
  	private ConfirmInterceptor confirm;
  	
  	private final List<String> patterns = Arrays.asList("/guestbook/*", "/admin/*", "/user/list");
  	
  	@Override
  	public void addInterceptors(InterceptorRegistry registry) {
  		registry.addInterceptor(confirm).addPathPatterns(patterns);
  	}
  }
  ```



## Swagger

- Swagger를 이용한 REST API 문서화

  - 프로젝트 개발시 일반적으로 FrontEnd 개발자와 BackEnd 개발자 분리
  - FrontEnd 개발자의 경우 화면과 로직에 집중을 하고 BackEnd 개발자가 만든 문서 API를 보며 데이터 처리를 하게 된다
  - 이때 개발 상황의 변화에 따른 API의 추가 또는 변경할 때마다 문서에 적용하는 불편함 발생
  - 이 문제 해결 위해 Swagger 사용

- Swagger

  - 간단한 설정으로 프로젝트의 API 목록을 웹에서 확인 및 **테스트** 할 수 있게 해주는 Library
  - Swagger를 사용하면 Controller에 정의되어 있는 모든 URL을 바로 확인할 수 있다
  - API 목록 뿐 아니라 API의 명세 및 설명도 볼 수 있으며, API를 직접 테스트해 볼 수도 있다

- Swagger 적용

  - pom.xml에 swagger2 dependency 추가

  - SwaggerConfiguration.java

    ```java
    @Configuration
    @EnableSwagger2 // 이거 호출
    public class SwaggerConfiguration {
    
    //	Swagger-UI 2.x 확인
    //	http://localhost:8080/{your-app-root}/swagger-ui.html
    //	Swagger-UI 3.x 확인
    //	http://localhost:8080/{your-app-root}/swagger-ui/index.html
    
    	private String version = "V1";
    	private String title = "SSAFY GuestBook API " + version;
    	
    	@Bean
    	public Docket api() {
    		return new Docket(DocumentationType.SWAGGER_2).consumes(getConsumeContentTypes()).produces(getProduceContentTypes())
    					.apiInfo(apiInfo()).groupName(version).select()
    					.apis(RequestHandlerSelectors.basePackage("com.ssafy.guestbook.controller"))
    					.paths(regex("/admin/.*")).build()
    					.useDefaultResponseMessages(false);
    	}
    	
    	private Set<String> getConsumeContentTypes() {
            Set<String> consumes = new HashSet<>();
            consumes.add("application/json;charset=UTF-8");
    //      consumes.add("application/xml;charset=UTF-8");
            consumes.add("application/x-www-form-urlencoded");
            return consumes;
        }
    
        private Set<String> getProduceContentTypes() {
            Set<String> produces = new HashSet<>();
            produces.add("application/json;charset=UTF-8");
            return produces;
        }
    
    	private ApiInfo apiInfo() {
    		return new ApiInfoBuilder().title(title)
    				.description("<h3>SSAFY API Reference for Developers</h3>Swagger를 이용한 GuestBook API<br><img src=\"/img/ssafy_logo.png\" width=\"150\">") 
    				.contact(new Contact("SSAFY", "https://edu.ssafy.com", "ssafy@ssafy.com"))
    				.license("SSAFY License")
    				.licenseUrl("https://www.ssafy.com/ksp/jsp/swp/etc/swpPrivacy.jsp")
    				.version("1.0").build();
    	}
    
    }
    ```

  - Swagger 적용될 Controller, Dto 설정

  - API 실행화면에서 설정해보기

  - 오류에 대해 프론트에 알리기

    ```java
    @ApiResponse({
        @ApiResponse(code = 405, message = "지원하지 않는 메소드 호출!")
        @ApiResponse(code = 200, message = "정상 처리")
        @ApiResponse(code = 500, message = "서버 에러!")
    })
    ```

    - 이걸 보고 오류나면 고치라고 전달해주는 API 문서일 뿐 실제로 이렇게 실행되는 것이 아님