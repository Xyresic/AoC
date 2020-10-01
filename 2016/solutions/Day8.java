import java.io.*;
import java.util.*;

public class Day8 {
    public static void main(String[] args) throws FileNotFoundException{
        Scanner s = new Scanner(new File("../inputs/input8.txt"));
        boolean[][] display = new boolean[6][50];
        int count = 0;

        while (s.hasNext()) {
            String instr = s.nextLine();
            if (instr.contains("rect")) {
                String[] dims = instr.split(" ")[1].split("x");
                for (int i = 0; i < Integer.parseInt(dims[1]); i++) {
                    for (int j = 0; j < Integer.parseInt(dims[0]); j++) {
                        display[i][j] = true;
                    }
                }
            } else {
                String[] split = instr.split(" ");
                int index = Integer.parseInt(split[2].split("=")[1]);
                if (instr.contains("row")) {
                    boolean[] copy = display[index].clone();
                    for (int i = 0; i < 50; i++) {
                        display[index][(i + Integer.parseInt(split[4])) % 50] = copy[i];
                    }
                } else {
                    boolean[] copy = new boolean[6];
                    for (int i = 0; i < 6; i++) {
                        copy[i] = display[i][index];
                    }
                    for (int i = 0; i < 6; i++) {
                        display[(i + Integer.parseInt(split[4])) % 6][index] = copy[i];
                    }
                }
            }
        }

        //part one
        for (boolean[] row : display) {
            for (boolean grid : row) {
                if (grid) count++;
            }
        }
        System.out.println(count);

        //part two
        for (boolean[] row : display) {
            for (boolean grid : row) {
                if (grid) {
                    System.out.print('#');
                } else {
                    System.out.print(' ');
                }
            }
            System.out.println();
        }
    }
}