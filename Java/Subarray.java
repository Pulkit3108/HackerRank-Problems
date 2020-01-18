import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] A = new int[n];
        int i,c=0,j;
        for(i=0;i<n;i++){
            A[i] = scan.nextInt();
        }
        for(i=0;i<n;i++){
            int s=0;
            for(j=i;j<n;j++){
                s=s+A[j];
                if(s<0){
                    c+=1;
                }

            }
            
        }
        System.out.println(c);
    }
}

