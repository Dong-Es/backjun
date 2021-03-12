import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T =sc.nextInt();

        for (int t = 0; t <= T; t++)
            /*T만큼 반복을 하겠다는 조건문 입니다.*/
        {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println(a+b);
            /*for문안에 조건문을 쓸수 있다는것을 배웠습니다.*/
        }
        sc.close();
    }
}
