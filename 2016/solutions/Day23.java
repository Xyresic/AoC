import java.io.*;
import java.util.*;

public class Day23 {
    public static Integer assembunny(List<String> lines, int start) {
        int index = 0;
        HashMap<String, Integer> registers = new HashMap<>();
        registers.put("a", start);
        registers.put("b", 0);
        registers.put("c", 0);
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
                case "jnz":
                    if ((split[1].chars().allMatch(Character::isDigit) && !split[1].equals("0")) || registers.get(split[1]) != 0) {
                        try {
                            int jump = Integer.parseInt(split[2]);
                            if (split[1].equals("d") && split[2].equals("-5")) {
                                registers.replace("a", registers.get("a") + registers.get("b") * registers.get("d"));
                                registers.replace("c", 0);
                                registers.replace("d", 0);
                            } else index += jump - 1;
                        } catch (NumberFormatException e) {
                            index += registers.get(split[2]) - 1;
                        }
                    }
                    break;
                default:
                    try{
                        int ind = index + registers.get("c");
                        String[] instr = lines.get(ind).split(" ");
                        switch (instr[0]) {
                            case "inc":
                                lines.set(ind, "dec " + instr[1]);
                                break;
                            case "dec":
                            case "tgl":
                                lines.set(ind, "inc " + instr[1]);
                                break;
                            case "jnz":
                                lines.set(ind, "cpy " + instr[1] + " " + instr[2]);
                                break;
                            default:
                                lines.set(ind, "jnz " + instr[1] + " " + instr[2]);
                        }
                    } catch (IndexOutOfBoundsException ignored) {}
            }
            index++;
        }
        return registers.get("a");
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input23.txt"));
        List<String> lines = new ArrayList<>();
        while (s.hasNext()) lines.add(s.nextLine());

        //part one
        System.out.println(assembunny(new ArrayList<>(lines), 7));

        //part two
        System.out.println(assembunny(lines, 12));
    }
}
