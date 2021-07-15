import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        sc.close();

        int sum = 0;
        /*1~n까지의 합과 비슷한 문제를 풀때 중요한 명령어*/
        for(int i = 1; i<=n; i++){
            sum += i;
        }
        System.out.println(sum);
    }
}
