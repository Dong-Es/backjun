import java.util.Arrays;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] a = new int[3];
        a[3]= sc.nextInt();
        Arrays.sort(a);

        while (true){
            if (a[2] == (a[0] = a[1] = 0)) {
                break;
            }
            if (a[2]==a[0]+a[1]){
                System.out.println("right");
            }
            else{
                System.out.println("wrong");
            }
        }

    }
}
