package BasicMath;

import java.util.Arrays;

public class lcmHcf {
    public static void main(String[] args) {
        System.out.println(Arrays.toString(lcmAndGcd((long)14,(long)8)));
    }
    static Long[] lcmAndGcd(Long A , Long B) {
        long num;
        if (A > B) {
            num = B;

        } else {
            num = A;
        }
        boolean flag = true;
        if (A%2 == 1 || B%2 == 1) {
            flag = false;
        }
        while (num > 1) {
            if ((num == B || num == A) && !(B%num == 0 && A%num==0)) {
                if (flag) {
                } else {
                    num = num / 2;

                }
            }
            if (B%num == 0 && A%num==0) {
                return new Long[]{A*B/num,num};
            }

            num--;
        }
        return new Long[]{A*B,(long)1};
    }
}
