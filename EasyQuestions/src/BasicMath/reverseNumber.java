package BasicMath;
// Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
// outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
//
//Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
public class reverseNumber {
    public static void main(String[] args) {
        System.out.println((int) Math.pow(2,31));
        System.out.println((int) (Math.pow(2,31) - 2));

        System.out.println(reverse((int) Math.pow(2,31) ));

    }
    public static int reverse(int x) {
        boolean flag = false;
        if (x < 0) {
            flag = true;
            x = x*-1;
        }
        long z = 0;
        while (x >0) {
            int r = x%10;
            x = x/10;
            z= z*10 + r;
        }
        if (z > Math.pow(2,31)-1 || z < Math.pow(-2,31)) {
            return 0;
        }
        if (flag) {
            return (int)-z;
        }
        return (int)z;
    }
}
