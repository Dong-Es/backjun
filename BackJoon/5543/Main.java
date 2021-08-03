import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int buger = 2001;
        int drink = 2001;

        for(int i =0; i<3; i++) {
            int value = sc.nextInt();
            if (value < buger) {
                buger = value;
            }
        }
        for(int i=0; i<2; i++){
            int value=sc.nextInt();
            if(value<drink){
                drink=value;
            }
        }
        System.out.println(buger+drink-50);
    }
}

