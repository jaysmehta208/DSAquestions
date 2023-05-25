package BasicMath;
// Given an integer x, return true if x is a palindrome, and false otherwise.
public class palindromeNumber {
    public static void main(String[] args) {
        System.out.println(isPalindrome(10));
    }
    public static boolean isPalindrome(int x) {
        int  y = x;
        int z = 0;
        while (x >0) {
            int r = x%10;
            x = x/10;
            z= z*10 + r;
        }
        if (y == z) {
            return true;
        }
        return false;
    }
}
