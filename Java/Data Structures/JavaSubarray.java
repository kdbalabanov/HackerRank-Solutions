import java.io.*;
import java.util.*;

public class Solution 
{
    public static void main(String[] args) 
	{
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        int[] input = new int[n];
        int counter = 0;
        
        for (int i = 0; i < n; i++)
        {
            input[i] = scan.nextInt();
        }
		
        scan.close();
        
        for (int j = 0; j < n; j++)
        {
            int sum = 0;
            for (int k = j; k < n; k++)
            {
                sum += input[k];
                if (sum < 0)
                {
                    counter++;
                }
            }
        }
        
        System.out.println(counter);
    }
}