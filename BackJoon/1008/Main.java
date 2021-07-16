/*첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.*/
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        double a, b;
        Scanner sc = new Scanner(System.in);
        a = sc.nextDouble();
        b = sc.nextDouble();
        System.out.println(a/b);
    }
}
