package Arrays;
// Got
public class patterns {
    public static void main(String[] args) {
        twentytwo();
    }
    public static void one() {
        for (int i =0; i < 5;i++) {
            for (int j=0;j < 5;j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void two() {
        for (int i =0; i < 5;i++) {
            for (int j=0;j <= i;j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void three() {
        for (int i =0; i < 5;i++) {
            for (int j=0;j <=i;j++) {
                System.out.print(j+1);
            }
            System.out.println();
        }
    }
    public static void four() {
        for (int i =0; i < 5;i++) {
            for (int j=0;j <=i;j++) {
                System.out.print(i+1);
            }
            System.out.println();
        }
    }
    public static void five() {
        for (int i =4; i >=0;i--) {
            for (int j=i;j >= 0;j--) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
    public static void six() {
        for (int i =4; i >=0;i--) {
            for (int j=0;j <=i;j++) {
                System.out.print(j+1);
            }
            System.out.println();
        }
    }
    public static void seven() {
        int j = 1;
        String a = " ";
        String b = "*";
        for (int i =4; i >=0;i--) {
            System.out.print(a.repeat(i));
            System.out.print(b.repeat(j));
            j+=2;
            System.out.println();
        }
    }
    public static void eight() {
        int j = 9;
        String a = " ";
        String b = "*";
        for (int i =0; i <5;i++) {
            System.out.print(a.repeat(i));
            System.out.print(b.repeat(j));
            j-=2;
            System.out.println();
        }
    }
    public static void nine() {
        int j = 1;
        String a = " ";
        String b = "*";
        for (int i =0; i <10;i++) {
            if (i < 5) {
                System.out.print(a.repeat(4-i));
                System.out.print(b.repeat(j));
                j+=2;
            } else {
                j-=2;
                System.out.print(a.repeat(i-5));
                System.out.print(b.repeat(j));
            }
            System.out.println();
        }
    }
    // 10 is repetitive
    public static void eleven() {
        int count = 1;
        for (int i =0; i < 5;i++) {
            for (int j=0;j <= i;j++) {
                System.out.print(count%2);
                count++;
            }
            System.out.println();
        }
    }
    public static void twelve() {
        String a = " ";
        for (int i = 0; i <= 3;i++){
            for (int j = 0;j <= i;j++) {
                System.out.print(j+1);
            }
            System.out.print(a.repeat(6 - 2*i));
            for (int j = i;j >= 0;j--) {
                System.out.print(j+1);
            }
            System.out.println();

        }
    }
    public static void thirteen(){
        int count = 1;
        for (int i = 0 ; i < 5;i++) {
            for (int j = 0; j <= i;j++) {
                System.out.print(count+" ");
                count++;
            }
            System.out.println();
        }
    }
    public static void fourteen(){
        for (int i = 0 ; i < 5;i++) {
            for (int j = 0; j <= i;j++) {
                System.out.print((char)(65+j));
            }
            System.out.println();
        }
    }
    // 15 is repetitive
    public static void sixteen(){
        for (int i = 0 ; i < 5;i++) {
            for (int j = 0; j <= i;j++) {
                System.out.print((char)(65+i));
            }
            System.out.println();
        }
    }
    public static void eighteen(){
        for (int i = 0 ; i < 5;i++) {
            for (int j = 0; j <= i;j++) {
                System.out.print((char)(69-i+j));
            }
            System.out.println();
        }
    }
    public static void nineteen() {
        String a = "*";
        String b = " ";
        int count = 5;
        for (int i = 10; i > 0;i--) {
            if (i > 5) {
                System.out.print(a.repeat(count));
                System.out.print(b.repeat(10-(2*count)));
                System.out.print(a.repeat(count));
                count--;
            } else {
                count++;
                System.out.print(a.repeat(count));
                System.out.print(b.repeat(10-(2*count)));
                System.out.print(a.repeat(count));
            }
            System.out.println();

        }
    }
    // 20 is repetitive
    public static void twentyone() {
        for (int i = 0; i < 4;i++) {
            for (int j = 0; j < 4;j++){
                if (i==0 || j == 0 || i == 3 || j == 3) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
    public static void twentytwo() {
        int temp = 0;
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 7; j++) {
                int[] arr = {i,j,6-i,6-j};
                int min = arr[0];
                for (int k = 1; k < 4;k++) {
                    if (arr[k] < min) {
                        min = arr[k];
                    }
                }
                System.out.print(4 - min);
            }
            System.out.println();

        }
    }
}
