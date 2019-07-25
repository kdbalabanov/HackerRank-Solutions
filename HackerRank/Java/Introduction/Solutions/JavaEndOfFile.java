import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int counter = 0;
        while (in.hasNext()) {
            counter++;
            System.out.println(Integer.toString(counter) + " " + in.nextLine());
        }
    }
}