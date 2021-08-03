import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int vacation = sc.nextInt();
        int korean = sc.nextInt();
        int math = sc.nextInt();
        int Sang_korean = sc.nextInt();
        int Sang_math = sc.nextInt();

        int korean_study =  korean/Sang_korean;
        int math_study = math/Sang_math;

        if(korean % Sang_korean!=0){
            korean_study += 1;
        }
        if (math % Sang_math!=0){
            math_study += 1;
        }
    System.out.println(vacation-Math.max(korean_study,math_study));
    }
}
