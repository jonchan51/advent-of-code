import java.util.*;

class P1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        while (sc.hasNext()) {
            int mass = sc.nextInt();
            sum += mass / 3 - 2;
        }
        System.out.println(sum);
    }

}
