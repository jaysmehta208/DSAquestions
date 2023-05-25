package BasicMath;
// Got
// Given a number N. Count the number of digits in N which evenly divides N.
//
//Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided

public class countDigits {
    static int evenlyDivides(int N){
        String nn = Integer.toString(N);
        int count= 0;
        for (int i = 0; i < nn.length();i++){
            int temp = Integer.parseInt(String.valueOf(nn.charAt(i)));
            if (temp!= 0 && N%temp == 0) {
                count++;
            }
        }
        return count;

    }
}


