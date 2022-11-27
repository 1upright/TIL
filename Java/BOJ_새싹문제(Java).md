# BOJ 새싹문제(Java)



## [Hello World](https://www.acmicpc.net/problem/2557) 

```java
class Main{
  public static void main(String[] args) {
      System.out.print("Hello World!");
  }
}
```



## [오늘 날짜](https://www.acmicpc.net/problem/10699) 

```java
import java.time.*;
class Main{
  public static void main(String[] args) {
    System.out.println(LocalDate.now());
  }
}
```



## [고양이](https://www.acmicpc.net/problem/10171)

```java
class Main{
  public static void main(String[] args) {
    System.out.println("\\    /\\");
    System.out.println(" )  ( ')");
    System.out.println("(  /  )");
    System.out.println(" \\(__)|");
  }
}
```



## [개](https://www.acmicpc.net/problem/10172)

```java
class Main{
  public static void main(String[] args) {
    System.out.println("|\\_/|");
    System.out.println("|q p|   /}");
    System.out.println("( 0 )\"\"\"\\");
    System.out.println("|\"^\"`    |");
    System.out.println("||_/=\\\\__|");
  }
}
```



## [새싹](https://www.acmicpc.net/problem/25083)

```java
class Main{
  public static void main(String[] args) {
    System.out.println("         ,r\'\"7");
    System.out.println("r`-_   ,\'  ,/");
    System.out.println(" \\. \". L_r\'");
    System.out.println("   `~\\/");
    System.out.println("      |");
    System.out.println("      |");
  }
}
```



## [A+B](https://www.acmicpc.net/problem/1000) 

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(sc.nextInt() + sc.nextInt());
  }
}
```



## [A-B](https://www.acmicpc.net/problem/1001)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(sc.nextInt() - sc.nextInt());
  }
}
```



## [A×B](https://www.acmicpc.net/problem/10998)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(sc.nextInt() * sc.nextInt());
  }
}
```



## [사칙연산](https://www.acmicpc.net/problem/10869)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    System.out.println(a+b);
    System.out.println(a-b);
    System.out.println(a*b);
    System.out.println(a/b);
    System.out.println(a%b);
  }
}
```



## [A/B](https://www.acmicpc.net/problem/1008)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(sc.nextInt() / sc.nextDouble());
  }
}
```



## [꼬마 정민](https://www.acmicpc.net/problem/11382)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(sc.nextLong() + sc.nextLong() + sc.nextLong());
  }
}
```



## [두 수 비교하기](https://www.acmicpc.net/problem/1330)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    if (a<b) {
      System.out.println("<");
    } else if (a>b) {
      System.out.println(">");
    } else {
      System.out.println("==");
    }
  }
}
```



## [시험 성적](https://www.acmicpc.net/problem/9498)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    if (90<=x) {
      System.out.println('A');
    } else if (80<=x) {
      System.out.println('B');
    } else if (70<=x) {
      System.out.println('C');
    } else if (60<=x) {
      System.out.println('D');
    } else {
      System.out.println('F');
    }
  }
}
```



## [사분면 고르기](https://www.acmicpc.net/problem/14681)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    int y = sc.nextInt();
    if (x>0&&y>0) {
      System.out.println(1);
    } else if (x>0&&y<0) {
      System.out.println(4);
    } else if (x<0&&y>0) {
      System.out.println(2);
    } else {
      System.out.println(3);
    }
  }
}
```



## [윤년](https://www.acmicpc.net/problem/2753)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    if (x%4==0&&(x%100!=0||x%400==0)) {
      System.out.println(1);
    } else {
      System.out.println(0);
    }
  }
}
```



## [사파리월드](https://www.acmicpc.net/problem/2420)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println(Math.abs(sc.nextLong() - sc.nextLong()));
  }
}
```



## [N 찍기](https://www.acmicpc.net/problem/2741)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();

    for (int i=1; i<N+1; i++) {
      System.out.println(i);
    }
  }
}
```



## [팩토리얼](https://www.acmicpc.net/problem/10872)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int x = sc.nextInt();
    System.out.println(factorial(x));
  }

  public static int factorial(int x) {
    if(x <= 1) return 1;
    return x*factorial(x-1);
  }
}
```



## [A+B - 3](https://www.acmicpc.net/problem/10950)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    
    for (int i=0; i<T; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      System.out.println(a+b);
    }
  }
}
```



## [A+B - 5](https://www.acmicpc.net/problem/10952)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    while (true) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      if (a==0 && b==0) {
        break;
      }
      System.out.println(a+b);
    }
  }
}
```



## [구구단](https://www.acmicpc.net/problem/2739)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    for (int i=1; i<10; i++) {
      System.out.println(n+" * "+i+" = "+n*i);
    }
  }
}
```



## [별 찍기 - 1](https://www.acmicpc.net/problem/2438)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    for (int i=1; i<n+1; i++) {
      for (int j=0; j<i; j++) {
        System.out.print('*');
      }
      System.out.println();
    }
  }
}
```



## [A+B - 4](https://www.acmicpc.net/problem/10951)

```java
import java.util.*;

class Main {
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
	    while (sc.hasNextInt()) {
	      int a = sc.nextInt();
	      int b = sc.nextInt();
	      System.out.println(a+b);
	    }
	}
}
```



## [빠른 A+B](https://www.acmicpc.net/problem/15552)

```java
import java.io.*;

class Main{
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    int N = Integer.parseInt(br.readLine());
    for (int i=0; i<N; i++) {
      String s = br.readLine();
      int x = Integer.parseInt(s.split(" ")[0]);
      int y = Integer.parseInt(s.split(" ")[1]);
      
      bw.write(x+y+"\n");
    }
    bw.flush();
  }
}
```



## [X보다 작은 수](https://www.acmicpc.net/problem/10871)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int X = sc.nextInt();

    StringBuilder sb = new StringBuilder();

    for (int i=0; i<N; i++) {
      int Y = sc.nextInt();
      if (X > Y) {
        sb.append(Y+" ");
      }
    }

    System.out.println(sb);
  }
}
```



## [개수 세기](https://www.acmicpc.net/problem/10807)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int N = sc.nextInt();
    int[] nums = new int[N];
    int cnt = 0;

    for (int i=0; i<N; i++) {
      nums[i] = sc.nextInt();
    }
    
    int v = sc.nextInt();

    for(int i=0; i<N; i++) {
      if (nums[i] == v) {
        cnt ++;
      }
    }

    System.out.println(cnt);
  }

}
```



## [과제 안 내신 분..](https://www.acmicpc.net/problem/5597)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int[] stu = new int[31];

    for (int i=0; i<28; i++) {
      int n = sc.nextInt();
      stu[n] = 1;
    }

    for (int i=1; i<31; i++) {
      if (stu[i] != 1) System.out.println(i);
    }
  }
}
```



## [행렬 덧셈](https://www.acmicpc.net/problem/2738)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int m = sc.nextInt();

    int[][] mat1 = new int[n][m];
    int[][] mat2 = new int[n][m];

    for (int i=0; i<n; i++) {
      for (int j=0; j<m; j++) {
        mat1[i][j] = sc.nextInt();
      }
    }

    for (int i=0; i<n; i++) {
      for (int j=0; j<m; j++) {
        mat2[i][j] = sc.nextInt();
      }
    }

    for (int i=0; i<n; i++) {
      for (int j=0; j<m; j++) {
        System.out.print(mat1[i][j] + mat2[i][j] + " ");
      }
      System.out.print("\n");
    }
  }
}
```



## [아스키 코드](https://www.acmicpc.net/problem/11654)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.next().charAt(0);
    System.out.println(n);
  }
}
```



## [단어 길이 재기](https://www.acmicpc.net/problem/2743)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.next().length();
    System.out.println(n);
  }
}
```



## [대소문자 바꾸기](https://www.acmicpc.net/problem/2744)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();
    char [] arr;
    arr = s.toCharArray();

    for (int i=0; i<arr.length; i++) {
      String c = String.valueOf(arr[i]);
      int x = arr[i];
      
      if (65 <= x && x < 91) {
        System.out.print(c.toLowerCase());
      }
      if (97 <= x && x < 123) {
        System.out.print(c.toUpperCase());
      }

    }
  }
}
```



## [학점계산](https://www.acmicpc.net/problem/2754)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.nextLine();

    switch (s) {
      case "A+": System.out.println(4.3); break;
      case "A0": System.out.println(4.0); break;
      case "A-": System.out.println(3.7); break;
      case "B+": System.out.println(3.3); break;
      case "B0": System.out.println(3.0); break;
      case "B-": System.out.println(2.7); break;
      case "C+": System.out.println(2.3); break;
      case "C0": System.out.println(2.0); break;
      case "C-": System.out.println(1.7); break;
      case "D+": System.out.println(1.3); break;
      case "D0": System.out.println(1.0); break;
      case "D-": System.out.println(0.7); break;
      case "F": System.out.println(0.0); break;
    }
  }
}
```



## [알파벳 찾기](https://www.acmicpc.net/problem/10809)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String s = sc.next();

    int[] arr = new int[26];
    for (int i=0; i<26; i++) {
      arr[i] = -1;
    }

    for (int i=0; i<s.length(); i++) {
      char c = s.charAt(i);
      if (arr[c-'a']  == -1) {
        arr[c-'a'] = i;
      }
    }

    for (int i=0; i<26; i++) {
      System.out.print(arr[i]+" ");
    }
  }
}
```



## [그대로 출력하기](https://www.acmicpc.net/problem/11718)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    while (sc.hasNextLine()) {
      String s = sc.nextLine();
      System.out.println(s);
    }
  }
}
```



## [문자열](https://www.acmicpc.net/problem/9086)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    for (int i=0; i<n; i++) {
      String s = sc.next();
      System.out.println(String.valueOf(s.charAt(0))+String.valueOf(s.charAt(s.length()-1)));
    }
  }
}
```



## [5의 수난](https://www.acmicpc.net/problem/23037)

```java
import java.util.*;

class Main {
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		String s = sc.next();
		int [] arr = new int[s.length()];
		
		for (int i=0; i<s.length(); i++) {
			arr[i] = s.charAt(i)-'0';
		}
		
		int res = 0;
		for (int i=0; i<s.length(); i++) {
			res += Math.pow(arr[i], 5);
		}
		
		System.out.println(res);
	}
}
```



## [피보나치 수 5](https://www.acmicpc.net/problem/10870)

```java
import java.util.*;

class Main{
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    System.out.println(fibonacci(n));
    }

  static int fibonacci(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibonacci(n-1) + fibonacci(n-2);
  }
}
```



## [이상한 기호](https://www.acmicpc.net/problem/15964)

```java
import java.util.*;

class Main {
	public static void main(String[] args) {
	    Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(a*a-b*b);
	}
}
```

