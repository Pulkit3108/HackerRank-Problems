import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList[] A = new ArrayList[n];
        int i,d,j;
        for(i=0;i<n;i++){
            d = scan.nextInt();
            A[i] = new ArrayList();
            for(j=0;j<d;j++){
                A[i].add(scan.nextInt());
            }
            
        }
        int q = scan.nextInt();
        for(i=0;i<q;i++){
            int x = scan.nextInt();
            int y = scan.nextInt();
            try{
                System.out.println(A[x-1].get(y-1));
            }
            catch(Exception e){
                System.out.println("ERROR!");
            }
        }

    }
}

