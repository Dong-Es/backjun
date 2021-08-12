import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        while (sc.hasNextLine()){
            String text = sc.nextLine();
            System.out.println(text);
        }
        sc.close();
    }
}
