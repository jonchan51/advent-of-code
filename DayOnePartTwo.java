import java.util.*;

class DayOnePartTwo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        while (sc.hasNext()) {
            int mass = sc.nextInt();
            int fuel = mass / 3 - 2;
            while (fuel > 0) {
                sum += fuel;
                fuel = fuel / 3 - 2;
            }
        }
        System.out.println(sum);
    }

}
