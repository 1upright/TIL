# Java10

> 자바의 정석 ch10



## 날짜와 시간

- java.util.Date
  - 날짜와 시간을 다룰 목적으로 만들어진 클래스(JDK 1.0)
  - Date의 메서드는 거의 deprecatede되었지만, 여전히 쓰이고 있다
- java.util.Calender
  - Date 클래스를 개선한 새로운 클래스(JDK 1.1) 여전히 단점이 존재
- java.time패키지
  - Date와 Calendar의 단점을 개선한 새로운 클래스 제공(JDK 1.8)



## Calendar 클래스

- 추상 클래스이므로 getInstance()를 통해 구현된 객체를 얻어야 한다

- get()으로 날짜와 시간 필드 가져오기 - int get(int field)

- 정의된 필드

  - 날짜
    - YEAR(년)
    - MONTH(월)
    - WEEK_OF_YEAR(년의 몇 번째 주)
    - WEEK_OF_MONTH(그 달의 몇 번째 주)
    - DATE(일)
    - DAY_OF_MONTH(그 달의 몇 번째 일)
    - DAY_OF_YEAR(그 해의 몇 번째 일)
    - DAY_OF_WEEK(요일)
    - DAY_OF_WEEK_IN_MONTH(그 달의 몇 번째 요일)
  - 시간
    - HOUR(시간(0~11))
    - HOUR(시간(0~23))
    - MINUTE(분)
    - SECOND(초)
    - MILLISECOND(천분의 일초)
    - ZONE_OFFSET(GMT기준 시차)
    - AM_PM(오전/오후)

- 예제

  - set()으로 날짜 설정

    - Calendar date1 = Calendar.getInstance();
    - date1.set(2022, 6, 20);
    - date1set(Calendar.YEAR, 2022);

  - 시간 지정하는 방법

    - Calendar time1 = Calendar.getInstance();
    - time1.set(Calendar.HOUR_OF_DAY, 10);
    - time1.set(Calendar.MINUTE, 20);
    - time1.set(Calendar.SECOND, 30);

  - clear()는 Calendar객체의 모든 필드 초기화

    - Calendar dt = Calendar.getInstance();
    - System.out.println(new Date(dt.getTimeInMillis())); // Tue Aug 29 07:13:03 KST 2017
    - dt.clear();
    - System.out.println(new Date(dt.getTimeInMillis())); // Thu Jan 01 00:00:00 KST 1970

  - clear(int field)는 Calendar객체의 특정 필드 초기화

    ```java
    Calendar dt = Calendar.getInstance();
    
    System.out.println(new Date(dt.getTimeInMillis()));
    
    dt.clear(Calendar.SECOND);
    dt.clear(Calendar.MINUTE);
    dt.clear(Calendar.HOUR_OF_DAY);
    dt.clear(Calendar.HOUR);
    
    System.out.println(new Date(dt.getTimeInMillis()));
    ```

  - add()는 특정 필드의 값을 증가 또는 감소(다른 필드에 영향 O)

    ```java
    Calendar date = Calendar.getInstance();
    date.clear();
    date.set(2020, 7, 31); // 2020년 8월 31일로 설정
    ```

  - roll()은 특정 필드의 값을 증가 또는 감소(다른 필드에 영향 X)

    ```java
    date.set(2020, 7, 31);
    
    date.roll(Calendar.DATE, 1);
    date.roll(Calendar.MONTH, -8);
    ```

  - Date의 메서드는 대부분 deprecated되었지만 여전히 사용

    - Calendar를 Date로 변환

      ```java
      Calendar cal = Calendar.getInstance();
      ...
      Date d = new Date(cal.getTimeInMillis());
      ```

    - Date를 Calendar로 변환

      ```java
      Date d = new Date();
      ...
      Calendar cal = Calendar.getInstance();
      cal.setTime(d)
      ```



## 형식화 클래스

- java.text패키지의 DecimalFormat, SimpleDateFormat
- 숫자와 날짜를 원하는 형식으로 쉽게 출력 가능(숫자, 날짜 => 형식 문자열)
- 형식 문자열에서 숫자와 날짜를 뽑아내는 기능(형식 문자열 => 숫자, 날짜)



#### DecimalFormat

- 숫자를 형식화할 때 사용(숫자 => 형식 문자열)

  ```java
  double number = 1234567.89;
  DeciamlFormat df = new DecimalFormat("#.#E0");
  String result = df.format(number);
  ```

- 특정 형식의 문자열을 숫자로 변환할 때도 사용(형식 문자열 => 숫자)

  ```java
  DecimalFormat df = new DecimalFormat("#,###.##");
  Number num = df.parse("1,234,567.89");
  double d = num.doubleValue()
  ```



#### SimpleDateFormat

- 날짜와 시간을 다양한 형식으로 출력할 수 있게 해준다

  ```java
  Date today = new Date();
  SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd");
  
  String result = df.format(today);
  ```

- 특정 형식으로 되어 있는 문자열에서 날짜와 시간을 뽑아낼 수도 있다

  ```java
  DateFormat df = new SimpleDateFormat("yyyy년 MM월 dd일");
  DateFormat df2 = new SimpleDateFormat("yyyy/MM/dd");
  
  Date d = df.parse("2015년 11월 23일");
  String result = df2.foramt(d);
  ```

- a

  - 오전/오후(AM, PM)

- H

  - 시간(0~23)

- k

  - 시간(1~24)

- K

  - 시간(0~11)

- h

  - 시간(1~12)

- m

  - 분(0~59)

- s

  - 초(0~59)

- S

  - 천분의 일초(0~999)

- z

  - Time zone(General time zone)

- Z

  - Time zone(RFC 822 time zone)

- `

  - escape문자(특수문자 표현에 사용)