Start_out,Start_in=map(int,input().split())
Second_out,Second_in=map(int,input().split())
Third_out,Third_in=map(int,input().split())
Fouth_out,Fouth_in=map(int,input().split())

First_station_out=Start_out
First_station_in=First_station_out+Start_in

Second_station_out=First_station_in-Second_out 
Second_station_in=Second_station_out+Second_in

Thrid_Station_out=Second_station_in-Third_out
Thrid_Station_in=Thrid_Station_out+Third_in

Fouth_Station_out=Thrid_Station_in-Fouth_out
Fouth_Station_in=Fouth_Station_out+Fouth_in

print(max(First_station_out,First_station_in,Second_station_out,Second_station_in,Thrid_Station_out,Thrid_Station_in,Fouth_Station_out,Fouth_Station_in))
