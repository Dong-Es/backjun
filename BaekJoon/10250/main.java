import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int repeat = sc.nextInt();

        for (int i=0; i<repeat; i++){
            int floor = sc.nextInt();
            int room =sc.nextInt();
            int customer = sc.nextInt();

            if (floor%customer==0){
                System.out.println((floor * 100) + (customer / floor));
            }
            else{
                System.out.println(((customer%floor)*100)+((customer / floor)+1));
            }
        }
    }
}
