import java.io.*;
import java.util.*;

public class Solution 
{
    public static void main(String[] args) 
	{
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ArrayList[] lists = new ArrayList[n];
        
        for (int i = 0; i < n; i++)
        {
            int d = scan.nextInt();
            lists[i] = new ArrayList();
            
            for (int j = 0; j < d; j++)
            {
                lists[i].add(scan.nextInt());
            }
        }
        
        int q = scan.nextInt();
        
        for (int k = 0; k < q; k++)
        {
            int x = scan.nextInt();
            int y = scan.nextInt();
            
            try
            {
                System.out.println(lists[x - 1].get(y - 1));
            }
            catch (Exception e)
            {
                System.out.println("ERROR!");
            }
        }
    }
}