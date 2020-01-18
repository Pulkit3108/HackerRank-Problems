import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Animal{
	void walk(){
		System.out.println("I am walking");
	}
}
class Sing extends Animal{
    void sing(){
        System.out.println("I am singing");
    }
}

class Bird extends Sing{
	void fly(){
		System.out.println("I am flying");
	}
}


public class Solution{

   public static void main(String args[]){

	  Bird bird = new Bird();
	  bird.walk();
	  bird.fly();
      bird.sing();
	
   }
}
