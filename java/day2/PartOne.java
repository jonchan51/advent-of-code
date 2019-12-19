import java.util.*;

class PartOne {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] numStrings = input.split(",");
        int[] inputs = new int[10000];
        for (int i = 0; i < numStrings.length; i++) {
            inputs[i] = Integer.parseInt(numStrings[i]);
        }
        int index = 0;
        boolean notDone = true;
        while (notDone) {
            switch (inputs[index]) {
            case 1:
                inputs[inputs[index + 3]] = inputs[inputs[index + 1]] + inputs[inputs[index + 2]];
                break;
            case 2:
                inputs[inputs[index + 3]] = inputs[inputs[index + 1]] * inputs[inputs[index + 2]];
                break;
            case 99:
                notDone = false;
                break;
            }
            index += 4;
        }
        System.out.println(inputs[0]);
    }

}
