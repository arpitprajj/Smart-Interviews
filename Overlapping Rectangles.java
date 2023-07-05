import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        while(t-->0)
        {
            long xlb1=sc.nextInt();
            long ylb1=sc.nextInt();
            long xtr1=sc.nextInt();
            long ytr1=sc.nextInt();
            
            long xlb2=sc.nextInt();
            long ylb2=sc.nextInt();
            long xtr2=sc.nextInt();
            long ytr2=sc.nextInt();
            
            long   area1=(Math.abs(xlb1-xtr1)*Math.abs(ylb1-ytr1));
            long  area2=(Math.abs(xlb2-xtr2)*Math.abs(ylb2-ytr2));
            
            long xcom=(Math.min(xtr1,xtr2)-Math.max(xlb1,xlb2));
            long ycom=(Math.min(ytr1,ytr2)-Math.max(ylb1,ylb2));
            
            long   areacom=0;
            if(xcom>0 && ycom>0)
                 areacom=xcom*ycom;
            System.out.println(area1+area2-areacom);
            
            
            
            
        }
    }
}
