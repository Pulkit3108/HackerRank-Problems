import java.util.*;
import java.io.*;
import java.lang.Math; 

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int j;
            int k=a;
            int c=1;
            for(j=0;j<n;j++)
            {
                k = k + (c*b);
                c=c*2;
                System.out.printf("%d ",k);

            }
            System.out.printf("%n");
        }
        in.close();
    }
}

