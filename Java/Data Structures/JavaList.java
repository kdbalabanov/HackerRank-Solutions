import java.io.*;
import java.util.*;

public class Solution 
{
    public static void main(String[] args) 
	{
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        ArrayList<Integer> list = new ArrayList<Integer>();
        
        for (int i = 0; i < n; i++)
        {
            list.add(in.nextInt());
        }
        
        int q = in.nextInt();
        
        for (int j = 0; j < q; j++)
        {
            String operation = in.next();
            
            if(operation.equals("Insert"))
            {
                int index = in.nextInt();
                int x = in.nextInt();
                
                list.add(index, x);
            }
            else if (operation.equals("Delete"))
            {
                int index = in.nextInt();
                
                list.remove(index);
            }
        }
        
        for (int k = 0; k < list.size(); k++)
            System.out.print(list.get(k) + " ");
    }
}