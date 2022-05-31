import java.util.*;

class Main{
  static int T;
  static int N;
  static int map[][];
  static int res;
  public static void main(String[] args) throws Exception {
    Scanner scan = new Scanner(System.in);
    Main m = new Main();
    StringBuilder sb = new StringBuilder();
    T = scan.nextInt();

    for (int tc=1; tc<=T; tc++) {
      N = scan.nextInt();
      map = new int[N][N];
      res = 0;
      for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            map[i][j]=scan.nextInt();
        }
      }
      for (int j=0; j<N; j++) {
        m.dfs(0, j, 0, map[0][j], 1);
      }
      sb.append("#"+tc+" "+res+"\n");
    }
    System.out.print(sb);
  }

  public void dfs(int i, int j, int flag, int s, int depth) {
    if (depth == N+2) {
      res = Math.max(res, s);
      return;
    }
    if (i!=0 && flag==0) {
      if (j < N-1) {
        dfs(i-1, j+1, 1, s+map[i-1][j+1], depth+1);
      }
      if (j >= 1) {
        dfs(i-1, j-1, 1, s+map[i-1][j-1], depth+1);
      }
    }
    if (i < N-1) {
      dfs(i+1, j, flag, s+map[i+1][j], depth+1);
    }
  }
}