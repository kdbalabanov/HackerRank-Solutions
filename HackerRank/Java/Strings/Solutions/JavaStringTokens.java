import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        s = s.trim();
        if(s.length() <= 400000 && s.length() >= 1)
        {
            String[] result = s.split("[\\s!,?._'@]+");
            System.out.println(result.length);
            
            if(result.length > 0)
            {
                for(int i = 0; i < result.length; i++)
                {
                    System.out.println(result[i]);
                }
            }
        }
        else if(s.length() == 0)
        {
            System.out.println(0);
        }
        
        scan.close();
    }
}