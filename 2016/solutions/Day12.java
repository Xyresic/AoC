import java.io.*;
import java.util.*;

public class Day12 {
    public static Integer assembunny(List<String> lines, boolean part_one) {
        int index = 0;
        HashMap<String, Integer> registers = new HashMap<>();
        registers.put("a", 0);
        registers.put("b", 0);
        registers.put("c", part_one? 0:1);
        registers.put("d", 0);

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
                default:
                    if (split[1].equals("1") || registers.get(split[1]) != 0) {
                        index += Integer.parseInt(split[2]) - 1;
                    }
            }
            index++;
        }
        return registers.get("a");
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input12.txt"));
        List<String> lines = new ArrayList<>();
        while (s.hasNext()) lines.add(s.nextLine());

        //part one
        System.out.println(assembunny(lines, true));

        //part two
        System.out.println(assembunny(lines, false));
    }
}
