import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int min = 0;
        int man = 0;
        for(int i=0;i<4;i++) {
            int min_point = sc.nextInt();
            min += min_point;
        }
        for(int i=0;i<4;i++) {
            int man_point = sc.nextInt();
            man += man_point;
        }
        if(min>man){
            System.out.println(min);
        }
        else if(min==man){
            System.out.println(min);
        }
        else{
            System.out.println(man);
        }
    }
}
