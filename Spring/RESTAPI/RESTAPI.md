# REST API

## 배경 지식

- OPEN API
  - 프로그래밍에서 사용할 수 있는 개방되어 있는 상태의 Interface
  - 대부분의 OPEN API가 REST 방식으로 지원
- REST
  - Representational State Transfer
  - 제어할 자원을 명시하고 HTTP Method(GET, POST, PUT, DELETE)을 통해 해당 자원을 제어하는 명령을 내리는 방식의 아키텍처
  - 구성
    - 자원 - URI
    - 행위 - HTTP Method
    - 표현 (Representations)
  - 기존과의 차이점
    - 기존 Service : 요청에 대한 처리를 한 후 가공된 data를 이용하여 특정 플랫폼에 적합한 형태의 View로 만들어 반환
    - REST Service : data 처리만 한다거나, 처리 후 반환될 data가 있다면 JSON이나 XML 형식으로 전달. View에 대해서는 신경 쓸 필요 없다
      - 이런 이유로 Open API에서 많이 사용
  - 딱 정해진 표준이 없어 다들 이렇게 쓰더라~ 정도의 암묵적인 표준만 정해져 있음
    - 하이픈 사용 가능, 언더바 사용 X
    - 대문자 사용 X
    - URI 마지막에 `/` 사용 X
    - `/`로 계층 관계 나타냄
    - 확장자가 포함된 파일 이름을 직접 포함시키지 않는다
    - URL는 명사 사용
- Jackson library
  - jackson-databind 라이브러리는 객체를 JSON 포맷의 문자열로 변환시켜 브라우저로 전송
  - jackson-dataformat-xml 라이브러리는 객체를 xml로 브라우저로 전송
- REST 관련 Annotation
  - @RestController : Controller가 REST 방식을 처리하기 위한 것임을 명시
  - @ResponseBody : JSP 같은 뷰로 전달되는 것이 아니라 데이터 자체를 전달
  - @PathVariable : URL 경로에 있는 값을 파라미터로 추출
  - @CrossOrigin : Ajax의 크로스 도메인 문제를 해결
  - @RequestBody : JSON 데이터를 원하는 타입으로 바인딩



## REST_API 실습

#### 아이디 중복 검사

```java
// MemberController.java
@GetMapping("/idcheck")
public @ResponseBody String idCheck(@RequestParam("ckid") String checkId) throws Exception {
    logger.debug("아이디 중복 검사 : {}", checkid);
    int cnt = memberService.idCheck(checkId);
    return "{idcount:'" + cnt + "'}";
}
```

- @ResponseBody : 이것이 ViewName이 아니라 넘겨주는 데이터 자체라는 것을 알려줌

  - 하지만 돌려보면 오류가 남
    - JSONObject나 JSONArray를 쓰면 된다

  ```java
  @GetMapping("/idcheck")
  public @ResponseBody String idCheck(@RequestParam("ckid") String checkId) throws Exception {
      logger.debug("아이디 중복 검사 : {}", checkid);
      int cnt = memberService.idCheck(checkId);
      JSONObject json = new JSONObject();
      json.put("idcount", cnt);
      return json.toString();
  }
  ```



#### 회원 정보 REST

- list.jsp

  ```jsp
  $.ajax({
  	url:'${root}/admin/user',
  	type:'GET',
  	dataType: 'json',
  	...
  })
  ```

  - admin/user로 GET 방식으로 보내지면

- AdminController.java

  ```java
  @Controller // Controller로 인식하게 해줌
  @RequestMapping("/admin") // 여기서 admin으로 받아주고
  @CrossOrigin("*")
  public class AdminController {
      
      private static final Logger logger = LoggerFactory.getLogger(AdminController.class);
      
      @Autowired
      private MemberService memberService;
      
      @RequestMapping(value = "/user", method = RequestMethod.GET, headers = {"Content-type=application/json"}) // 여기서 /user
      
      ...
      
      @RequestMapping(value = "/user", method = RequestMethod.POST, headers = {"Content-type=application/json"})
  }
  ```

  - 이곳에서 mapping되어서 admin/user로 걸러짐

- 그 안에서 listMember를 호출하고

  ```java
  @RequestMapping(value = "/user", method = RequestMethod.GET, headers = {"Content-type=application/json"})
  @ResponseBody ????
  public List<MemberDto> userList() throws Exception {
      List<MemberDto> list = memberService.listMember();
      // 여기서 println 찍으면 members가 list로 나옴
      return null;
  }
  ```

- member.xml

  ```xml
  <mapper namespace="com.ssafy.guestbook.mode.mapper.MemberMapper">
  	...
      
      <select id="listMember" resultType="memberDto">
      	select userid, userpwd, username, email, date_format(joindate, '%y.%m.%d') joindate
          from ssafy_member
          order by joindate desc;
      </select>
  </mapper>
  ```

  - 여기서 유저정보를 list로 넘겨줌

- 이제 AdminController에 json에 정보 넘겨주도록 만들면 됨

  ```java
  @RequestMapping(value = "/user", method = RequestMethod.GET, headers = {"Content-type=application/json"})
  @ResponseBody ????
  public @ResponseBody String userList() throws Exception {
      List<MemberDto> list = memberService.listMember();
  	JsonArray arr = new JSONArray();
      for(MemberDto dto : list) {
          JSONObject json = new JSONObject();
          json.put("userid", dto.getUserId());
          json.put("username", dto.getUserName());
          json.put("userpwd", dto.getUserPwd());
          json.put("email", dto.getEmail());
          json.put("joindate", dto.getJoinDate());
          
          arr.put(json)
      }
      JSONObject obj = new JSONObject();
      obj.put("users", arr);
      return obj.toString();
  }
  ```

- **근데 이렇게 할 필요 없이 AdminController 자체를 @Controller가 아닌 @RestController라고 지정해주면 모든 요소에 대하여 @ResponseBody를 한 효과를 누릴 수있다!(매우 중요)**

  ```java
  @RestController
  @RequestMapping("/admin")
  @CrossOrigin("*")
  public class AdminController {
      
      ...
      
      @RequestMapping(value = "/user", method = RequestMethod.GET, headers = {"Content-type=application/json"})
  	@ResponseBody ????
      public List<MemberDto> userList() throws Exception {
          return memberService.listMember();
      } // 하지만 이러면 json이 아니라 list로 넘어간다.. 나중에 jackson 이용해서 바꿔줄 것!
          
      // public List...(value="/user", method=POST)
      // public MemberDto...
      // 등등등이 밑에 있다..
          
      ...
  }
  ```




#### 회원 목록

- AdminController.java

  ```java
  @RequestMapping(value = "/user", method = RequestMethod.POST, headers = { "Content-type=application/json" })
  public List<MemberDto> userRegister(@RequestBody MemberDto memberDto) throws Exception {
      memberService.registerMember(memberDto);
      return memberService.listMember();
  }
  ```

  - 이러면 admin 로그인하고 회원 목록에서 등록하면 바로 list에 올릴 수 있다(모달 창이 나왔다가 등록 후 사라짐, 새로고침X)

  ```java
  @RequestMapping(value = "/user/{userid}", method = RequestMethod.GET, headers = { "Content-type=application/json" })
  public MemberDto userInfo(@PathVariable("userid") String userid) throws Exception {
      return memberService.getMember(userid);
  }
  ```

  - 이러면 list에서 아이디를 더블클릭하면 회원정보가 뜬다



#### 회원정보 수정

- list.jsp

  ```jsp
  // 회원 정보 수정 보기.
  $(document).on("click", ".modiBtn", function() {
  	let mid = $(this).parents("tr").attr("data-id");
  	$("#view_" + mid).css("display", "none");
  	$("#mview_" + mid).css("display", "");
  });
  
  // 회원 정보 수정 실행.
  $(document).on("click", ".modifyBtn", function() {
  	let mid = $(this).parents("tr").attr("data-id");
  	let modifyinfo = JSON.stringify({
  				"userId" : mid, 
  				"userPwd" : $("#userpwd" + mid).val(), 
  				"email" : $("#email" + mid).val()
  				//"address" : $("#address" + mid).val()
  			   });
  	$.ajax({
  		url:'${root}/admin/user',  
  		type:'PUT',
  		contentType:'application/json;charset=utf-8',
  		dataType:'json',
  		data: modifyinfo,
  		success:function(users) {
  			makeList(users);
  		},
  		error:function(xhr,status,msg){
  			console.log("상태값 : " + status + " Http에러메시지 : "+msg);
  		}
  	});
  });
  
  // 회원 정보 수정 취소.
  $(document).on("click", ".cancelBtn", function() {
  	let mid = $(this).parents("tr").attr("data-id");
  	$("#view_" + mid).css("display", "");
  	$("#mview_" + mid).css("display", "none");
  });
  ```

- AdminController.java

  ```java
  @RequestMapping(value = "/user", method = RequestMethod.PUT, headers = { "Content-type=application/json" })
  public List<MemberDto> userModify(@RequestBody MemberDto memberDto) throws Exception {
      memberService.updateMember(memberDto);
      return memberService.listMember();
  }
  ```



#### 회원 정보 삭제

- list.jsp

  ```jsp
  // 회원 탈퇴.
  $(document).on("click", ".delBtn", function() {
  	if(confirm("정말 삭제?")) {
  		let delid = $(this).parents("tr").attr("data-id");
  		$.ajax({
  			url:'${root}/admin/user/' + delid,  
  			type:'DELETE',
  			contentType:'application/json;charset=utf-8',
  			dataType:'json',
  			success:function(users) {
  				makeList(users);
  			},
  			error:function(xhr,status,msg){
  				console.log("상태값 : " + status + " Http에러메시지 : "+msg);
  			}
  		});
  	}
  });
  ```

- AdminController.java

  ```java
  @RequestMapping(value = "/user/{userid}", method = RequestMethod.DELETE, headers = { "Content-type=application/json" })
  public List<MemberDto> userDelete(@PathVariable("userid") String userid) throws Exception {
      memberService.deleteMember(userid);
      return memberService.listMember();
  }
  ```



#### RestController를 썼을 때

- AdminController.java

  ```java
  @RestController
  @RequestMapping("/admin")
  @CrossOrigin("*")
  public class AdminController {
  
  	private static final Logger logger = LoggerFactory.getLogger(AdminController.class);
  	
  	@Autowired
  	private MemberService memberService;
  
  	@GetMapping("/user")
  	public @ResponseEntity<?> userList() throws Exception {
  		List<MemberDto> list = memberService.listMember();
  		if (list != null && !list.isEmpty()) {
  			return new ResponseEntity<List<MemberDto>>(list, HttpStatus.OK);
  		} else {
  			return new ResponseEntity<Void>(HttpStatus.NO_CONTENT);
  		}
  	}
  	
  	@PostMapping("/user")
  	public ResponseEntity<?> userRegister(@RequestBody MemberDto memberDto) throws Exception {
  		memberService.registerMember(memberDto);
  		return new ResponseEntity<List<MemberDto>>(memberService.listMember(), HttpStatus.OK);
  	}
  	
  	@GetMapping("/user/{userid}")
  	public ResponseEntity<?> userInfo(@PathVariable("userid") String userid) throws Exception {
  		MemberDto memberDto = memberService.getMember(userid);
  		if (memberDto != null) {
  			return new ResponseEntity<MemberDto>(memberDto, HttpStatus.OK);
  		} else {
  			return new ResponseEntity<Void>(HttpStatus.NO_CONTENT);
  		}
  	}
  	
  	@PutMapping("/user")
  	public ResponseEntity<?> userModify(@RequestBody MemberDto memberDto) throws Exception {
  		memberService.updateMember(memberDto);
  		return new ResponseEntity<List<MemberDto>>(memberService.listMember(), HttpStatus.OK);
  //		나중에 int를 return 하는 서비스를 만든다면
  //		int cnt = memberService.updateMember(memberDto);
  //		return new ResponseEntity<Integer>(cnt, HttpStatus.CREATED);
  	}
  	
  	@DeleteMapping("/user/{userid}")
  	public ResponseEntity<?> userDelete(@PathVariable("userid") String userid) throws Exception {
  		memberService.deleteMember(userid);
  		return new ResponseEntity<List<MemberDto>>(memberService.listMember(), HttpStatus.OK);
  	}
  }
  ```



## 배포

> SpringBoot를 사용하지 않는 Spring의 경우 war 파일로 만들어주어야 함
