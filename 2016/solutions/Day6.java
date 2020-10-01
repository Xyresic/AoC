import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Day6 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input6.txt"));
        int[][] counts = new int[8][26];

        while (s.hasNext()) {
            String line = s.nextLine();
            for (int i = 0; i < line.length(); i++) {
                counts[i][line.charAt(i) - 97]++;
            }
        }

        //part one
        for (int[] count : counts) {
            int[] max = new int[2];
            for (int i = 0; i < count.length; i++) {
                if (count[i] > max[0]) {
                    max[0] = count[i];
                    max[1] = i;
                }
            }
            System.out.print((char)(max[1] + 97));
        }

        //part two
        System.out.println();
        for (int[] count : counts) {
            int[] min = {Integer.MAX_VALUE, 0};
            for (int i = 0; i < count.length; i++) {
                if (count[i] < min[0]) {
                    min[0] = count[i];
                    min[1] = i;
                }
            }
            System.out.print((char)(min[1] + 97));
        }
    }
}
