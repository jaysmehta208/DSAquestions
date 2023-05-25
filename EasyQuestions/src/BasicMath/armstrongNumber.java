package BasicMath;
// Got
// For a given 3 digit number, find whether it is armstrong number or not.
// An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the
// number itself. Return "Yes" if it is a armstrong number else return "No".
//NOTE: 371 is an Armstrong number since 33 + 73 + 13 = 371
public class armstrongNumber {
    public static void main(String[] args) {
        System.out.println(armstrongNumber(152));
    }
    static String armstrongNumber(int n) {
        int temp = n;
        long sum = 0;
        while (n > 0) {
            int r = n % 10;
            n = n / 10;
            sum+=r*r*r;
        }
        if (sum==temp) {
            return "Yes";
        }
        return "No";
    }
}

// Time Complexity: O(1)
// Auxiliary Space: O(1)