# Java07

> 자바의 정석 ch07



## 상속

- 기존의 클래스로 새로운 클래스를 작성하는 것(코드의 재사용)

- 두 클래스를 부모와 자식으로 관계 맺어주는 것

- 자손은 조상의 모든 멤버를 상속받는다(생성자, 초기화블럭 제외)

- 자손의 멤버 개수는 조상보다 적을 수 없다(같거나 많다)

  ```java
  class Parent {
      int age; // 멤버 1개
  }
  
  class Child extends Parent {} // 멤버 1개(상속받음)
  ```

- 자손의 변경은 조상에 영향을 미치지 않는다

  ```java
  class Parent {
      int age; // 멤버 1개
  }
  
  class Child extends Parent {
      void play() {
          System.out.println("놀자~")
      }
  } // 멤버 2개(자신 1개 + 상속받은거 1개)
  ```

```java
class Tv {
    boolean power;
    int channel;
    
    void power() { power = !power }
    void channelUp() { ++channel; }
    void channelDown() { --channel; }
} // 멤버 5개

class SmartTv extends Tv {
    boolean caption;
    void displayCaption(String text) {
        if (caption) {
            System.out.println(text);
        }
    }
} // 멤버 7개 = 5개 + 2개

class Ex {
    putblic static void main(String args[]) {
        SmartTv stv = new SmartTv();
        stv.channel = 10;
        stv.channelUp();
        System.out.println(stv.channel);
        stv.displayCaption("Hello, World");
        stv.caption = true;
        stv.displayCaption("Hello, World");
    }
}
```



## 포함 관계

- 클래스의 멤버로 참조변수를 선언하는 것

- 작은 단위의 클래스를 만들고 이들을 조합해서 클래스를 만든다

- 클래스 간의 관계 결정하기

  - 상속 : A는 B이다 (is-a)

    - 꼭 필요할 때만

    ```java
    class Circle extends Point {
        int r;
    }
    ```

  - 포함 : A는 B를 가지고 있다 (has-a)

    - 90%가 포함으로 함

    ```java
    class Circle {
        Point c = new Point();
        int r;
    }
    ```

```java
class MyPoint {
    int x;
    int y;
}

class Circle extends MyPoint {
    MyPoint p = new MyPoint();
    int r;
}

public class InheritanceTest {
    public static void main(String[] args) {
        Circle c = new Circle();
        c.p.x = 1;
        c.p.y = 2;
        c.r = 3;
        System.out.println("c.p.x="c.x);
        System.out.println("c.p.y="c.y);
        System.out.println("c.z="c.z);
    }
}
```



## 단일 상속

- Java는 단일상속만을 허용한다(C++은 다중상속 허용)

  ```java
  class TvDVD extends Tv, DVD {} // 에러!! 조상은 하나만 허용
  ```

- 비중이 높은 클래스 하나만 상속관계로, 나머지는 포함관계로 한다

  ```java
  class TvDVD extends Tv {
      DVD dvd = new DVD();
      ...
  }
  ```



## Object 클래스

> 모든 클래스의 조상

- 부모가 없는 클래스는 자동적으로 Object 클래스를 상속받게 된다

  ```java
  class Tv {} // == class Tv extends Object{}
  ```

- 모든 클래스는 Object클래스에 정의된 11개의 메서드를 상속받는다

  - ex) toString(), equals() ...



## 오버라이딩

> 상속받은 조상의 메서드를 자신에 맞게 변경하는 것

- 내용(구현부)만 변경 가능, 선언부 변경불가

```java
class Point {
    int x;
    int y;
    
    String getLocation() {
        return "x :" + x + ", y :" + y;
    }
}

class Point3D extends Point {
    int z;
    
    String getLocation() {
        return "x :" + x + ", y :" + y + ", z :" + z;
    } // 이거 안했으면 결과가 x, y만 나옴
}

public class OverrideTest {
    public static void main(Strint[] args) {
        MyPoint3D p = new MyPoint3D();
        p.x = 3;
        p.y = 5;
        p.z = 7;
        System.out.println(p.getLocation()); // x :3, y :5
    }
}
```

```java
class MyPoint extends Object {
    int x;
    int y;
    
    MyPoint(int x, int y){
        this.x = x;
        this.y = y;
    }
    
    Public String toString() {
        return "x :" + x + ", y :" + y;
    }
}

public class OverrideTest {
    public static void main(String[] args) {
        MyPoint p = new MyPoint(3, 5);
        System.out.println(p);
    }
}
```

- 조건

  - 선언부가 조상 클래스의 메서드와 일치해야 한다
  - 접근 제어자를 조상 클래스의 메서드보다 좁은 범위로 변경할 수 없다
  - 예외는 조상 클래스의 메서드보다 많이 선언할 수 있다

- 오버로딩 vs 오버라이딩

  - 오버로딩 : 기존에 없는 새로운 메서드를 정의하는 것

  - 오버라이딩 : 상속받은 메서드의 내용을 변경하는 것

    ```java
    class Parent {
        void parentMethod() {}
    }
    
    class Child extends Parent {
        void parentMethod() {} // 오버라이딩
        void parentMethod(int i) {} // 오버로딩
        
        void childMethod() {} // 메서드 정의
        void childMethod(int i) {} // 오버로딩
        void childMethod() {} // 중복 정의
    }
    ```



## 참조변수 super

- 객체 자신을 가리키는 참조변수. 인스턴스 메서드 내에서만 존재
- 조상의 멤버를 자신의 멤버와 구별할 때 사용

```java
class Ex {
    public static void main(String args[]) {
        Child c = new Child();
        c.method();
    }
}

class Parent { int x = 10; }

class Child extends Parent {
    int x = 20;
    
    void method() {
        System.out.println("x=" + x); // 20
        System.out.println("this.x=" + this.x); // 20
        System.out.println("super.x=" + super.x); // 10
    }
}

class Child2 extends Parent {
    void method() {
        System.out.println("x=" + x); // 10
        System.out.println("this.x=" + this.x); // 10
        System.out.println("super.x=" + super.x); // 10
    }
}
```



#### super()

> 조상의 생성자

- 조상의 생성자를 호출할 때 사용
- 조상의 멤버는 조상의 생성자를 호출해서 초기화
- 조건 : **생성자의 첫 줄에 반드시 생성자를 호출해야 한다(super(), this())**
  - 그렇지 않으면 컴파일러가 생성자의 첫 줄에 super(); 삽입

```java
class Point {
    int x, y;
    
    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Point3D extends Point {
    int z;
    
    Point3D(int x, int y, int z) {
        super(x, y);
        this.z = z;
    }
}
```



## 패키지

> 서로 관련된 클래스의 묶음

- 클래스는 클래스 파일, 패키지는 폴더. 하위 패키지는 하위 폴더
- 클래스의 실제 이름은 패키지를 포함(java.lang.String)
- rt.jar는 클래스들을 압축한 파일(JDK설치경로\jre\lib에 위치)
  - java 9부터 없어짐



#### 패키지 선언

- 패키지는 소스파일의 첫 번째 문장으로 단 한번 선언
- 같은 소스 파일의 클래스들은 모두 같은 패키지에 속하게 된다
- 패키지 선언이 없으면 이름없는 패키지에 속하게 된다



## 클래스 패스

- 클래스 파일의 위치를 알려주는 경로
- 환경변수 classpath로 관리하며, 경로간의 구분자는 ';'를 사용
- classpath(환경변수)에 패키지의 루트를 등록해줘야 함



## import 문

- 클래스를 사용할 때 패키지 이름을 생략할 수 있다

- 컴파일러에게 클래스가 속한 패키지를 알려준다

- java.lang패키지의 클래스는 import하지 않고도 사용할 수 있다

  - String, Object, System, Thread

    ```java
    import java.lang.*;
    
    class ImportTest
    {
        public static void main(String[] args) // 여기서 String 
        {
            System.out.println("Hello World!");
        }
    }
    ```

- `import 패키지명.클래스명;` or `import 패키지명.*;`

- import 문은 패키지문과 클래스선언의 사이에 선언한다

- import문은 컴파일 시에 처리되므로 프로그램 성능에 영향없음

  - import java.util.*; 해도 성능 똑같고 시간 차이 많이 없음

- 이름이 같은 클래스가 속한 두 패키지를 import할 때는 클래스 앞에 패키지명을 붙여줘야 한다



#### static import 문

- static 멤버를 사용할 때 클래스 이름을 생략할 수 있게 해준다

  ```java
  import static java.lang.Integer.*;
  import static java.lang.Math.random;
  import static java.lang.System.out;
  ```

  ```java
  import static java.lang.System.out;
  import static java.lang.Math.*;
  
  class Ex {
      public static void main(Strint[] args) {
          out.println(random());
          
          out.println("Math.PI :" + PI);
      }
  }
  ```



## 제어자

- 클래스와 클래스의 멤버(멤버 변수, 메서드)에 부가적인 의미 부여

- 접근 제어자

  - public, protected, (default), private

- 그 외

  - static, final, abstract, native, transient, synchronized, volatile, strictfp

- 하나의 대상에 여러 제어자를 같이 사용가능(접근 제어자는 하나만)

  ```java
  public class ModifierTest {
      public static final int WIDTH = 200;
      
      public static void main(String[] args) {
          System.out.println("WIDTH="+WIDTH);
      }
  }
  ```

- static - 클래스의, 공통적인

  - 멤버변수
  - 메서드

- final - 마지막의, 변경될 수 없는

  - 클래스
  - 메서드
  - 멤버변수
  - 지역변수

  ```java
  final class FinalTest { // 조상이 될 수 없는 클래스
      final int MAX_SIZE = 10; // 값을 변경할 수 없는 멤버변수(상수)
      
      final void getMaxSize() { // 오버라이딩 할 수 없는 메서드(변경불가)
          final int LV = MAX_SIZE; // 값을 변경할 수 없는 지역변수(상수)
          return MAX_SIZE;
      }
  }
  ```

- abstract - 추상의, 미완성의

  - 클래스
  - 메서드

  ```java
  abstract class AbstractTest { // 추상 클래스(추상 메서드를 포함한 클래스)
      abstract void move(); // 추상 메서드(구현부가 없는 메서드)
  }
  ```

  - 미완성 메서드임
  - 추상 클래스의 인스턴스 생성 불가
  - 추상클래스를 상속받아서 완전한 클래스를 만든 후에 객체 생성 가능

  

## 접근 제어자

> 4개중에 한개만 선택할 수 있다

- private : 같은 클래스 내에서만 접근이 가능하다
- (default) : 같은 패키지 내에서만 접근이 가능하다
- protected : 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스의 접근이 가능하다
- public : 접근 제한이 없다

```java
package pkg1;

public class MyParent { // 접근제어자가 public (MyParent.java파일이어야 함)
    private 	int prv;
    			int dft;
    protected 	int prt;
    public 		int pub;
    
    public void printMembers() {
        System.out.println(prv);
        System.out.println(dft);
        System.out.println(prt);
        System.out.println(pub);
    }
}

class MyParentTest { // 접근 제어자가 (default)
    public static void main(String[] args) {
        MyParent p = new MyParent();
        System.out.println(p.prv); // 에러
        System.out.println(p.dft); // OK
        System.out.println(p.prt); // OK
        System.out.println(p.pub); // OK
    }
}
```

```java
package pkg2;

// import pkg1.MyParent; // ctrl+shift+o

class MyChild extends pkg1.MyParent {
    public void printMembers() {
        MyParent p = new MyParent();
        System.out.println(p.prv); // 에러
        System.out.println(p.dft); // 에러
        System.out.println(p.prt); // OK
        System.out.println(p.pub); // OK
    }
}

public class MyParentTest2 {
    public static void main(String[] args) {
        MyParent p = new MyParent();
        System.out.println(p.prv); // 에러
        System.out.println(p.dft); // 에러
        System.out.println(p.prt); // 에러
        System.out.println(p.pub); // OK
    }
}
```



## 캡슐화

- 접근 제어자를 사용하는 이유

  - 외부로부터 데이터를 보호하기 위해서

    ```java
    public class Time {
        private int hour; // 외부접근을 막는다. 메서드는 public
        private int minute;
        private int second;
        
        public int getHour() { return hour; }
        
        public void setHour(int hour) {
            if (hour < 0 || hour > 23) return;
            this.hour = hour;
        }
    }
    
    public class TimeTest {
        public static void main(String[] args) {
            Time t = new Time();
            
            t.sethour(21);
            System.out.println(t.getHour());
            t.sethour(100);
            System.out.println(t.getHour()); // 21이 두번 찍힘
        }
    }
    ```

  - 외부에는 불필요한, 내부적으로만 사용되는 부분을 감추기 위해서

    ```java
    public class Time {
        private int hour;
        private int minute;
        private int second;
        
        public int getHour() { return hour; }
        
        public void setHour(int hour) {
            if (isUnvalidHour(hour)) return;
            
            this.hour = hour;
        }
        
        private boolean isUnvalidHour(int hour) {
            return hour <0 || hour > 23;
        }
    
    }
    
    public class TimeTest {
        public static void main(String[] args) {
            Time t = new Time();
            
            t.sethour(21);
            System.out.println(t.getHour());
            t.sethour(100);
            System.out.println(t.getHour());
    }



## 다형성

- 여러가지 형태를 가질 수 있는 능력

- 조상 타입 참조 변수로 자손 타입 객체를 다루는 것

  ```java
  SmartTv s = new SmartTv(); // 참조변수와 인스턴스 타입이 일치
  Tv t = new SmartTv(); // 조상 타입 참조변수로 자손 타입 인스턴스 참조
  ```

- 자손 타입의 참조변수로 조상 타입의 객체를 가리킬 수 없다

  ```java
  Tv t = new SmartTv(); // OK
  SmartTv s = new Tv(); // 에러
  ```

  - 조상 7개 자손 5개면 2개 안쓰면 되지만 조상 5개 자손 7개면 에러가 남

- 참조변수의 타입은 인스턴스의 타입과 반드시 일치?

  - 보통 일치하지만 아닐 수도 있음

- 참조변수가 조상타입일 때와 자손타입일 때의 차이?

  - 참조변수로 사용할 수 있는 멤버의 개수가 달라짐

- 자손 타입의 참조변수로 조상 타입의 객체를 가리킬 수 있나요?

  - 허용되지 않음




## 참조변수의 형변환

- 사용할 수 있는 멤버의 개수를 조절하는 것

- 조상 자손 관계의 참조변수는 서로 형변환 가능

  ```java
  FireEngine f = new FireEngine();
  
  Car c = (Car)f; // OK. 조상입 Car타입으로 형변환(생략가능)
  FireEngine f2 = (FireEngine) c; // OK. 자손인 FireEngine타입으로 형변환(생략불가)
  Ambulance a = (Ambulance) f; // 에러. 상속관계가 아닌 클래스 간의 형변환 불가
  ```

```java
class Ex {
    public static void main(String args[] {
        Car car = null;
        FireEngine fe = new FireEngine(); // 실제 인스턴스가 무어싱ㄴ지 중요
        
        // FireEngine fe2 = null;
        // fe.water();
        // car = fe; // 형 변환이 생략됨
        // car.water(); // 컴파일 에러!! Car type의 참조변수로는 water를 호출할 수 없다
        // fe2 = (FireEngine) car; // 자손타입 <= 조상타입. 형변환 생략 불가
        // fe2.water();
        
        FireEngine fe2 = (FireEngine)car; // 조상 -> 자손으로 형변환
        Car car2 = (Car) fe2; // 자손 -> 조상으로 형변환
        // car2.drive(); // NullPointerException발생
    }
}

class Car {
    String color;
    int door;
    
    void drive() {
        System.out.println("drive, Brr~");
    }
    
    void stop() {
        System.out.println("stop!");
    }
}

class FireEngine extends Car {
    void water() {
        System.out.println("water!!")
    }
}
```

```java
class Ex {
    public static void main(String args[] {
        Car c = new Car();
        FireEngine fe = (FireEngine) c; // 형변환 실행 에러 java.lang.ClassCastException
		fe.water(); // 컴파일 오케이
    }
}

class Car {
    String color;
    int door;
    
    void drive() {
        System.out.println("drive, Brr~");
    }
    
    void stop() {
        System.out.println("stop!");
    }
}

class FireEngine extends Car {
    void water() {
        System.out.println("water!!")
    }
}
```



## instanceof 연산자

- 참조변수의 형변환 가능여부 확인에 사용. 가능하면 true 반화

- 형변환 전에 반드시 instanceof로 확인해야 함

  ```java
  void doWork(Car c) {
      if (c instanceof FireEngine) { // 1. 형변환 가능한지 확인
          FireEngine fe = (FireEngine) c; // 2. 형변환
          // 형변환을 하는 이유 : 인스턴스의 원래 기능을 모두 사용하려고
          // Car 타입의 리모콘인 c로는 water()를 호출할 수 없으니까 리모콘을 FireEngine 타입으로 바꿔서 water() 호출
          fe.water();
          ...
      }
  }
  ```

- 참조변수의 형변환은 왜 하나요?

  - 참조변수(리모콘)을 변경함으로써 사용할 수 있는 멤버의 개수를 조절하기 위해서



## 매개변수의 다형성

- 참조형 매개변수는 메서드 호출시, 자신과 같은 타입 또는 자손타입의 인스턴스를 넘겨줄 수 있다
- 장점
  - 다형적 매개변수
  - 하나의 배열로 여러 종류의 객체를 다루기
- 다형성
  - Tv t = new SmartTv();
    - Tv => 조상, SmartTv => 자손
  - 참조변수의 형변환 - 리모콘 바꾸기
    - 사용 가능한 멤버 개수 조절
  - instanceof 연산자
    - 형변환 가능 여부 확인

```java
class Product {
    int price;
    int bonusPoint;
    
    Product (int price) {
    	this.price = price;
    	bonusPoint = (int)(price/10.0);
	}
}

class Tv1 extends Product {
    Tv1() {
        super(100); // tv의 가격
    }
    
    public String toString() { return "Tv";}
}

class Computer extends Product {
    Computer() { super(200); }
    
    public String toString() { return "Computer"; }
}

class Buyer {
    int money = 1000;
    int bonusPoint = 0;
    
    void buy(Product p) {
        if(money < p.price) {
            System.out.println("잔액이 부족하여 물건을 살 수 없습니다.");
           	return;
        }
        
        money -= p.price;
        bonusPoint += p.bonusPoint;
        System.out.println(p + "을/를 구입하셨습니다.");
    }
}

class Ex {
    public static void main(String args[]) {
        Buyber b = new Buyer();
        
        b.buy(new Tv1());
        b.buy(new Computer());
        
        System.out.println("현재 남은 돈은 " + b.money + "만원입니다.");
        System.out.println("현재 보너스점수는 " + b.bonusPoint + "점입니다.");
    }
}
```

Tv을/를 구입하셨습니다.

Computer을/를 구입하셨습니다.

현재 남은 돈은 700만원입니다.

현재 보너스점수는 30점입니다.



## 여러 종류의 객체를 배열로 다루기

- 조상타입의 배열에 자손들의 객체를 담을 수 있다.

  ```java
  class Buyer {
      int money = 1000;
      int bonusPoint = 0;
      
      Product[] cart = new Product[10];
      
      int i = 0;
      
      void buy(Product p) {
          if (money < p.price) {
              System.out.println("잔액부족");
              return;
          }
          
          money -= p.price;
          bonusPoint += p.bonusPoint;
          cart[i++] = p;
      }
  }
  ```

  

## 추상 클래스

- 미완성 메서드를 갖고 있는 클래스

  ```java
  abstract class Player { // 추상클래스(미완성 클래스)
      abstract void play(int pos); // 추상메서드(몸통{}이 없는 미완성 메서드)
      abstract void stop(); // 추상메서드
  }
  ```

- 다른 클래스 작성에 도움을 주기 위한 것. 인스턴스 생성 불가

- 상속을 통해 추상 메서드를 완성해야 인스턴스 생성 가능



#### 추상 메서드

- 미완성 메서드. 구현부(몸통{}이 없는 메서드)

- 꼭 필요하지만 자손마다 다르게 구현될 것으로 예상되는 경우

  ```java
  abstract class Player {
      abstract void play(int pos);
      abstract void stop();
  }
  
  class AudioPlayer extends Player {
      void play(int pos) {}
      void stop)() {}
  }
  
  abstract class AbstractPlayer extends Player {
      void play(int pos) {}
  }
  ```

- 작성

  - 여러 클래스에 공통적으로 사용될 수 있는 추상클래스를 바로 작성하거나 기존클래스의 공통 부분을 뽑아서 추상클래스를 만든다

  ```java
  // 수정 전
  class Marine {
      int x, y;
      void move(int x, int y) {}
      void stop() {}
      void stimPack() {}
  }
  class Tank {
      int x, y;
      void move(int x, int y) {}
      void stop() {}
      void changeModek() {}
  }
  ...
  ```

  ```java
  // 수정 후
  abstract class Unit {
      int x, y;
      abstract void move(int x, int y);
      void stop() {}
  }
  
  class Marine extends Unit {
      void move(int x, int y) {}
      void stimPack() {}
  }
  
  class Tank extends Unit {
      void move(int x, int y) {}
      void changeMode() {}
  }
  ...
  ```

- 추상화된 코드는 구체화된 코드보다 유연하다(변경에 유리)

  - GregorianCalendar cal = new GregorianCalendar();
    - 구체적
  - Calendar cal = Calendar.getInstance();
    - 추상적(애매하게 썼음)



## 인터페이스

- 추상 메서드의 집합

- 구현된 것이 전혀 없는 설계도. 껍데기(모든 멤버가 public)

  ```java
  interface 인터페이스이름 {
      public static final 타입 상수이름 = 값; // public, static, final 생략 가능
      public abstract 메서드이름(메개변수목록); // public, abstract 생략 가능
  }
  ```



#### 인터페이스의 상속

- 인터페이스의 조상은 인터페이스만 가능(Object가 최고 조상 아님)

- 다중 상속이 가능(추상메서드는 충돌해도 문제 없음)

  ```java
  interface Fightable extends Movable, Attackable {}
  
  interface Movable {
      void move(int x, int y);
  }
  
  interface Attackable {
      void attack(Unit u);
  }
  ```



#### 인터페이스의 구현

- 인터페이스에 정의된 추상 메서드를 완성하는 것

- 인터페이스의 추상메서드 몸통{} 만들기(미완성 설계도 완성하기)

- class 클래스이름 implements 인터페이스이름 {}

  ```java
  class Fighter implements Fightable {
      public void move(int x, int y) {}
      public void attack(Unit u) {}
  }
  ```

- 일부만 구현하는 경우, 클래스 앞에 abstract를 붙여야 함

  ```java
  abstract class Fighter implements Fightable {
      public void move(int x, int y)
  }
  ```



#### 인터페이스를 이용한 다형성

- 인터페이스도 구현 클래스의 부모

- 인터페이스 타입 매개변수는 인터페이스 구현한 클래스의 객체만 가능

- 인터페이스 메서드의 리턴타입으로 지정할 수 있다

  ```java
  abstract class Unit {
      int x, y;
      abstract void move(int x, int y);
      void stop() { System.out.println("멈춥니다."); }
  }
  
  interface Fightable {
      void move(int x, int y);
      void attack(Fightable f);
  }
  
  class Fighter extends Unit2 implements Fightable {
      public void move(int x, int y) {
          System.out.println("["+x+","+y+"]로 이동");
      }
      public void attack(Fightable f) {
          System.out.println(f+"를 공격");
      }
  }
  
  public class FighterTest {
      public static void main(String[] args) {
          // Unit2 f = new Fighter(); // Unit2에는 attack()이 없어서 호출 불가
          Fightable f = new Fighter();
          f.move(100, 200);
          f.attack(new Fighter());
          f.move(100, 200);
          Fighter f2 = new Fighter();
          f.attack(f2);
      }
  }
  ```



#### 인터페이스의 장점

- 두 대상(객체) 간의 '연결, 대화, 소통'을 돕는 '중간 역할'을 한다

- 선언(설계)과 구현을 분리시킬 수 있게 한다

- 인터페이스 덕분에 B가 변경되어도 A는 안 바꿀 수 있게 된다(느슨한 결합)

  - A(User)-B(Provider) 관계에서 B를 C로 변경할 때 A도 바꿔야하지만 A(User)-I(B(Provider)) 관계면 B를 C로 바꿔도 A(User)-I(C(Provider)) 관계가 되어 A를 변경할 필요가 없게 된다

  ```java
  class A {
      public void method(B b) {
          b.method();
      }
  }
  
  class B {
      public void method() {
          System.out.println("B클래스의 메서드");
      }
  }
  
  class C {
      public void method() {
          System.out.println("C클래스의 메서드");
      }
  }
  
  public class InterfaceTest {
      public static void main(String[] args) {
          A a = new A();
          a.method(new C()); // A가 B를 사용(의존)
      }
  }
  ```

- 개발 시간을 단축할 수 있다

- 변경에 유리한 유연한 설계가 가능하다

- 표준화가 가능하다

- 서로 관계없는 클래스들을 관계 맺어줄 수 있다



## 디폴트 메서드, static 메서드

- JDK 1.8부터 추가
- 인터페이스에 새로운 메서드를 추가하기 어려움
- 디폴트 메서드는 인스턴스 메서드(인터페이스 원칙 위반)
- 디폴트 메서드가 기존의 메서드와 충돌할 때의 해결책
  - 여러 인터페이스의 디폴트 메서드 간의 충돌	
    - 인터페이스를 구현한 클래스에서 디폴트 메서드를 오버라이딩해야 한다
  - 디폴트 메서드와 조상 클래스의 메서드 간의 충돌
    - 조상 클래스의 메서드가 상속되고, 디폴트 메서드는 무시된다



## 내부 클래스

> 클래스 안의 클래스

- 내부 클래스에서 외부 클래스의 멤버들을 쉽게 접근할 수 있다

- 코드의 복잡성을 줄일 수 있다(캡슐화)

  ```java
  class AAA {
      int i = 100;
      BBB b = new BBB();
      
      class BBB {
          void method() {
              AAA a = new AAA();
              System.out.println(a, i);
          }
      }
  }
  
  class CCC {
      BBB b = new BBB();
  }
  
  public class InnerTest {
      public static void main(String[] args) {
          BBB b = new BBB();
          b.method();
      }
  }
  ```

- 내부 클래스의 종류와 유효범위(scope)는 변수와 동일

  - 인스턴스 클래스
  - 스태틱 클래스
  - 지역 클래스
  - 익명 클래스



#### 내부 클래스의 제어자와 접근성

- 내부 클래스의 제어자는 변수에 사용 가능한 제어자와 동일

  ```java
  class Outer {
      private int iv=0;
      protected static int cv=0;
      
      void myMethod() {
          int lv=0;
      }
  }
  ```

  ```java
  class Outer {
      private class InstanceInner {}
      protected static class StaticInner {}
      
      void myMethod() {
          class LocalInner {}
      }
  }
  ```

```java
class Ex {
    class InstanceInner {
        int iv = 100;
        static int cv = 100;
        final static int CONST = 100;
    }
    
    static class StaticInner {
        int iv = 200;
        static int cv = 200;
    }
    
    void myMethod() {
        class LocalInner {
            int iv = 300;
            static int cv = 300;
            final static int CONST = 300;
        }
        
        int i = LocalInner.CONST;
    }
    
    public static void main(String args[]) {
        System.out.println(InstanceInner.CONST);
        System.out.println(StaticInner.cv);
        System.out.println(LocalInner.CONST);
    }
}
```

```java
class Outer {
    private int outerIv = 0;
    static int outerVb = 0;
    
    class InstanceInner {
        int iiv = outerIv;
        int iiv2 = outerCv;
    }
    
    static class StaticInner {
        static int scv = outerCv;
    }
    
    void myMethod() {
        int lv = 0;
        final int LV = 0;
        
        class LocalInner {
            int liv = outerIv;
            int liv2 = outerCv;
            int liv3 = lv;
            int liv4 = LV;
            
            void method() {
                System.out.println(lv);
            }
        }
    }
}
```



## 익명 클래스

- 이름이 없는 일회용 클래스. 정의와 생성을 동시에

  ```java
  new 조상클래스이름() {
      
  }
  
  new 구현인터페이스이름() {
      
  }
  ```

  ```java
  class Ex {
      Object iv = new Object() { void method(){} };
      static Object cv = new Object() { void method(){} };
      
      void myMethod() {
          Object lv = new Object(){ void method(){} };
      }
  }
  ```

  ```java
  import java.awt.*;
  import java.awt.event.*;
  
  class Ex {
      public static void main(String[] args) {
          Button b = new Button("Start");
          b.addActionListener(new EventHandler());
      }
  }
  
  class EventHandler implements ActionListener {
      public void actionPerformed(ActionEvent e) {
          System.out.println("ActionEvent occurred!!")
      }
  }
  ```
