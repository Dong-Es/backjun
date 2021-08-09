import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(sc.hasNext()){
            int a = sc.nextInt();
            int b = sc.nextInt();

            System.out.println(a+b);
            }
        }
    }
// 자바의 경우 반복문 안에 hasNext()메서드를 사용한다.
