import java.io.*;
import java.util.*;

public class Day10 {
    public static void add_val(HashMap<Integer, List<Integer>> map, int key, int val) {
        if (!map.containsKey(key)) map.put(key, new ArrayList<>());
        map.get(key).add(val);
    }

    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input10.txt"));
        int bot = -1;
        HashMap<Integer, List<Integer>> bots = new HashMap<>();
        HashMap<Integer, List<Integer>> outputs = new HashMap<>();
        List<String> instructions = new ArrayList<>();
        while(s.hasNext()) instructions.add(s.nextLine());

        List<String> reference = new ArrayList<>(instructions);
        List<String> instr_copy = new ArrayList<>(instructions);
        while (reference.size() > 0) {
            for (String instr : reference) {
                String[] split = instr.split(" ");
                if (instr.contains("goes")) {
                    int val = Integer.parseInt(split[1]);
                    int bot_num = Integer.parseInt(split[5]);
                    add_val(bots, bot_num, val);
                    instr_copy.remove(instr);
                } else {
                    int bot_num = Integer.parseInt(split[1]);
                    if (bots.containsKey(bot_num) && bots.get(bot_num).size() > 1) {
                        if (bots.get(bot_num).contains(61) && bots.get(bot_num).contains(17)) {
                            bot = bot_num;
                        }
                        int low_num = Integer.parseInt(split[6]);
                        int high_num = Integer.parseInt(split[11]);
                        if (split[5].equals("bot")) {
                            add_val(bots, low_num, Collections.min(bots.get(bot_num)));
                        } else {
                            add_val(outputs, low_num, Collections.min(bots.get(bot_num)));
                        }
                        if (split[10].equals("bot")) {
                            add_val(bots, high_num, Collections.max(bots.get(bot_num)));
                        } else {
                            add_val(outputs, high_num, Collections.max(bots.get(bot_num)));
                        }
                        instr_copy.remove(instr);
                    }
                }
            }
            reference = new ArrayList<>(instr_copy);
        }

        //part one
        System.out.println(bot);

        //part two
        System.out.println(outputs.get(0).get(0) * outputs.get(1).get(0) * outputs.get(2).get(0));
    }
}
