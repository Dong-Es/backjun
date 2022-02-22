import java.util.Scanner;

public class main_long {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int First_out = sc.nextInt();
        int First_in =sc.nextInt();

        int Second_out = sc.nextInt();
        int Second_in =sc.nextInt();

        int Third_out = sc.nextInt();
        int Third_in =sc.nextInt();

        int Fouth_out = sc.nextInt();
        int Fouth_in =sc.nextInt();


        int First_station_out=First_out;
        int First_station_in=First_station_out+First_in;

        int Second_station_out=First_station_in-Second_out;
        int Second_station_in=Second_station_out+Second_in;

        int Third_station_out=Second_station_in-Third_out;
        int Third_station_in=Third_station_out+Third_in;

        int Fouth_station_out=Third_station_in-Fouth_out;
        int Fouth_station_in=Fouth_station_out+Fouth_in;

        int First_station=Math.max(First_station_in,First_station_out);
        int Second_station=Math.max(Second_station_in,Second_station_out);
        int Third_Station=Math.max(Third_station_in,Third_station_out);
        int Fouth_station=Math.max(Fouth_station_in,Fouth_station_out);

        int FS_station=Math.max(First_station,Second_station);
        int TF_station=Math.max(Third_Station,Fouth_station);

        System.out.println(Math.max(FS_station,TF_station));
    }
}
