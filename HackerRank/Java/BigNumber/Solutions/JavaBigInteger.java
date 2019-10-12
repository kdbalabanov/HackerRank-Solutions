import java.io.*;
import java.util.*;
import java.math.BigInteger;

public class Solution {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        BigInteger a = input.nextBigInteger();
        BigInteger b = input.nextBigInteger();
        BigInteger sum = a.add(b);
        BigInteger mult = a.multiply(b);
        System.out.println(sum);
        System.out.println(mult);
    }
}