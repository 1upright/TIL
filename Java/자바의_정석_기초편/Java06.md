# Java06

> 자바의 정석 ch06



## 객체 지향 언어

- 코드의 재사용성이 높고 유지보수가 용이, 중복 코드 제거
- 프로그래밍 언어 + 객체지향개념(규칙)
- 핵심 개념
  - 캡슐화
  - 상속
  - 추상화
  - 다형성
- 설계에 대한 내용



#### 클래스와 객체

- 클래스
  - 객체를 정의해 놓은 것
  - 객체를 생성하는데 사용
  - 클래스란?
    - 설계도
    - 데이터 + 함수
    - 사용자의 정의 타입
- 객체
  - 실제로 존재하는 것. 사물 또는 개념
  - 객체가 가지고 있는 기능과 속성에 따라 다름
- 정의 1) 클래스는 설계도다
  - 클래스 : 객체 = 설계도 : 제품

```JAVA
class TV {
    String color; // 색깔
    boolean power; // 전원상태
    int chnnel; // 채널
    // 이들은 변수
    
    void power() { power = !power; }
    void channelUp() { channel++; }
    void channelDown() { channel--; }
    // 이들은 메서드
}
```

- 객체와 인스턴스
  - 객체 : 모든 인스턴스를 대표하는 일반적 용어
  - 인스턴스 : 특정 클래스로부터 생성된 객체
  - (대충 같다고 이해하자)
- 클래스 =>인스턴스화=> 인스턴스(객체)
- 이해를 돕기 위해
  - 클래스(설계도)가 왜 필요해? => 객체(TV)를 생성하기 위해
  - 객체(TV)가 왜 필요해? => 객체(TV)를 사용하려고
  - 객체(TV)를 사용한다는 것은? => 객체(TV)가 가진 속성(변수)과 기능(메서드)을 사용하려고



#### 하나의 소스파일에 여러 클래스 작성

```java
// Hello2.java
public class Hello2 {} // public class가 있는 경우 소스파일의 이름은 반드시 public class 이름과 일치
class Hello3 {}

// Hello3.java
class Hello2 {} // public class가 없는 경우 소스파일의 이름은 Hello2.java, Hello3.java 모두 가능
class Hello3 {}
```

- public class가 두개면 에러
- public class와 소스파일의 이름이 불일치하면 에러
- 대소문자를 구분하기 때문에 이름의 대소문자가 다르면 불일치하는 것으로 보고 에러



#### 객체의 생성과 사용

1. 생성

   - 클래스명 변수명;

   - 변수명 = new 클래스명();

     ```java
     Tv t;
     t = new TV();
     ```

2. 사용

   ```java
   t.channel = 7;
   t.channelDown();
   System.out.println("현재 채널 : "+t.channel);
   ```

- 하나의 인스턴스를 여러개의 참조변수가 가리키는 경우 => 가능
- 여러 인스턴스를 하나의 참조변수가 가리키는 경우 => 불가능

```java
class Ex {
    public static void main(String args[]) {
        Tv t;
        t = new Tv();
        t.channel = 7;
        t.channelDown();
        System.out.println("현재 채널은 " + t.channel + "입니다.");
    }
}

class Tv {
    String color;
    boolean power;
    int channel;
    
    void power() { power = !power; }
    void channelUp() { ++channel; }
    void channelDown() { --channel; }
}
```



#### 객체 배열

> 참조변수 배열

- `Tv tv1, tv2, tv3;` => `Tv[] tvArr = new Tv[3];`



## 클래스의 정의

- 정의 2) 클래스는 데이터 + 함수다

  - 변수 : 하나의 데이터를 저장할 수 있는 공간
  - 배열 : 같은 종류의 여러 데이터를 하나로 저장할 수 있는 공간
  - 구조체 : 서로 관련된 여러 데이터를 하나로 저장할 수 있는 공간
  - 클래스 : 데이터와 함수의 결합(구조체 + 함수)

- 정의 3) 클래스는 사용자 정의 타입이다

  - 원하는 타입을 직접 만들 수 있다

  - 시간 관련 타입을 만든다고 가정

    - int hour; int minute; int second;

    - int hour1, hour2, hour3

      int minute1, minute2, minue3

      int second1, second2, second3

    - int[] hour = new int[3];

      int[] minute = new int[3];

      int[] second = new int[3];

    - class Time {

      ​	int hour;

      ​	int minute;

      ​	int second;

      }

    - Time t = new Time();

      t.hour = 12; t.minute = 34; t.second = 56;



#### 선언 위치에 따른 변수 종류

```java
class Variables {
    int iv; // 인스턴스 변수
    static int cv; // 클래스 변수(static 변수, 공유 변수)
    
    void method() {
        int lv = 0; // 지역 변수
    } // *메서드 영역
} // *클래스 영역
```

| 변수의 종류   | 선언 위치               | 생성 시기                   |
| ------------- | ----------------------- | --------------------------- |
| 클래스 변수   | 클래스 영역             | 클래스에 메모리가 올라갈 때 |
| 인스턴스 변수 | 클래스 영역             | 인스턴스가 생성되었을 때    |
| 지역변수      | 클래스 영역 이외의 영역 | 변수 선언문이 수행되었을 때 |



#### 클래스 변수와 인스턴스 변수

- Card 객체
  - 속성
    - 숫자(개별적)
    - 무늬(개별적)
    - 폭(공통적)
    - 높이(공통적)
  - 기능

- 공통적인 속성은 cv로(쓰면서 static을 붙여줌) 개별적인 속성은 iv로 한다

  ```java
  class Card {
      String kind; // 무늬
      int number; // 숫자
      
      static int width = 100; // 폭
      static int height = 250; // 높이
  }
  ```



#### 메서드란?

> 문장들을 묶어놓은 것

- 하나의 작업을 하는 코드를 묶어놓은 후 이름을 붙여주면 메서드
- 정의?
  1. 문장을 묶은 것
  2. 값(입력)을 받아서 처리하고, 결과를 반환(출력)

- 메서드 장점

  - 코드 중복을 줄일 수 있다
  - 코드 관리가 쉽다
  - 코드 재사용할 수 있다
  - 코드가 간결해서 이해하기 쉬워진다

- 메서드 작성

  - 반복적으로 수행되는 여러 문장을 메서드로 작성
  - 하나의 메서드는 한 가지 기능만 수행하도록 작성

- 메서드 구성

  - 선언부
    - 반환 타입
    - 메서드 이름
    - 매개변수(입력)
  - 구현부
    - 메서드 호출시 수행될 코드

  ```java
  int add (int a, int b): // "타입" "이름" "매개변수"
  {
      int result = a + b;
      return result; // 수행될 코드
  }
  ```

- void : 없다(반환값이 없을 때 사용)

- 구현부에 지역변수가 있음

  - 호출 이후 사라짐
  - 이름이 겹쳐도 상관없음
  - 매개변수도 지역변수임