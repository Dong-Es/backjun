
import java.util.Arrays;
import java.util.Scanner;

public class main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int[] intArr = new int[3];

        intArr[0] = sc.nextInt();
        intArr[1] = sc.nextInt();
        intArr[2] = sc.nextInt();

        Arrays.sort(intArr);

        for(int i = 0; i < 3 ; i++) {
            if(i<2)
                System.out.print(intArr[i]+" ");
            else
                System.out.print(intArr[i]);
        }

    }
}
