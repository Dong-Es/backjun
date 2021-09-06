import java.util.Scanner;

public class back2490 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i=0; i<3; i++){
            int count = 0;
            for (int j=0; j<4; j++){
                int playlist= sc.nextInt();
                if (playlist == 0){
                    count++;
                }
            }
            if (count == 0)
                System.out.println("E");
            else if (count ==1)
                System.out.println("A");
            else if (count ==2)
                System.out.println("B");
            else if (count ==3)
                System.out.println("C");
            else
                System.out.println("D");
            }
        }
    }
