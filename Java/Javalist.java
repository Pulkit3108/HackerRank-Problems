import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        List<Integer> a = new ArrayList<>();
        int N = scan.nextInt();
        int i=0;
        for(i=0;i<N;i++){
            int x=scan.nextInt();
            a.add(i,x);
        }
        int Q = scan.nextInt();
        while(Q-->0){
            String input = scan.next();
            if(input.equals("Insert")){
                int x = scan.nextInt();
                int y = scan.nextInt();
                a.add(x,y);
            }
            else{
                int x = scan.nextInt();
                a.remove(x);
            }
        }
        for(Integer ans : a){
            System.out.print(ans + " ");
        }

        
    }
}

