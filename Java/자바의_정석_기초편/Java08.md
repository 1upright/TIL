# Java08

> 자바의 정석 ch08

## 프로그램 오류

- 컴파일 에러 : 컴파일할 때 발생하는 에러

- 런타임 에러 : 실행할 때 발생하는 에러

  - 에러(Error) : 프로그램 코드에 의해서 수습될 수 없는 심각한 오류

  - 예외(Exception) : 프로그램 코드에 의해서 수습될 수 있는 간단한 에러

    ```java
    public cass class ExceptionTest {
        public static void main(String[] args) {
            system.out.println(args[0]);
        }
    } // 런타임 에러
    ```

    - Exception 클래스들 : 사용자의 실수와 같은 외적인 요인에 의해 발생하는 예외
    - RuntimeException 클래스들 : 프로그래머의 실수로 발생하는 예외

- 논리적 에러 : 작성 의도와 다르게 동작



#### 예외 처리 : try-catch문

- 예외처리

  - 정의 : 프로그램 실행 시 발생할 수 있는 예외의 발생에 대비한 코드를 작성하는 것
  - 목적 : 프로그램의 비정상 종료를 막고, 정상적인 실행상태를 유지하는 것

- 흐름

  1. try블럭 내에서 예외가 발생한 경우
     1. 발생한 예외와 일치하는 catch블럭이 있는지 확인
     2. 일치하는 catch블럭을 찾게 되면, 그 catch 블럭 내의 문장들을 수행하고 전체 try-catch 문을 빠져나가서 그 다음 문장을 계속해서 수행한다. 만일 일치하는 catch블럭을 찾지 못하면, 예외는 처리되지 않는다
  2. try블럭 내에서 예외가 발생하지 않은 경우
     1. catch블럭을 거치지 않고 전체 try-catch문을 빠져나가서 수행을 계속한다

  ```java
  class Ex {
     public static void main(String args[]) {
         System.out.println(1);
         System.out.println(2);
         try {
             System.out.println(3);
             System.out.println(0/0);
             System.out.println(4);
         } catch (ArithmeticException ae) {
             if (ae instanceof ArithmeticException)
                 System.out.println("true");
             System.out.println("ArithmeticException");
         } catch (Exception e) {
             System.out.println("Exception");
         }
         System.out.println(6);
     }
  }
  ```

  1

  2

  3

  true

  ArithmeticException

  6



#### printStackTrace()와 getMessage()

- printStackTrace()
  - 예외발생 당시의 호출스택(Call Stack)에 있었던 메서드의 정보와 예외 메시지를 화면에 출력한다
- getMessage()
  - 발생한 예외클래스의 인스턴스에 저장된 메시지를 얻을 수 있다



#### 멀티 catch 블럭

- 내용이 같은 catch블럭을 하나로 합친 것



#### 예외 발생시키기

- 연산자 new를 이용해서 발생시키려는 예외 클래스의 객체를 만든 다음

  - Exception e = new Exception("고의로 발생시켰음");

- 키워드 throw를 이용해서 예외를 발생시킨다

  - throw e;

  ```java
  class Ex {
      public static void main(String args[]) {
          try {
              Exception e = new Exception("고의로 발생키셨음");
              throw e;
          } catch (Exception e) {
              System.out.println("에러 메시지 : " + e.getMessage());
              e.printStackTrace();
          }
          System.out.println("프로그램이 정상 종료되었음.");
      }
  }
  ```



#### checked예외, unchecked예외

- checked예외 : 컴파일러가 예외 처리 여부를 체크(예외 처리 필수)

- unchecked예외 : 컴파일러가 예외 처리 여부를 체크 안함(예외 처리 선택)

  ```java
  class Ex {
      public static void main(String[] args) {
          try {
              throw new Exception();
          } catch(Exception e) {}
          
          throw new RuntimeException();
      }
  }
  ```



#### 메서드에 예외 선언하기

- 예외를 처리하는 방법 : try-catch문, 예외 선언하기

- 메서드가 호출시 발생가능한 예외를 호출하는 쪽에 알리는 것

  ```java
  class Ex {
      public static void main(String[] args) throws Exception {
          method1();
      } // main 메서드 끝
      
      static void method1() throws Exception {
          method2();
      } // method1 끝
      
      static void method2() throws Exception {
          throw new Exception();
      } // method2 끝
  }
  ```

  ```java
  import java.io.*;
  
  class Ex {
      public static void main(String[] args) {
          try {
              File f = createFile(args[0]);
              System.out.println( f.getName()+"파일이 성공적으로 생성되었습니다.");
          } catch (Exception e) {
              System.out.println(e.getMessage()+" 다시 입력해 주시기 바랍니다.");
          }
      } // main 메서드 끝
      
      static File createFile(String fileName) throws Exception {
          if (fileName=null || fileName.equals(""))
              throw new Exception("파일 이름이 유효하지 않습니다.");
         	File f = new File(fileName);
          
          f.createNewFile();
          return f;
      } // createFile 메서드 끝
  } // 클래스의 끝
  ```




#### 사용자 정의 예외 만들기

- 직접 예외 클래스를 정의할 수 있다

- 조상은 Exception과 RuntimeException 중에서 선택

  ```java
  class MyException extends Exception {
      
      private final int ERR_CODE;
      
      MyException(String msg, int errCode) {
          super(msg);
          ERR_CODE = errCode;
      }
      
      MyException(String msg) {
          this(msg, 100);
      }
      
      public int getErrCode() {
          return ERR_CODE;
      }
  }
  ```



#### 예외 되던지기

- 예외를 처리한 후에 다시 예외를 발생시키는 것

- 호출한 메서드와 호출된 메서드 양쪽 모두에서 예외처리하는 것

  ```java
  class Ex {
      public static void main(String[] args) {
          try {
              method1();
          } catch (Exception e) {
              System.out.println("main메서드에서 예외가 처리되었습니다.");
          }
      }
      
     	static void method1() throws Exception {
          try {
              throw new Exception();
          } catch (Exception e) {
              System.out.println("method1메서드에서 예외가 처리되었습니다.");
              throw e;
          }
      }
  }
  ```

  method1메서드에서 예외가 처리되었습니다.

  main메서드에서 예외가 처리되었습니다.



#### 연결된 예외(chained exception)

- 한 예외가 다른 예외를 발생시킬 수 있다
- 예외 A가 예외 B를 발생시키면 A는 B의 원인 예외
  - Throwable initCause(Throwable cause)
    -  지정된 예외를 원인 예외로 등록
  - Throwable getCause
    - 원인 예외를 반환
- 사용 이유
  - 여러 예외를 하나로 묶어 다루기 위해
  - checked 예외를 unchecked 예외로 변경하려 할 때
