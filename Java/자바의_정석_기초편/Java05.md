# Java05

> 자바의 정석 ch05



## 배열

> 같은 타입의 여러 변수를 하나의 묶음으로 다루는 것

- int[] score = new int[5];
- 참조 변수에 이름 붙이고 인덱스를 이용해서 다룬다
- "같은 타입", "연속적임"의 특징을 가진다



#### 배열의 선언과 생성

- 타입[] 변수이름;

  ```java
  int[] score; // 참조변수 score 선언
  score = new int[5]; // int타입의 값 5개를 저장할 수 있는 배열 생성
  ```



#### 배열의 인덱스

- 0에서 -1까지



#### 배열의 길이

- 배열이름.length

  ```java
  int[] arr = new int[5];
  int tmp = arr.length; // 5
  ```

- 배열은 한번 생성하면 그 길이를 바꿀 수 없다

  - 늘리려고 하면 그 옆에 공간이 비어있는지 알 수 없기 때문에 바꿀 수 없으며, 공간이 필요하다면 새로운 배열을 만들면 된다



#### 배열의 초기화

- 배열의 각 요소에 처음으로 값을 저장하는 것

  ```java
  int[] score = new int[5];
  score[0] = 50;
  score[1] = 60;
  ...;
  
  int[] score = new int[] { 50, 60, 70, 80, 90} // 잘 안씀
  
  int[] score = { 50, 60, 70, 80, 90 }; // 거의 이렇게 씀, 두 줄로 나눠 쓰면 안됨
  ```



#### 배열의 출력

```java
char[] chArr = {'a', 'b', 'c'};
System.out.println(chArr); // abc가 출력(char인 경우에만 사용 가능)

int iArr = { 100, 95, 80, 70, 60 };
for(int i=0; i<iArr.length; i++) {
    System.out.printlen(iArr[i]);
} // 배열의 요소 차례로 출력

System.out.println(Array.toString(iArr)); // [100, 95, 80, 70, 60]이 출력
```



#### 배열의 활용

```java
class Ex {
    public static void main(String[] args) {
        int sum = 0; // 총합 저장 위한 변수
        float average = 0f; // 평균 저장 위한 변수
        
       	int score[] = {100, 88, 100, 100, 90};
        
        for (int i=0; i<score.length; i++) {
            sum += score[i]
        }
        average = sum/(float)score.length;
        
        System.out.println("총합 : " + sum);
        System.out.println("평균 : " + average);
    }
}
```

- 섞기

  ```java
  import java.util.Arrays;
  
  class Ex {
      public static void main(String[] args) {
          int[] numArr = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
          System.out.println(Arrays.toString(numArr));
          
          for (int i=0; i<100; i++) {
              int n = (int)(Math.random()*10);
              int tmp = numArr[0];
              numArr[0] = numArr[n];
              numArr[n] = tmp;
          }
          System.out.println(Arrays.toString(numArr));
      }
  }
  ```



#### String 배열

- String[] name = new String[3];

  ```java
  import java.util.Arrays;
  
  class Ex {
      public static void main(String[] args) {
          String[] strArr = {"가위", "바위", "보"};
          System.out.println(Arrays.toString(strArr));
          
          for (int i=0; i<10; i++) {
              int tmp = (int)(Math.random()*3);
              System.out.println(strArr[tmp]);
          }
      }
  }
  ```



#### String 클래스

- char[]와 메서드를 결합한 것

- 내용을 변경할 수 없다(read only)

  - 새로 저장하면 새로운 곳에 저장될 뿐..

- 주요 메서드

  - char charAt(int index)

    - 문자열에서 해당 위치에 있는 문자 반환

      ```java
      String str = "ABCDE";
      char ch = str.charAt(3);
      ```

  - int length()

    - 문자열의 길이 반환

      ```java
      int l = str.length()
      ```

  - String substring(int from, int to)

    - 문자열에서 해당 범위(from~to)의 문자열을 반환(to는 포함X)

      ```java
      String str = "012345";
      String tmp = str.substring(1,4); // 123
      ```

  - boolean equals(Object obj)

    - 문자열의 내용이 같은지 확인

  - char[] toCharArray()

    - 문자열을 문자배열(char[])로 변환하여 반환



#### 커맨드 라인을 통해 입력받기

> 입력한 값들이 문자열 배열에 담겨 전달됨

```java
class Ex {
    public static voide main(String[] args) {
        System.out.println("매개변수의 개수:"+args.length);
        for(int i=0; i<args.length; i++) {
            System.out.println("args["+i+"] = \""+ args[i] + "\"");
        }
    }
}
```



#### 2차원 배열

> 테이블 형태의 데이터를 저장하기 위한 배열

- `int[][] score = new int[4][3];`

- `int[][] arr = new int[][]{{1, 2, 3}, {4, 5, 6}};`

  ```java
  int[][] score = {
      {100, 100, 100},
      {20, 20, 20},
      {30, 30, 30},
      {40, 40, 40}
  };
  ```

- 예제

  ```java
  class Ex {
      public static void main (String[] args) {
          int[][] score = {
              {100, 100, 100},
              {20, 20, 20},
              {30, 30, 30},
              {40, 40, 40}
          };
          int sum = 0;
          
          for (int i=0; i<score.length; i++) {
              for (int j=0; j<score[i].length; j++) {
                  System.out.printf("score[%d][%d]=%d%n", i, j, score[i][j]);
                  
                  sum += score[i][j];
              }
          }
          
          System.out.println("sum="+sum);
      }
  }
  ```

  ```java
  class Ex {
      public static void main (String[] args) {
          String[][] words = {
              {"chair", "의자"},
              {"computer", "컴퓨터"},
              {"integer", "정수"}
          };
          
          Scanner scanner = new Scanner(System.in);
          
          for(int i=0; i<words.length; i++) {
              System.out.printf("Q%d. %s의 뜻은?", i+1, words[i][0]);
              
              String tmp = scanner.nextLine();
              
              if(tmp.equals(words[i][1])) {
                  System.out.printf("정답입니다.%n%n");
              } else {
                  System.out.printf("틀렸습니다. 정답은 %s입니다.%n%n", words[i][1]);
              }
          }
      }
  }
  ```

  

#### Arrays로 배열 다루기

- 문자열 비교와 출력 - equals(), toString()

  ```java
  int[] arr = {0, 1, 2, 3, 4};
  int[][] arr2D = {{1, 2}, {3, 4}};
  
  System.out.println(Arrays.toString(arr)); // [0, 1, 2, 3, 4]
  System.out.println(Arrays.deepToString(arr2D)); // [[1, 2], [3, 4]]
  
  String[][] str2D = new String[][]{{"aaa", "bbb"}, {"ccc", "ddd"}};
  String[][] str2D2 = new String[][]{{"aaa", "bbb"}, {"ccc", "ddd"}};
  
  System.out.println(Arrays.equals(str2D, str2D2)); // false
  System.out.println(Arrays.deepEquals(str2D, str2D2)); // true
  ```

- 배열의 복사 - copyOf(), copyOfRange()

  ```java
  int[] arr = {0, 1, 2, 3, 4};
  int[] arr2 = Arrays.copyOf(arr, arr.length); // [0, 1, 2, 3, 4]
  int[] arr3 = Arrays.copyOf(arr, 3); // [0, 1, 2]
  int[] arr2 = Arrays.copyOf(arr, 7); // [0, 1, 2, 3, 4, 0, 0]
  int[] arr2 = Arrays.copyOfRange(arr, 2, 4); // [2, 3]
  int[] arr2 = Arrays.copyOfRange(arr, 0, 7); // [0, 1, 2, 3, 4, 0, 0]
  ```

- 배열의 정렬 - sort()

  ```java
  int[] arr = {3, 2, 0, 1, 4};
  Arrays.sort(arr);
  System.out.println(Arrays.toString(arr)); // [0, 1, 2, 3, 4]
  ```
