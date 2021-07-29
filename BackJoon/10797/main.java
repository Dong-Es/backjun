import java.util.Scanner;

public class back10797 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();

        int car = 0;
        int cnt =0;

        for(int i=0; i<5;i++){
            car = sc.nextInt();
            if(day == car){
                cnt++;
            }
        }
        sc.close();
        System.out.println(cnt);
    }
}
