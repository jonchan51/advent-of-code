import java.util.*;

class PartTwo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        String[] numStrings = input.split(",");
        int[] inputs = new int[10000];
        for (int i = 0; i < numStrings.length; i++) {
            inputs[i] = Integer.parseInt(numStrings[i]);
        }
        for (int i = 1; i < 100; i++) {
            for (int j = 1; j < 100; j++) {
                if (checkParam(i, j, 19690720, inputs.clone())) {
                    System.out.println(100 * i + j);
                }
            }
        }
    }

    static boolean checkParam(int noun, int verb, int target, int[] inputs) {
        inputs[1] = noun;
        inputs[2] = verb;
        int index = 0;
        boolean notDone = true;
        while (notDone) {
            int op = inputs[index];
            switch (op) {
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
        return target == inputs[0];
    }

}
