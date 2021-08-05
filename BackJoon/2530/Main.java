import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int second = sc.nextInt();
        int plus_time = sc.nextInt();

        int sum = second+plus_time;

        int S = sum%60;
        int M = minute+(sum/60);
        int H = ((sum/60)/60);
        if(M>=60){
            M -=60;
        }
        if (H>=24){
            H -= 24;
        }
        System.out.println(H+" "+M+" "+S);
    }
