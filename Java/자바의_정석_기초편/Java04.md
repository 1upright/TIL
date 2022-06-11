# Java04

> 자바의 정석 ch4



## if문

```java
if (score>60) {
    System.out.println("합격입니다.");
}

if (score>60)
    System.out.println("합격입니다"); // 하나만 나오는 경우는 {} 생략 가능
```



## if-else문

```java
if (input==0) {
    System.out.println("0입니다.");
} else {
    System.out.println("0이 아닙니다.");
}
```



## if-else if문

> 여러 개 중의 하나 - 여러 개의 조건식을 포함한 조건식

``` java
import java.util.scanner;

class Ex {
    public static void main(String[] args) {
        int score = 0; // 점수 저장 위한 변수
        char grade = ''; // 학점 저장 위한 변수. 공백으로 초기화한다

        System.out.print("점수를 입력하세요.");
        Scanner scanner = new Scanner(System.in);
        score = scanner.nextInt();

        if(score >= 90) {
            grade = 'A';
        } else if(score >= 80) {
            grade = 'B';
        } else if(score >= 70) {
            grade = 'C';
        } else {
            grade = 'D';
        }
        System.out.println("당신의 학점은 " + grade + "입니다.");
    }    
}
```



## 중첩 if문

> if문 안의 if문. 1000번도 됨(중첩횟수 제약 X)

```java
if (num >= 0) {
    if (num != 0) {
        sign = '+';
    } else {
        sign = '-';
    }
}
```



## switch문

> 처리해야 하는 경우의 수가 많을 때 유용한 조건문

```java
import java.util.scanner;

class Ex {
    public static void main(String[] args) {
        System.out.print("현재 월을 입력하세요.");
		
        Scanner scanner = new Scanner(System.in);
        int month = scanner.nextInt();
        
        switch(month) {
            case 3:
            case 4:
            case 5:
                System.out.println("현재의 계절은 봄입니다.");
                break;
            case 6: case 7: case 8:
                System.out.println("현재의 계절을 여름입니다.");
                break;
            case 9: case 10: case 11:
                System.out.println("현재의 계절을 가을입니다.");
            	break;
            default:
            // case 12: case 1: case 2:
                System.out.println("현재의 계절을 겨울입니다.");
        }
    }    
}
```

- 제약 조건

  - switch문의 조건식 결과는 정수 또는 문자열이어야 한다

  - case문의 값은 정수 상수(문자 포함), 문자열만 가능하며, 중복되지 않아야 한다.

    ```java
    int num, result;
    final int ONE = 1;
    
    switch (result) {
        case '1': // OK. 문자 리터럴(정수 49와 동일)
        case ONE:  // OK. 정수 상수
        case "YES": // OK. 문자열 리터럴. JDK 1.7부터 사용
        case num: // 에러. 변수는 불가
        case 1.0; // 에러. 실수도 불가
    }
    ```



## 임의의 정수 만들기

> 1~3의 숫자를 임의로 출력하려면?

- Math.random() - 0.0과 1.0 사이의 임의의 double 값을 반환

  - 0.0 <= Math.random() < 1.0

  1. 각 변에 3을 곱한다
     - 0.0 * 3 <= Math.random() * 3 < 1.0 * 3
     - 0.0 <= Math.random() * 3 < 3.0
  2. 각 변을 int형으로 변환한다
     - 0 <= (int)(Math.random() * 3) < 3
  3. 각 변에 1을 더한다
     - 1 <= (int)(Math.random() * 3) + 1 < 4



## for문

> 조건을 만족하는 동안 블럭을 반복

```java
for (int i=1;i<=5;i++) {
    System.out.println("hi");
}

for (int i=10;i>=1;i--) {
    System.out.println(i);
}

for (int i=1,j=10; i<=10; i++,j--) {
    System.out.println("i="+i+",j="+j);
}
```



## 중첩 for문

```java
import java.util.*;

class Ex {
    public static void main(String[] args) {
        for (int i=2;i<=9;i++) {
            for (int j=1,j<=9,j++) {
                System.out.println(i+"*"+j+"*"+(i*j));
            }
            System,out.println();
        }
    }    
}
```



## While문

```java
int i = 5;
while (i-- != 0) {
    System.out.println("hi");
}

int sum = 0;
int i = 0;
while (sum <= 100) {
    System.out.printf("%d" - "%d%n", i, sum);
    sum += ++1;
}
```



## do-while문

> 블럭을 최소한 한 번 이상 반복
>
> 사용자 입력받을 때 유용

```java
import java.util.scanner;

class Ex {
    public static void main(String[] args) {
        int input = 0, answer = 0;
        
        answer = (int)(Math.random()*100)+1; // 1~100 사이의 임의의 수 저장
        Scanner scanner = new Scanner(System.in);
        
        do {
            System.out.print("1과 100 사이의 정수를 입력하세요");
            input = scanner.nextInt();
            
            if (input > answer) {
                System.out.println("더 작은 수로 다시 시도해보세요.");
            } else if (input < answer) {
                System.out.println("더 큰 수로 다시 시도해보세요.");
            }
        } while(input!=answer);
        
        System.out.println("정답입니다.")
        }
    }    
}
```



## break문

> 자신이 포함된 하나의 반복문을 벗어난다

- while(true)로 무한 반복시키고 break
- for(;;)로 무한 반복시키고 break



## continue문

> 자신이 포함된 반복문의 끝으로 이동 - 다음 반복으로 넘어감
>
> 전체 반복 중에서 특정 조건시 반복을 건너뛸 때 사용



## 이름 붙은 반복문

> 원래는 break가 하나의 반복문만 벗어날 수 있지만 그 이상을 벗어나게 하는 break

```java
Loop1 : for (int i=2;i<=9;i++) {
    for (int j=1;j<=9;j++) {
        if (j==5)
            break Loop1;
        System.out.println(i+"*"+j+"="+i*j);
    }
    System.out.println();
}
```