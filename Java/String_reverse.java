import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B="";
        boolean flag=true;
        for(int i=0;i<A.length()/2;i++){
            if(A.charAt(i)!=A.charAt(A.length()-i-1)){
                flag=false;
                break;
            }
                 
        }
        if(flag==true){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
            

        /* Enter your code here. Print output to STDOUT. */
        
    }
}



