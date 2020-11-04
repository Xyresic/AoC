import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Day21 {
    static final int[] unscramble_offsets = {1, 1, 6, 2, 7, 3, 0, 4};

    public static void swap(List<String> list, int pos1, int pos2) {
        String at1 = list.get(pos1);
        list.set(pos1, list.get(pos2));
        list.set(pos2, at1);
    }

    public static String scramble(List<String> input, boolean unscramble) throws FileNotFoundException{
        Scanner s = new Scanner(new File("../inputs/input21.txt"));
        List<String> instructions = new ArrayList<>();
        while (s.hasNext()) instructions.add(s.nextLine());
        if (unscramble) Collections.reverse(instructions);

        for (String line : instructions) {
            String[] split = line.split(" ");
            if (line.contains("swap")) {
                int pos1, pos2;
                if (line.contains("letter")) {
                    pos1 = input.indexOf(split[2]);
                    pos2 = input.indexOf(split[5]);
                } else {
                    pos1 = Integer.parseInt(split[2]);
                    pos2 = Integer.parseInt(split[5]);
                }
                swap(input, pos1, pos2);
            } else if (line.contains("rotate")) {
                int offset;
                List<String> scrambled = new ArrayList<>();
                if (line.contains("based")) {
                    int index = input.indexOf(split[6]);
                    if (unscramble) offset = unscramble_offsets[index];
                    else offset = 1 + index + (index > 3 ? 1 : 0);
                } else offset = Integer.parseInt(split[2]);
                for (int j = 0; j < 8; j++) {
                    scrambled.add(input.get(Math.floorMod(j + offset * (unscramble ^ line.contains("left")? 1:-1), 8)));
                }
                input = scrambled;
            } else if (line.contains("reverse")) {
                int start = Integer.parseInt(split[2]);
                int end = Integer.parseInt(split[4]);
                for (int j = 0; j < (end - start + 1) / 2; j++) swap(input, start + j, end - j);
            } else {
                String removed = input.remove(Integer.parseInt(split[unscramble ? 5 : 2]));
                input.add(Integer.parseInt(split[unscramble ? 2 : 5]), removed);
            }
        }

        return String.join("", input);
    }

    public static void main(String[] args) throws FileNotFoundException{
        List<String> map = new ArrayList<>();
        for (int i = 0; i < 8; i++) map.add((char)('a' + i) + "");

        //part one
        System.out.println(scramble(map, false));

        map = Arrays.stream("fbgdceah".split("")).collect(Collectors.toList());
        //part two
        System.out.println(scramble(map, true));
    }
}
