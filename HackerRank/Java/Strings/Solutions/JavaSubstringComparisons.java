import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution 
{
    public static String getSmallestAndLargest(String s, int k) 
	{
        String smallest = "";
        String largest = "";
        
        for(int i = 0; i < s.length() - (k-1); i++)
        {
            String substring= s.substring(i, i + k);
            
            if(i == 0)
            {
                smallest = substring;
            }
            
            if(substring.compareTo(smallest) < 0)
            {
                smallest = substring;
            }
            
            if(substring.compareTo(largest) > 0)
            {
                largest = substring;
            }
        }
        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) 
	{
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();
      
        System.out.println(getSmallestAndLargest(s, k));
    }
}