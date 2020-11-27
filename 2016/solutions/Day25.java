import java.io.*;
import java.util.*;

public class Day25 {
    public static boolean assembunny(List<String> lines, int start) {
        int index = 0;
        HashMap<String, Integer> registers = new HashMap<>();
        registers.put("a", start);
        registers.put("b", 0);
        registers.put("c", 0);
        registers.put("d", 0);
        List<Integer> stream = new ArrayList<>();

        while(index < lines.size()) {
            String[] split = lines.get(index).split(" ");
            switch (split[0]) {
                case "cpy":
                    try {
                        registers.replace(split[2], Integer.parseInt(split[1]));
                    } catch (NumberFormatException e) {
                        registers.replace(split[2], registers.get(split[1]));
                    }
                    break;
                case "inc":
                    registers.replace(split[1], registers.get(split[1]) + 1);
                    break;
                case "dec":
                    registers.replace(split[1], registers.get(split[1]) - 1);
                    break;
                case "jnz":
                    if (split[1].equals("1") || !split[1].equals("0") && registers.get(split[1]) != 0) {
                        int jump = Integer.parseInt(split[2]);
                        if (split[1].equals("c") && split[2].equals("-5")) {
                            registers.replace("d", registers.get("d") + 231 * registers.get("c"));
                            registers.replace("b", 0);
                            registers.replace("c", 0);
                        } else if (split[1].equals("1") && split[2].equals("-21")) {
                            if (stream.get(0) == 0 && stream.get(stream.size() - 1) == 1) return true;
                        } else index += jump - 1;
                    }
                    break;
                default:
                    int val = registers.get("b");
                    if (!(stream.size() % 2 == 0 && val == 0 || stream.size() % 2 == 1 && val == 1)) return false;
                    stream.add(val);
            }
            index++;
        }
        return false;
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input25.txt"));
        List<String> lines = new ArrayList<>();
        while (s.hasNext()) lines.add(s.nextLine());
        int start = 1;

        while (true) {
            if (assembunny(new ArrayList<>(lines), start)) {
                //part one
                System.out.println(start);
                break;
            }
            start++;
        }
    }
}