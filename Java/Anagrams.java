import java.util.Scanner;

public class Solution {

    static boolean isAnagram(String a, String b) {
        boolean flag=true;
        if(a.length()!=b.length()){
            flag=false;
        }
        else{
            a=a.toUpperCase();
            b=b.toUpperCase();
            int i;
            int A[] = new int[26];
            int B[] = new int[26];
            for(i=0;i<a.length();i++){
                A[a.charAt(i)-'A']++;
                B[b.charAt(i)-'A']++;
            }
            for(i=0;i<26;i++){
                if(A[i]!=B[i]){
                    flag=false;
                    break;
                }
            }
        }
        return(flag);
    }

    public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
