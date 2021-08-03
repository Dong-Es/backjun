import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int snack_price = sc.nextInt();
        int snack_sum= sc.nextInt();
        int moeny=sc.nextInt();

        int plus_money = snack_price*snack_sum-moeny;

        if(snack_price*snack_sum<moeny){
            System.out.println(0);
        }
        else{
            System.out.println(plus_money);
        }

    }
}
