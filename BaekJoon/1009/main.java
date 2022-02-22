import java.util.*;
public class main {

    static List<Long> list = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for(int i=0;i<T;i++) {
            list.clear();
            int a = sc.nextInt();
            int b = sc.nextInt();

            if(a%10==0) {
                System.out.println(10);
                continue;
            }
            cal(a,b);
        }
    }

    public static void cal(int a, int b) {
        long X = a;
        while(!list.contains(X%10)) {
            list.add(X%10);
            X = X*a;
        }
        System.out.println(list.get((b%(list.size())+list.size()-1)%list.size()));
    }
}
