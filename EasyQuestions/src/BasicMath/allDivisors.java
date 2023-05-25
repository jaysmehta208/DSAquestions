package BasicMath;
// Got
// Given a positive integer N., The task is to find the value of    \sum_{i=1}^{i=n} F(i)  where function F(i) for the
// number i be defined as the sum of all divisors of ‘i‘.
public class allDivisors {
    public static void main(String[] args) {
        System.out.println(sumOfDivisors(5));
    }
    static long sumOfDivisors(int N){
        long sum = 0;
        for (int i = N; i > 0;i--) {
            sum+= (long) (N / i) *i;
        }
        return sum;
    }
}

// Time Complexity: O(N)
// Auxiliary Space: O(1)