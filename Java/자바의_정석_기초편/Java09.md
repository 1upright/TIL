# Java09

> 자바의 정석 ch09



## Object 클래스

- 모든 클래스의 최고 조상, 11개의 메서드만을 가짐
  - 9장
    - protected Object clone()
      - 객체 자신의 복사본 반환
    - public boolean equals(Object obj)
      - 객체 자신과 같은 obj가 같은 객체인지 알려줌. 같으면 true, 다르면 false.
    - protected void finalize()
      - 객체가 소멸될 때 가비지 컬렉터에 의해 자동 호출
    - public Class getClass()
      - 객체 자신의 클래스 정보를 담고 있는 Class인스턴스 반환
    - public int hashCode()
      - 객체 자신의 해시코드 반환
    - public String toString()
      - 객체 자신의 정보를 문자열로 반환
  - 13장
    - public void notify()
      - 객체 자신을 사용하려고 기다리는 쓰레드를 하나만 깨움
    - public void notifyAll()
      - 객체 자신을 사용하려고 기다리는 모든 쓰레드를 깨움
    - public void wait(), public void wait(long timeout), public void wait(long timeout, int nanos)
      - 다른 쓰레드가 notify를 호출할 떄까지 현재 쓰레드를 무한히 또는 지정된 시간(timeout, nanos)동안 기다리게 한다



#### equals()

```java
class Ex {
    public static void main(String[] args) {
        Value v1 = new Value(10);
        Value v2 = new Value(10);
        
        if (v1.equals(v2))
            System.out.println("v1과 v2는 같습니다.");
        else
            System.out.println("v1과 v2는 다릅니다.");
    }
}

class Value {
    int value;
    
    Value(int value) {
        this.value = value;
    }
    
    public boolean equals(Object obj) {
        Value v = (Value)obj;
        
        return this.value==v.value;
    }
}
```

- 오버라이딩

  - 인스턴스 변수(iv)의 값을 비교하도록 equals()를 오버라이딩해야 한다

  ```java
  class Person {
      long id;
      
      public boolean equals(Object obj) {
          if(obj instanceof Person)
              return id == ((Person)obj).id;
          else
              return false;
      }
      
      Person(long id) {
          this.id = id;
      }
  }
  ```



#### hashCode()

- 객체의 해시코드를 반환하는 메서드
- Object클래스의 hashCode()는 객체의 주소를 int로 변환해서 반환
- equals()를 오버라이딩하면, hashCode()도 오버라이딩해야 한다
- equals()의 결과가 true인 두 객체의 해시코드는 같아야 하기 때문
- System.identityHashCode(Object obj)는 Object클래스의 hashCode()와 동일



#### toString()

- 객체를 문자열(String)으로 변환하기 위한 메서드

- 오버라이딩

  ```java
  class Card {
      String kind;
      long number;
      
     	Card() {
          this("SPADE", 1);
      }
      
      Card(String kind, int number) {
          this.kind = kind;
          this.number = number;
      }
      
      // equals 오버라이딩
      public boolean equals(Object obj) {
          if(!(obj instanceof Card))
              return false;
          
          Card c = (Card)obj;
          return this.kind.equals(c.kind) && this.number==c.number;
      }
      
      // Object 클래스의 toString()을 오버라이딩
      public String toString() {
          return "kind:"+kind+", number:"+number;
      }
  }
  
  class Ex {
      public static void main(String[] args) {
          Card c1 = new Card();
          Card c2 = new Card();
          
          System.out.println(c1.toString());
          System.out.println(c2.toString());
      }
  }
  ```



## String 클래스

- String 클래스 = 데이터(char[]) + 메서드(문자열 관련)
- 내용을 변경할 수 없는 불변 클래스
- 덧셈 연산자를 이용한 문자열 결합은 성능이 떨어짐
  - 문자열의 결합이나 변경이 잦다면, 내용 변경이 가능한 StringBuffer를 사용
- 문자열 비교
  - `String str = "abc";` 와 `String str = new String("abc");`
    - 문자열 리터럴 "abc"의 주소를 str에 저장
    - 새로운 String 인스턴스 생성



#### 문자열 리터럴

- 문자열 리터럴은 프로그램 실행시 자동으로 생성된다
- 같은 내용의 문자열 리터럴은 하나만 만들어진다



#### 빈 문자열

- 내용이 없는 문자열. 크리가 0인 char형 배열을 저장하는 문자열
  - String str = "";
- 크기가 0인 배열을 생성하는 것은 어느 타입이나 가능
  - char[] chArr = new char[0];
  - int[] iArr = {};
- 문자(char)와 문자열(String)의 초기화
  - String str = "";



#### 생성자와 메서드

- String(String s)
  - 주어진 문자열을 갖는 String 인스턴스를 생성
  - 잘안씀
- String(char[] value)
  - 주어진 문자열을 갖는 String 인스턴스를 생성
  - 자주 쓰임
- String(StringBuffer buf)
  - StringBuffer 인스턴스가 갖고 있는 문자열과 같은 내용의 String인슽너스 생성
- char charAt(int index)
  - 지정된 위치에 있는 문자를 알려준다(index는 0부터 시작)
- int compareTo(String str)
  - 문자열과 사전순서로 비교한다. 같으면 0을, 사전순으로 이전이면 음수를, 이후면 양수를 반환
- String concat(String str)
  - 문자열을 뒤에 덧붙인다
- boolean contains(CharSequence s)
  - 지정된 문자열이 포함되었는지 검사
- boolean endsWith(String suffix)
  - 지정된 문자열로 끝나는지 검사
- boolean equals(Object obj)
  - 매개변수로 받은 문자열(obj)과 String인스턴스의 문자열을 비교. obj가 String이 아니거나 문자열이 다르면 false 반환
- boolean equalsIgnoreCase(String str)
  - 문자열과 String 인스턴스의 문자열을 대소문자 구분없이 비교한다
- int indexOf(int ch)
  - 주어진 문자가 문자열에 존재하는지 확인하여 위치를 알려준다. 못 찾으면 -1을 반환한다
- int lastIndexOf(int ch)
  - 지정된 문자 또는 문자코드를 문자열의 오른쪽 끝에서부터 찾아서 위치를 알려준다. 못 찾으면 -1을 반환한다
- int lasIndexOf(String str)
  - 지정된 문자열을 인스턴스의 문자열 끝에서부터 찾아서 위치를 알려준다. 못 찾으면 -1을 반환한다
- int length()
  - 문자열의 길이를 알려준다
- String[] split(String regex)
  - 문자열을 지정된 분리자(regex)로 나누어 문자열 배열에 담아 반환한다
- String[] split(String regex, int limit)
  - 문자열을 지정된 분리자(regex)로 나누어 문자열 배열에 담아 반환한다. 단, 문자열 전체를 지정된 수(limit)로 자른다
- boolean startsWith(String prefix)
  - 주어진 문자열(prefix)로 시작하는지 검사한다
- String substring(int begin), String substring(int begin, int end)
  - 주어진 시작위치부터 끝 위치 범위에 포함된 문자열을 얻는다. 이때 시작위치의 문자는 범위에 포함되지만, 끝 위치 문자는 포함되지 않는다
- String toLowerCase()
  - String 인스턴스에 저장되어있는 모든 문자열을 소문자로 변환하여 반환한다
- String toUpperCase()
  - String 인스턴스에 저장되어있는 모든 문자열을 대문자로 변환하여 반환한다
- String trim()
  - 양쪽 끝의 공백 제거 후 반환
- static String valueOf(타입 이름)
  - 지정된 값을 문자열로 변환하여 반환, 참조변수의 경우 toString()을 호출한 결과를 반환



#### join()과 StringJoiner

- join()은 여러 문자열 사이에 구분자를 넣어 결합

  ```java
  String animals = "dog, cat, bear";
  String[] arr = animals.split(", "); // 문자열을 ", " 구분자로 나눠서 배열에 저장
  String str = String.join("-", arr);
  System.out.println(str); // dog-cat-bear
  ```

- 숫자를 문자열로 바꾸기

  ```java
  int i = 100;
  String str1 = i + ""; // 편리
  String str2 = String.valueOf(i); // 빠름
  ```

- 문자열을 숫자로 바꾸기

  ```java
  int i = Integer.parseInt("100");
  int i2 = Integer.valueOf("100");
  Integer i2 = Integer.valueOf("100");
  ```



#### StringBuffer 클래스

- 문자열을 저장&다루기
- String처럼 문자형 배열을 내부적으로 가지고 있음
- 그러나 String과 달리 내용 변경 가능(mutable)
- StringBuffer 생성자
  - 배열은 길이 변경불가. 공간이 부족하면 새로운 배열 생성
  - StringBuffer는 저장할 문자열의 길이를 고려하여 적절한 크기로 생성
- StringBuffer 변경
  - 내용 변경 가능
  - append()는 지정된 내용을 StringBuffer에 추가 후, StringBuffer의 참조를 변환
- StringBuffer 비교
  - StringBuffer는 equals()가 오버라이딩되어있지 않다(주소비교)
  - StringBuffer를 String으로 변환 후에 equals()로 비교해야 한다



#### StringBuffer의 생성자와 메서드

- StringBuffer()

  - 16문자를 담을 수 있는 버퍼를 가진 StringBuffer 인스턴스 생성

- StringBuffer(int length)

  - 지정된 개수의 문자를 담을 수 있는 버퍼를 가진 StringBuffer 인스턴스 생성

- StringBuffer(String str)

  - 지정된 개수의 문자열 값을 갖는 StringBuffer 인스턴스 생성

- StringBuffer append(타입 이름)

- int capacity()

  - StringBuffer인스턴스의 버퍼크기를 알려준다. length()는 버퍼에 담긴 문자열의 길이를 알려준다

- char charAt(int index)

  - 지정된 위치(index)에 있는 문자를 반환한다

- StringBuffer delete(int start, int end)

  - 시작위치부터 끝 위치 사이에 있는 문자를 제거한다. 단, 끝 위치의 문자는 제외

- StringBuffer deleteCharAt(int index)

  - 지정된 위치의 문자를 제거한다

- StringBuffer insert(int pos, 타입 이름)

  - 두 번째 매개변수로 받은 값을 문자열로 변환하여 지정된 위치(pos)에 추가

- int length()

  - 문자열 길이 반환

- StringBuffer replace(int start, int end, String str)

  - 지정된 범위의 문자들을 주어진 문자열로 바꾼다

- StringBuffer reverse()

  - 문자열 순서 뒤집기

- void setCharAt(int index, char ch)

  - 지정된 위치의 문자를 주어진 문자(ch)로 바꾼다

- void setLength(int newLength)

  - 지정된 길이로 문자열의 길이를 변경한다. 길이를 늘리는 경우에 나머지 빈 공간을 널문자로 채운다

- String toString()

  - StringBuffer 인스턴스의 문자열을 String으로 변환

- String substring(int start(, int end))

  - 지정된 범위 내의 문자열을 String으로 뽑아서 반환한다. 시작위치만 지정하면 시작위치부터 문자열 끝까지 뽑아서 반환

  ```java
  class Ex{
      public static void main(String[] args) {
          StringBuffer sb = new StringBuffer("01");
          StringBuffer sb2 = sb.append(23);
          sb.append('4').append(56);
          
          StringBuffer sb3 = sb.append(78);
          sb3.append(9.0);
          
          System.out.println("sb = "+sb);
          System.out.println("sb2 = "+sb2);
          System.out.println("sb3 = "+sb3);
          
          System.out.println("sb = "+sb.deleteCharAt(10));
          System.out.println("sb = "+sb.delete(3, 6));
          System.out.println("sb = "+sb.insert(3, "abc"));
          System.out.println("sb = "+sb.replace(6, sb.length(), "END"));
          
          System.out.println("capacity="+sb.capacity());
          System.out.println("length="+sb.length());
      }
  }
  ```

  sb = 0123456789.0

  sb2 = 0123456789.0

  sb3 = 0123456789.0

  sb = 01234567890

  sb = 01267890

  sb = 012abc67890

  sb = 012abcEND

  capacity=18

  length=9



#### StringBuilder

- StringBuffer는 동기화되어 있다. 멀티쓰레드에 안전(thread-safe)
- 멀티 쓰레드 프로그램이 아닌 경우, 동기화는 불필요한 성능저하, 이럴 땐 StringBuffer 대신 StringBuilder를 사용하면 성능 향상



## Math클래스

- 수학관련 static 메서드의 집합
- round()로 원하는 소수점 아래 세 번째 자리에서 반올림하기
  1. 원래 값에 100 곱하기
  2. 위 결과에 Math.round() 사용
  3. 위 결과를 다시 100.0으로 나누기
- 메서드
  - static double abs(double a), static float abs(float f), static int abs(int i), static long abs(long l)
    - 주어진 값의 절대값 반환
  - static double ceil(double a)
    - 값을 올림하여 반환
  - static double floor(double a)
    - 값을 버림하여 반환
  - static double max(double a, double b)
    - 비교해서 큰 수 반환
    - float, int, long도 가능
  - static double min(double a, double b)
    - 비교해서 작은 수 반환
    - float, int, long도 가능
  - static double random()
    - 0.0~1.0 범위의 랜덤 double 반환
  - static double rint(double a)
    - 주어진 double값과 가장 가까운 정수값을 double형으로 반환
  - static long round(double a), stating long round(float a)
    - 소수점 첫재짜리에서 반올림한 정수값(long) 반환
    - 두 정수의 정가운데에 있는 값은 항상 큰 정수 반환



## 래퍼(wrapper) 클래스

- 8개의 기본형을 객체로 다뤄야할 때 사용하는 클래스

- int => Integer, char => Character 이런식

  ```java
  class Ex {
      public static void main(String[] args) {
          Integer i = new Integer(100);
          Integer i2 = new Integer(100);
          
          System.out.println("i==12 ? "+(i==i2));
          System.out.println("i.equals(12) ? "+i.equals(12));
          System.out.println("i.compareTo(i2)="+i.compareTo(i2));
          System.out.println("i.toString()="+i.toString());
          
          System.out.println("MAX_VALUE="+Integer.MAX_VALUE);
          System.out.println("MIN_VALUE="+Integer.MIN_VALUE);
          System.out.println("SIZE="+Integer.SIZE+" bits");
          System.out.println("BYTES="+Integer.BYTES+" bytes");
          System.out.println("TYPE="+Integer.TYPE);
      }
  }
  ```

  

## Number 클래스

- 모든 숫자 래퍼 클래스의 조상



## 오토박싱 & 언박싱

- JDK1.5 이전에는 기본형과 참조형간의 연산이 불가능

- 기본형의 값을 객체로 자동변환하는 것을 오토박싱, 그 반대는 언박싱

  ```java
  ArrayList<Ingeger> list = new ArrayList<Integer>();
  list.add(10);
  
  int value = list.get(0);
  ```

  ```java
  import java.util.ArrayList; // ctrl+shift+o 자동 import문 추가
  
  public class RoundTest {
      public static void main(String[] args) {
          ArrayList<Integer> list = new ArrayList<Integer>();
          list.add(new Integer(100)); // list에는 객체만 추가가능
          list.add(100); // JDK 1.5이전에는 에러
          
          // Integer i = list.get(0); // list에 저장된 첫번째 객체를 꺼낸다
          // int i = list.get(0).intvalue(); // intValue()로 Integer를 int로 변환
         	int i = list.get(0); // intValue()로 Integer를 int로 변환
      }
  }
  ```

  ```java
  class Ex {
      public static void main(String[] args) {
          int i = 10;
          
          // 기본형을 참조형으로 형변환(형변환 생략가능)
          Integer intg = (Integer)i; // Integer intg = Integer.valueOf(i);
          Object obj = (Object)i; // Object obj = (Object)Integer.valueOf(i);
          
          Long lng = 100L; // Long lng = new Long(100L);
          
          int i2 = intg + 10; // 참조형과 기본형간의 연산 가능
          long l = intg + lng; // 참조형 간의 덧셈도 가능
          
          Integer intg2 = new Integer(20);
          int i3 = (int)intg2; // 참조형을 기본형으로 형변환 가능(형변환 생략 가능)
      }
  }
  ```