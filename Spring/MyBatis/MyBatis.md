# MyBatis

## 개요

- MyBatis는 Java Object와 SQL문 사이의 자동 Mapping 기능을 지원하는 ORM Framework
  - https://blog.mybatis.org
    - 들어가서 한글로 확인 가능
  - SQL을 별도의 파일로 분리해서 관리
  - Object-SQL 사이의 parameter mapping 작업을 자동으로 해줌
  - MyBatis는 Hibernate나 JPA처럼 새로운 DB 프로그래밍 패러다임을 익혀야 하는 부담이 없이, 개발자가 익숙한 SQL을 그대로 이용하면서 JDBC 코드 작성의 불편함을 제거해 주고, 도메인 객체나 VO 객체를 중심으로 개발이 가능
  - 특징
    - 쉬운 접근성과 코드의 간결함
      - 가장 간단한 persistence framework
      - XML형태로 서술된 JDBC 코드라 생각해도 될 만큼 JDBC의 모든 기능을 MyBatis가 대부분 제공
      - 복잡한 JDBC 코드를 걷어내며 깔끔한 소스코드 유지
      - 수동적인 parameter 설정과 Query 결과에 대한 mapping 구문을 제거
    - SQL문과 프로그래밍 코드의 분리
      - SQL에 변경이 있을 때마다 자바 코드를 수정하거나 컴파일하지 않아도 됨
      - SQL 작성과 관리 또는 검토를 DBA와 같은 개발자가 아닌 다른 사람에게 맡길 수 있음
    - 다양한 프로그래밍 언어로 구현가능
      - Java, C#, NET, Ruby



#### mybatis 설정

> MyBatis-3-User-Guide 참고

- mybatis-config.xml
  - environments(속성 부분), mappers(자바와 쿼리문 연결)를 반드시 작성
  - 가이드 대로 베껴오면 됨
  - 순서를 바꾸면 안됨
    - 주석에 있는 주소를 통해 dtd 파일 읽어보면
      - ,는 순서(이래서 안됨)
      - ?는 와도 되고 안와도 되고
      - *은 안와도 되고 하나가 와도 되고 여러개 와도 되고
      - #REQUIRED는 필수다
- dbinfo.properties에 url, dbid, dbpwd를 빼놓았음



## 방명록(MyBatis)

- member.xml 새로만들면

- mybatis-config.xml에 `<mapper resource="member.xml"/>` 집어넣기(member.xml도 읽어라)

- member.xml에 쿼리문 만들기

  - mybatis.org/dtd/mabatis-3.mapper.dtd 관련 DOCTYPE 호출해오면 mapper 자동완성 가능

  ```xml
  <mapper>
  	<insert id="" parameterType="com.ssafy.guestbook.model.MemberDto">
          <!-- mybatis한테 입력하려는 정보가 어디에 있다 정도는 인력해야함 = parameterType -->
      	insert into ssafy_member(user, username, userpwd, email, joindate)
          values(#{userid}, #{userName}, #{userPwd}, #{email}, now())
      </insert>
  </mapper>
  ```

- MemberDaoImpl.java(회원가입)

  ```java
  @Override
  public void registerMember(MemberDto memberDto) throws SQLException {
      try(SqlSession sqlSession = SqlMapConfig.getSqlSession()) {
          sqlSession.insert("com.ssafy.guestbook.model.dao.MemberDao.registerMember", memberDto);
      }
  }
  ```

  - 너무 길어서 수정

    ```java
    private final String NAMESPACE = "com.ssafy.guestbook.model.dao.MemberDao.";
    
    ...
        
    public void registerMember(MemberDto memberDto) throws SQLException {
        try(SqlSession sqlSession = SqlMapConfig.getSqlSession()) {
            sqlSession.insert(NAMESPACE + "registerMember", memberDto);
        }
    }
    ```

- 그대로 두면 db에 저장이 안되어있음

  - SqlMapCongid.java에서 openSession()에 openSession(boolean autoCommit)이 안되어 있으므로!
  - 혹은 MemberDaoImpl.java의 registerMember에 sqlSession.commit();을 붙여주던가
  - 나중에는 registerMember 위에 트랜잭션을 달아줄 것임!

- MemberDto login도 만들어보자

  ```java
  public MemberDto loging(Map<String, String> map) throws SQLException {
      try(SqlSession sqlSession = SqlMapConfig.getSqlSession()) {
          return sqlSession.selectOne(NAMESPACE + "login", map);
      }
  }
  ```

- login은 기본 Alias가 잡혀있음

- member.xml

  ```xml
  <select id="login" parameterType="map" resultType="member">
  <!-- resultType이 Dto 역할 -->
  select usermame, userid, email
  from ssafy_member
  where userid = #{userId} and userpwd = #{userPwd}
  </select>
  ```



## Mapper

- mapper의 namespace(ex : com.ssafy.guestbook.model.dao.MemberDao)는 겹치지 않게 해주세요
- 그 안에 insert, select 등을 해주세요
  - insert/select 등의 id는 mapper가 가지고 있는 메소드 이름으로 맞춰주세요
- mybatis 입장에서 어떤걸 줄건지 parameterType으로 클래스로 풀네임을 넣어주세요(Dto라던지..)
  - 원래는 풀네임 써줘야하는데 너무 기니까 config라는 파일에다 Alias(별칭)을 붙여놔서 설정해주세요
- 마지막으로 태그 안에 쿼리문을 넣어주는데 values의 치환 변수 같은건 #{userId}와 같이 대체해서 써주세요
  - 이들은 각각 property로 설정하면 됨
  - insert의 value들은 MemberDao에서 얻어오니까 getter가 될 것



#### guestbook에서 살펴보기

- GuestBookDaoImpl에서

  - guestbook에 insert하기
  - last_inser_id()를 select해서 articleno에 저장
  - for문을 이용해서 파일 여러개를 집어넣어라

- guestbookDto에 insert 하기전에는 getArticleNo()하면 0이, 하고 난 후에는 1이 출력된다

- guide의 동적 sql을 살펴보면 if, choose(when, otherwise), trim(where, set), foreach 등을 사용할 수 있다

  - foreach를 가장 많이 사용

    ```xml
    <insert id="registerFile" parameterType="guestbook">
    	insert in to file_info (articleno, savefolder, originfile, savefile)
        values
        <foreach collection="fileInfos" item="fileinfo" seperator=", ">
        	(#{articleNo}, #{fileinfo.saveFolder}, #{fileinfo.originFile}, #{fileinfo.saveFile})
        </foreach>
    </insert>
    ```

    ```xml
    <!-- if 쓴다면 이런 느낌-->
    <select id="findActiveBlogWithTitleLike" parmeterType="Blog" resultType="Blog">
    	SELECT * FROM BLOG
        WHERE state = 'ACTIVE'
        <if test="title != null">
        AND title like #{title}
        </if>
    </select>
    ```

- 글 하나당 파일 여러개하려면?

  ```xml
  <resultMap type="guestbook" id="articleList">
      <result column="articleno" property="articleNo"/>
  	<result column="userid" property="userId"/>
      <result column="username" property="userName"/>
      <result column="subjec" property="subject"/>
      <result column="content" property="content"/>
      <result column="regtime" property="regTime"/>
      <collection property="fileInfos" column="articleno=articleno" javaType="list" ofType="fileinfo" select="fileInfoList"/>
      <!-- 이 collection이 fileinfos라는 property에다 articleno인 조건을 만족하는거에다가 list type(형식)으로 집어넣어라. select는 밑에 select 태그 돌려서 집어넣으라는 뜻 -->
  </resultMap>
  ```

- and ${key} = #{word}

  - 값에다가가는 #을, 컬럼을 동적으로 바꿔야하는 경우에는 $를 붙인다
    - 값에다가 $ 넣는것도 가능은 하다

- resultMap="articleList"

  - MyBatis의 가장 중요하고 강력한 기능
  
  - ResultSet에서 데이터를 가져올 때 작성되는 JDBC 코드를 대부분 줄여주는 역할을 담당한다
  
  - join 매핑과 같은 복잡한 코드를 줄이고 복잡한 구문에서 관계 서술
  
  - map을 만들고 컬럼에 있는걸 집어넣는 느낌
  
  - 이걸 쓰면 for문도 돌릴 수 있다는 장점이 생긴다
  
    - for문 때문에 이걸 쓴다? X
  
    ```xml
    <resultMap id="userResultMap" type="User">
    	<id property="id" column="user_id" />
        <result property="username" column="username" />
        <result property="password" column="password" />
    </resultMap>
    ```



## MyBatis-Spring 연동

- 개요

  - MyBatis를 Standalone 형태로 사용하는 경우, SqlSessionFactory 객체를 직접 사용

  - 스프링을 사용하는 경우, 스프링 컨테이너에 MyBatis 관련 빈을 등록하여 MyBatis 사용

  - 스프링에서 제공하는 트랜잭션 기능을 사용하면 손쉽게 트랜잭션 처리

  - MyBatis를 스프링과 연동하기 위해서는 MyBatis에서 제공하는 Spring 연동 라이브러리 필요

  - MyBatis 스프링 연동 라이브러리 의존관계 설정

    ```xml
    <dependency>
    	<groupId>ord.mybatis</groupId>
        <artifactId>mybatis-spring</artifactId>
        <version>2.0.3</version>
    </dependency>
    ```

- DataSource 설정

  - 스프링을 사용하는 경우, 스프링에서 데이터 소스를 관리하므로 MyBatis 설정파일에서는 일부 설정을 생략
  - 스프링 환경 설정파일(application-context.xml)에 데이터소스 설정
  - 데이터소스는 dataSource 아이디를 가진 빈으로 데이터베이스 연결정보를 가진 객체
  - MyBatis와 스프링을 연동하면 데이터베이스 설정과 트랜잭션 처리는 스프링에서 관리

- 트랜잭션 관리자 설정

  - transactionManager 아이디를 가진 빈은 트랜잭션을 관리하는 객체

  - MyBatis는 JDBC를 그대로 사용하기 때문에 DataSourceTransactionManager 타입의 빈을 사용

  - tx:annotation-driven 요소는 트랜잭션 관리방법을 어노테이션으로 선언하도록 설정

  - 스프링은 메소드나 클래스에 @Transactional이 선언되어 있으면, AOP를 통해 트랜잭션 처리

  - 트랜잭션 관리자 설정

    ```xml
    <bean id="transactionManager" class="org.springframewor.jdbc.datasource.DataSourceTransactionManager">
    	<property name="dataSource" ref="dataSource" />
    </bean>
    ```

  - 어노테이션 기반 트랜잭션 설정

    ```xml
    <tx:annotation-driven transaction-manager="transactionManager" />
    ```

- SqlSessionFactoryBean 설정

  - MyBatis 애플리케이션은 SqlSessionFactory를 중심으로 수행

  - 스프링에서 SqlSessionFactory 객체를 생성하기 위해서는 SqlSessionFactoryBean을 빈으로 등록해야 함

  - SqlSessionFactoryBean을 빈으로 등록할 때, 사용할 데이터소스와 mybatis 설정파일 정보가 필요

    ```xml
    <bean id="sqlSessionFactoryBean" class="org.mybatis.spring.SqlSessionFactoryBean">
    	<property name="dataSource" ref="dataSource" />
        <property name="configLocation" ref="classpath:com/cafe/config/mybatis/mybatis-config.xml" />
        <property name="mapperLocations">
        	<list>
            	<value>classpath:com/cafe/config/mybatis/admin_board.xml</value>
                <value>classpath:com/cafe/config/mybatis/admin_member.xml</value>
                <value>classpath:com/cafe/config/mybatis/admin_poll.xml</value>
            </list>
        </property>
    </bean>
    ```

- mapper 빈 등록

  - Mapper 인터페이스를 사용하기 위해선 스캐너를 사용하여 자동으로 등록하거나, 직접 빈으로 등록

  - mapperScannerConfigurer을 설정하면, Mapper 인터페이스를 자동으로 검색하여 빈으로 등록

    - basePackage로 패키지를 설정하면, 해당 패키지 하위 모든 매퍼 인터페이스가 자동으로 등록

  - MapperFactoryBean 클래스는 매퍼 인터페이스를 직접 등록할 때 사용

    ```xml
    <!-- 방법 1. mapper scanner 사용 -->
    <bean id="mapperScannerConfigurer" class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    	<property name="basePackage" value="com.ssafy.edu.mybatis.mapper" />
    </bean>
    ```

    ```xml
    <!-- 방법 2. mapper interface 직접 등록 -->
    <bean id="authorMapper" class="org.mybatis.spring.mapper.MapperFactoryBean">
    	<property name="mapperInterface" value="com.ssafy.edu.mybatis.mapper.AuthorMapper" />
        <property name="sqlSessionFactory" ref="sqlSessionFactory" />
    </bean>
    ```

- MyBatis Configuration

  - 스프링을 사용하면 DB 접속정보 및 Mapper 관련 설정은 스프링 빈으로 등록하여 관리
  - 따라서 MyBatis 환경설정 파일에는 스프링에서 관리하지 않는 일부 정보만 설정
    - typeAlias, typeHandler 등

- 데이터 접근 객체 구현

  - 데이터 접근객체는 특정한 기술을 사용하여 데이터 저장소에 접근하는 방식을 구현한 객체
  - @Repository는 데이터 접근 객체를 빈으로 등록하기 위해서 사용하는 스프링에서 제공하는 어노테이션
  - @Autowired 어노테이션을 통해 사용하려는 Mapper 인터페이스를 데이터접근 객체와 의존관계 설정