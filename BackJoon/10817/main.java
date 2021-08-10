import java.util.Scanner;
import java.util.Arrays;
public class main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] alist = new int[3];

        for (int i=0; i<3; i++) {
            alist[i] = sc.nextInt();
        }
        Arrays.sort(alist);
        System.out.println(alist[1]);
    }
}
