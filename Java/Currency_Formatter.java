import java.io.*;
import java.util.*;
import java.text.NumberFormat;

public class Solution {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        NumberFormat us     = NumberFormat.getCurrencyInstance(Locale.US);
        Locale x = new Locale("en", "IN");
        NumberFormat india  = NumberFormat.getCurrencyInstance(x);
        NumberFormat china  = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        System.out.println("US: "+us.format(payment));
        System.out.println("India: "+ india.format(payment));
        System.out.println("China: "+china.format(payment));
        System.out.println("France: "+france.format(payment));
    }
}
