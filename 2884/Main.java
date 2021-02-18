import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

      Scanner sc = new Scanner(System.in);
      /*Scanner를 통해 키보드로부터 입력해줄수있는 명령어*/
      int h = sc.nextInt();
      /*h에 값을 입력할때 필요한 명령어*/
      int m = sc.nextInt();
      /*m에 값을 입력할때 필요한 명령어*/
      sc.close();
      /*입출력하는 변수 sc를 닫아주어 안정적으로 종료시키는 명령어*/

      if (m < 45) {
          h--;
          /*m이 45분보다 작으면 1시간을 빼야하기 때문에 시간의 값을 준 h값에 h--;를 써
          * 45분보다 작을시 1감소 시킵니다. */
          m = 60 - (45 - m);
          /*m의 값이 45보다 작을시 분은 0~60으로 이루어져있기 때문에 (45-m)의 값을 60에서 한번더 빼줍니다.*/
          if (h < 0) {
              h = 23;
          /*하루의 시간은 00:00~23:59입니다.
          * 24시간의 표현은 0:0(자정) 이기 때문에 0이상의 값이 들어가면 24가 넘어가바러기 때문에
          * 옳바른 시간이 아니게 되어버렵니다.*/
          }
          System.out.println(h+" "+m);
      }
      else{
          System.out.println(h+" "+(m-45));
      }
    }
}
