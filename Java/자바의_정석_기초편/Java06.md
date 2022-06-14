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



#### 메서드의 호출

```java
print99danAll(); // void print99danAll()을 호출
int result = add(3, 5); // int add(int x, int y)를 호출하고, 결과를 result에 저장
```

```java
class Ex {
    public static void main(String args[]) {
        MyMath mm = new MyMath(); // 1. 인스턴스 생성
        long result = mm.add(5, 3); // 2. 메서드 호출
        
        System.out.println("add(5L, 3L) = " + result)
    }
}

class MyMath {
    long add(long a, long b) {
        long result = a + b;
        return result;
    }
}
```



#### return문

- 실행 중인 메서드를 종료하고 호출한 곳으로 되돌아간다

- 반환 타입이 void가 아닌 경우 반드시 return문 필요

  ```java
  int max(int a, int b) {
      if (a > b)
          return a;
  } // 특정한 조건에서 return이 없으므로 에러
  ```

- 그냥 return; 이거는 생략 가능



#### 호출 스택

- 스택 : 밑이 막힌 상자. 위에 차곡차곡 쌓인다
- 호출 스택
  - 메서드 수행에 필요한 메모리가 제공되는 공간
  - 메서드가 호출되면 호출스택에 메모리 할당, 종료되면 해제
  - 아래 있는 메서드가 위의 메서드를 호출한 것
  - 맨 위 메서드 하나만 실행 중, 나머지는 대기 중
  - (함수 안의 함수)



#### 기본형 매개변수

- 기본형 - 변수의 값을 읽기만 할 수 있다(read only)

  ```java
  class Data {int x; }
  
  class Ex {
      public static void main (string[] args) {
          Data d = new Data();
          d.x = 10;
          System.out.println("main() : x = " + d.x);
          
          change(d.x);
          System.out.println("After change(d.x)");
          System.out.println("main() : x = " + d.x);
      }
      
      static void change(int x) { // 기본형 매개변수
          x = 1000;
          System.out.println("change() : x = " + x);
      }
  }
  ```

  main() : x = 10

  change() : x = 1000

  After change(d.x)

  main() : x = 10

- 참조형 - 변수의 값을 읽고 변경할 수 있다(read & write)

  ```java
  class Data {int x; }
  
  class Ex {
      public static void main (string[] args) {
          Data d = new Data();
          d.x = 10;
          System.out.println("main() : x = " + d.x);
          
          change(d);
          System.out.println("After change(d)");
          System.out.println("main() : x = " + d.x);
      }
      
      static void change(Data d) { // 참조형 매개변수
          d.x = 1000;
          System.out.println("change() : x = " + d.x);
      }
  }
  ```

​		main() : x = 10

​		change() : x = 1000

​		After change(d)

​		main() : x = 1000

- 참조형 반환타입

  ```java
  class Data {int x; }
  
  class Ex {
      public static void main (string[] args) {
          Data d = new Data();
          d.x = 10;
          System.out.println("main() : x = " + d.x);
          
          Data d2 = copy(d);
          System.out.println("d.x = "+d.x);
          System.out.println("d2.x = "+d2.x);
      }
      
      static Data copy(Data d) { // 반환 타입이 참조형
          Data tmp = new Data(); // 새로운 객체 tmp 생성
          tmp.x = d.x; // d.x의 값을 tmp.x에 복사
          return tmp; // 복사한 객체의 주소 반환
      }
  }
  ```
  
  d.x = 10
  
  d2.x = 10

#### Static 메서드와 인스턴스 메서드

- static 메서드 : 메서드 앞에 static이 붙은거(클래스 메서드)
  - 객체 생성 없이 '클래스이름.메서드이름()'으로 호출
  - 인스턴스 멤버(iv, im)와 관련없는 작업을 하는 메서드
  - 메서드 내에서 인스턴스 변수(iv) 사용불가
- 인스턴스 메서드
  - 인스턴스 생성 후, '참조변수.메서드이름()'으로 호출
  - 인스턴스 멤버(iv, im)와 관련된 작업을 하는 메서드
  - 메서드 내에서 인스턴스 변수(iv) 사용 가능

```java
class MyMath {
    long a, b; // 인스턴스 변수
    
    long add() {
        return a+b;
    } // 인스턴스 메서드
    
    static long add(long a, long b) {
        return a+b;
    } // static 메서드
}
```

```java
System.out.println(MyMath.add(200L, 100L)); // 클래스 메서드 호출
MyMath mm = new MyMath(); // 인스턴스 생성
mm.a = 200L;
mm.b = 100L;
System.out.println(mm.add()); // 인스턴스 메서드 호출
```

- 객체 == iv 묶음
- 메서드 == 명령문 묶음

- static을 언제 붙여야할까?
  - 속성(멤버 변수) 중에서 공통 속성에 static을 붙인다
  - **인스턴스 멤버(iv, im)을 사용하지 않는 메서드에 static을 붙인다**

```java
class Test {
    int iv; // 인스턴스 변수
    static int cv; // 클래스 변수
    
    void instanceMethod() { // 인스턴스 메서드
        System.out.println(iv); // 인스턴스 변수 사용 가능
        System.out.println(cv); // 클래스 변수 사용 가능
    }
    
    static void staticMethod() { // static 메서드
        System.out.println(iv); // 에러!!! 인스턴스 변수 사용 불가
        System.out.println(cv); // 클래스 변수 사용 가능
    }
} // static 메서드가 호출되었을 때 인스턴스 변수가 있을지 없을지 확인할 수 없어서 못씀
```



#### 오버로딩

> 한 클래스 안에 같은 이름의 메서드 여러 개 정의하는 것(메서드 오버로딩)

- 오버로딩 성립 조건

  - 메서드 이름이 같아야 한닫

  - 매개변수의 개수 또는 타입이 달라야 한다

  - 반환 타입은 영향 없다

    ```java
    int add(int a, int b) { return a+b; }
    int add(int x, int y) { return x+y; }
    // 오버로딩이 X, 메서드 중복 정의한 것
    // 에러 : add(int, int) is already defined
    ```

    ```java
    int add(int a, int b) { return a+b; }
    long add(int a, int b) { return (long)a+b; }
    // 오버로딩이 X, 반환 타입이 다를 뿐 메서드 중복 정의가 됨
    ```

    ```java
    long add(int a, long b) { return a+b; }
    long add(long a, int b) { return a+b; }
    // 오버로딩 O
    // add(3, 3)을 해버리면 에러 : 어떤 메서드를 호출한건지 알수가 없음(ambiguous)
    ```

    

#### 생성자

- 인스턴스가 생성될 때마다 호출되는 '인스턴스 초기화 메서드'

- 인스턴스 생성시 수행할 작업(iv 초기화)에 사용

  ```java
  Time t = new Time(12, 34, 56);
  ```

- iv 초기화를 편리하게 하려고 사용하는 메서드

- 조건

  - 이름이 클래스 이름과 같아야 한다

  - 리턴값이 없다(void 안붙임)

  - 모든 클래스는 반드시 생성자를 가져야 한다

    ```java
    class Card {
        ...
        Card () { // 매개변수 없는 생성자
            // 인스턴스 초기화 작업
        }
        
        Card(String kind, int number) { // 매개변수 있는 생성자
            // 인스턴스 초기화 작업
        }
    }
    ```

- 기본 생성자

  - 매개변수가 없는 생성자

  - 생성자가 하나도 없을 때만 컴파일러가 자동 추가

    ```java
    class Data {
        int value;
        // Data() {} // 기본 생성자를 컴파일러가 넣어줌
    }
    class Data2 {
        int value;
        // (1)
        Data2(int x) { // 매개변수가 있는 생성자
            value = x
        }
    }
    
    class Ex {
        public static void main(String[] args) {
            Data d1 = new Data(); // 생성자가 없어서 기본 생성자가 추가되어 error를 피함
            Data2 d2 = new Data2(); // compile error 발생
        } // error 없애려면 Data2의 (1) 위치에 기본생성자를 추가해야함
    }
    ```

- 매개변수가 있는 생성자

  ```java
  class Car {
      String color;
      String gearType;
      int door;
      
      Car() {} // 기본 생성자
      Car(String c, String g, int d) { // 매개변수가 있는 생성자
          color = c;
          gearType = g;
          door = d;
      }
  }
  ```

  - Car c = new Car("white", "auto", 4);
    - Car c : 참조변수
    - new 연산자 : 객체생성
    - white, auto, 4 : 객체초기화(생성자 호출)
    - = : 대입



#### 생성자 this()

> 생성자에서 다른 생성자 호출할 때 사용

- 다른 생성자 호출시 첫 줄에서만 사용 가능

```java
class Car {
    String color;
    String gearType;
    int door;
    
    Car() {
        this("white", "auto", 4);
    }
    
    Car(String color) {
        this(color, "auto", 4);
    }
    
    Car(String color, String gearType, int door) {
        this.color = color;
        this.gearType = gearType;
        this.door = door;
    }
}
```



#### 참조변수 this

> 인스턴스 자신을 가리키는 참조변수

- 인스턴스 메서드(생성자 포함)에서 사용가능

- 지역변수(lv)와 인스턴스 변수(iv)를 구별할 때 사용

  ```java
  Car(String color, String gearType, int door) {
      this.color = color;
      this.gearType = gearType;
      this.door = door;
      // this.iv = lv;
  }
  ```

  

#### 생성자 this() vs 참조변수 this

- this

  - 인스턴스 자신을 가리키는 참조변수. 인스턴스의 주소가 저장되어 있다
  - 모든 인스턴스메서드에 지역변수로 숨겨진 채로 존재한다

- this(), this(매개변수)

  - 생성자. 같은 클래스의 다른 생성자를 호출할 때 사용한다

- this와 this()는 비슷하게 생겼을 뿐 완전히 다른 것이다

  ```java
  class MyMath {
      long a, b; // this.a, this.b => iv의 진짜 이름
      
      MyMath(int a, int b) {
          this.a = a;
          this.b = b; // this 생략 불가
      }
      long add() {
          return a + b; // return this.a + this.b 사용, 생략 가능
      }
      static long add(long a, long b) { // 클래스 메서드(static 메서드)
          return a + b;
      }
  }
  ```

  

#### 변수의 초기화

- 지역변수(lv)는 수동 초기화 해야함(사용전 꼭!!)

- 멤버변수(iv, cv)는 자동 초기화된다

  - 전부 0으로 초기화됨

  ```java
  class Init {
      int x; // 인스턴스 변수 => 자동초기화
      int y = x; // 인스턴스 변수
      
      void method() {
          int i; // 지역 변수 => 수동초기화
          int j = i; // 에러!! 지역변수를 초기화하지 않고 사용
      }
  }
  ```

- 멤버변수 초기화 방법

  - 명시적 초기화(=)

    ```java
    class Car {
        int door = 4; // 기본형 변수의 초기화
        Engine e = new Engine(); // 참조형 변수의 초기화
    }
    ```

  - 초기화 블럭(복잡한 초기화할 때)

    - 인스턴스 초기화 블럭 : {}
      - 여러문장 넣기
      - iv 초기화 할때
    - 클래스 초기화 블럭 : static {}
      - cv 초기화 할때

  - 생성자(iv 초기화, 복잡한 초기화할 때)

    ```java
    Car(String color, String gearType, int door) {
        this.color = color;
        this.gearType = gearType;
        this.door = door;
    }
    ```

  - 요약

    - iv일때는 생성자, cv일때는 static {} 쓴다, 간단초기화는 명시적 초기화

  - 클래스 변수 초기화 시점 : 클래스가 처음 로딩될 때 한번

  - 인스턴스 변수 초기화 시점 : 인스턴스가 생성될 때  마다