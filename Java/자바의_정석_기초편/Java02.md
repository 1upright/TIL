# Java02

> 자바의 정석 ch2



- ctrl+space : 자동완성

- alt+shift+a : 멀티 컬럼 모드(토글)

  - shift+방향키로 동시 선택 가능

- print

  - print : 출력 후 줄바꿈 X
  - println : 출력 후 줄바꿈

  ```java
  System.out.println(5+3); // 8
  System.out.println(5-3); // 2
  System.out.println(5*3); // 15
  System.out.println(5/3); // 1
  ```



##  변수

> 하나의 값을 저장할 수 있는 메모리 공간



#### 변수의 선언

- 값을 저장할 공간을 만들기 위해 선언
- 방법
  - `변수타입 변수방법;`
  - int N;



#### 변수에 값 저장하기

```java
int age;
age = 25;
```

- 변수의 초기화
  - 변수에 처음으로 값을 저장하는 것



#### 변수의 타입

- 변수의 타입은 저장할 값의 타입에 의해 결정된다
- 저장할 값의 타입과 일차하는 타입의 변수를 선언
- 값의 타입(기본형) 8개
  - 문자 - char
  - 숫자
    - 정수 - byte, short, int, long
    - 실수 - float, double
  - 논리 - boolean



## 변수, 상수, 리터럴

- 변수 : 하나의 값을 저장하기 위한 공간

- 상수 : 값을 한 번만 저장 가능한 변수

  ```java
  final int MAX = 100 // MAX를 바꾸려고 하면 에러 발생
  ```

- 리터럴 : 그 자체로 값을 의미하는 것



#### 리터럴의 접두사와 접미사

| 종류   | 리터럴                     | 접미사 |
| ------ | -------------------------- | ------ |
| 논리형 | false, true                | 없음   |
| 정수형 | 123, 0b0101, 077, 0xFF     | L      |
| 실수형 | 3.14 3.0e8, 1.4f, 0x1.0p-1 | f, d   |
| 문자형 | 'A', '1', '\n'             | 없음   |
| 문자열 | "ABC", "123", "A", "true"  | 없음   |

```java
boolean power = true;
char ch = 'A';
String str = "ABC";
byte b = 127; // -128~127
int i = 100; // 10진수
int oct = 0100; // 8진수
int hex = 0x100; // 16진수
long l = 10_000_000_000L;
float f = 3.14f;
double d = 3.14d; // d는 생략 가능
```

- `10.` => 10.0
- `.10` => 0.10
- `10f` => 10.0f
- `1e3` => 1000.0(d)



#### 변수와 리터럴 타입 불일치

- 범위가 변수 > 리터럴 인 경우는 OK

  ```java
  int i = 'A'; // int > char
  long l = 123; // long > int
  double d = 3.14f; // double > float
  ```

- 그 반대는 에러

- byte, short 변수에 int리터럴 저장 가능



#### 문자와 문자열

```java
String s1 = new String("AB"); // 원래 이렇게 써야하지만
String s2 = "AB"; // String에 한해서 이렇게 쓰는 것 허용

String s = ""; // 빈 문자열
char ch = ''; // 에러

String s3 = "A" + "B"; // "AB"
```

- 비교
  - ""+7+7 == "77"
  - 7+7+"" == "14"



## 두 변수의 값 교환

```java
int x = 4, y = 2;
int tmp;

tmp = x;
x = y;
y = tmp;
```



## 기본형과 참조형

- 기본형
  - 오직 8개
  - boolean(true/false), char(하나의 문자만), byte(이전 데이터 다루는데 사용), short(C언어와의 호환을 위해 추가, 잘 안쓰임), int, long, float, double
  - 실제 값을 저장
- 참조형
  - 기본형을 제외한 나머지(String, System 등)
  - 메모리 주소를 저장(4byte 또는 8byte)
  - ex) Date = today; today = new Date();



## printf를 이용한 출력

- println()의 단점

  - 실수의 자리수 조절불가
  - 10진수로만 출력됨

  ```java
  System.out.println(10/3); // 3
  System.out.println(10.0/3); // 3.3333333...
  System.out.println(0x1A); // 26
  ```

- printf()로 출력형식 지정가능

  ```java
  System.out.printf("%.2f", 10.0/3); // 3.33
  System.out.printf("%X", 0x1A); // 1A
  ```



#### 지시자

- %b : boolean 형식으로 출력
- %d : 10진 정수 형식으로 출력
- %o : 8진 정수 형식으로 출력
- %x, %X : 16진 정수 형식으로 출력
- %f : 부동 소수점 형식으로 출력
- %e, %E : 지수 표현식 형식으로 출력
- %c : 문자로 출력
- %s : 문자열로 출력

```java
System.out.printf("age:%d year:%d%n", 26, 2022);

System.out.printf("%#o", 15); // 017 (# 붙이면 접두사)
System.out.printf("%#x", 15); // 0xf
System.out.printf("%#X", 15); // 0XF
System.out.printf("%s", Integer.toBinaryString(15)); // 1111

float f = 123.4567890f;
System.out.printf("%f", f); // 123.456789
System.out.printf("%e", f); // 1.234568e+02 (지수형식)
System.out.printf("%g", f); // 123.457 (간단한 형식)
System.out.printf("%g", 0.00000001); // 1.00000e-8 (간단한 형식)

System.out.printf("[%5d]%n", 10); // [   10]
System.out.printf("[%-5d]%n", 10); // [10   ]
System.out.printf("[%05d]%n", 10); // [00010]

double d = 1.23456789;
System.out.printf("[%14.10f]", d); // [  1.2345678900] 
```



## 입력 받기

> Scanner

- Scanner : 화면으로부터 데이터를 입력받는 기능을 제공하는 클래스

- 사용하려면

  - import 문 추가

    - import java.util.*;

  - scanner 객체 생성

    - Scanner scanner = new Scanner System.in;

  - scaner 객체 사용

    ```java
    int num1 = scanner.nextInt(); // 화면에서 입력받은 정수를 num1에 저장
    String input = scanner.nextLine(); // 화면에서 입력받은 내용을 input에 저장
    int num2 = Integer.parseInt(input); // 문자열을 숫자로 변환하여 num2에 저장
    ```



## 정수형의 오버플로우

- 오버플로우 : 표현가능한 범위를 넘는 것
- 부호 없는 정수(4byte)의 경우 표현범위가 0~15이므로 이 값이 계속 반복되고, 부호있는 정수(4bit)의 경우 표현 범위가 -8~7이므로 이 값이 무한히 반복된다



## 타입 간의 변환 방법

#### 문자와 숫자 간의 변환

- 3+'0'='3'
- '3'-'0'=3



#### 문자열로의 변환

- 3+""="3"
- '3'+""="3"



#### 문자열을 숫자로 변환

- Integer.parseInt("3")=3
- Double.parseDouble("3.4")=3.4
- "3".charAt(0)='3'
