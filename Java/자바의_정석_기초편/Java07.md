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

