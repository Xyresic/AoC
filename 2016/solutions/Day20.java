import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Day20 {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner s = new Scanner(new File("../inputs/input20.txt"));
        List<List<Long>> blacklist = new ArrayList<>();
        while (s.hasNext()) {
            String[] line = s.nextLine().split("-");
            blacklist.add(Arrays.stream(line).map(Long::parseLong).collect(Collectors.toList()));
        }
        blacklist = blacklist.stream().sorted(Comparator.comparing(a -> a.get(0))).collect(Collectors.toList());

        long end = 0;
        int count = 0;
        boolean found = false;
        for (int i = 0; i < blacklist.size() - 1; i++) {
            if (blacklist.get(i).get(0) > end + 1) {
                if (!found) {
                    //part one
                    System.out.println(end + 1);
                    found = true;
                }
                count += blacklist.get(i).get(0) - end - 1;
            }
            if (blacklist.get(i).get(1) > end) end = blacklist.get(i).get(1);
        }

        //part two
        System.out.println(count);
    }
}
