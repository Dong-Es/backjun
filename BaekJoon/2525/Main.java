import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int plus_time = sc.nextInt();

        int sum = minute+plus_time;

        hour += sum/60;
        minute = (minute+plus_time)%60;

        if(hour>=24){
            hour -=24;
        }
        System.out.println(hour+" "+minute);
    }
}
