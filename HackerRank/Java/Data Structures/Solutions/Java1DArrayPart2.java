import java.util.*;

public class Solution 
{
    public static boolean canWin(int leap, int[] game, int current) 
	{
        // Return true if you can win the game; otherwise, return false
        if (current < 0 || game[current] == 1)
            return false;
        else if (current + 1 >= game.length || current + leap >= game.length)
            return true;
        
        game[current] = 1;
        
        return canWin(leap, game, current + 1) || canWin(leap, game, current + leap) || canWin(leap, game, current - 1); 
    }
	
    public static void main(String[] args) 
	{
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
		
        while (q-- > 0) 
		{
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game, 0)) ? "YES" : "NO" );
        }
		
        scan.close();
    }
}