import java.io.*;
import java.util.*;

public class Solution 
{
    public static void main(String[] args) 
	{       
        Scanner sc=new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        
        System.out.println(A.length() + B.length());
        
        char[] achararr = A.toCharArray();
        char[] bchararr = B.toCharArray();
        achararr[0] = Character.toUpperCase(achararr[0]);
        bchararr[0] = Character.toUpperCase(bchararr[0]);
        A = new String(achararr);
        B = new String(bchararr);
                
        if(A.compareTo(B) <= 0)
        {
            System.out.println("No");
            System.out.println(A + " " + B);
        }
        else
        {
            System.out.println("Yes");
            System.out.println(A + " " + B);
        }
    }
}