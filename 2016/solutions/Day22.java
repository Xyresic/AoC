import java.io.*;
import java.util.*;

public class Day22 {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner s = new Scanner(new File("../inputs/input22.txt"));
        List<int[]> nodes = new ArrayList<>();
        int count = 0;

        while (s.hasNext()) {
            String line = s.nextLine();
            if (line.contains("node")) {
                String[] split = line.split("\\s+");
                int used = Integer.parseInt(split[2].substring(0, split[2].length() - 1));
                int avail = Integer.parseInt(split[3].substring(0, split[3].length() -1));
                nodes.add(new int[]{used, avail});
            }
        }

        for (int i = 0; i < nodes.size(); i++) {
            for (int j = i == 0? 1:0; j < nodes.size(); j++) {
                if (j != i && nodes.get(i)[0] != 0 && nodes.get(i)[0] <= nodes.get(j)[1]) count++;
            }
        }

        //part one
        System.out.println(count);

        /*
        The open node is at (4,25) and the full nodes range from (1,16) to (29,16).
        The shortest route to (28,0), next to the required data, takes 57 steps: 14 to (0,15) past the wall,
        28 to (28,15), and 15 to (28,0).
        It the takes 1 step to move the data from (29,0) to (28,0) and 5 steps each afterwards to move it one space left.
        This is as the most step efficient procedure, moving the empty node in a u-shape around the data node, takes 5 steps.
        Therefore it takes 57+1+28*5=198 steps in total.
        */
        //part two
        System.out.println(198);
    }
}
