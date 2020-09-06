import java.io.*;
import java.util.*;

public class Day1 {
    private static boolean intArrEquals(int[] a1, int[] a2) {
        if (a1.length != a2.length) return false;
        else {
            for (int i = 0; i < a1.length; i++) {
                if (a1[i] != a2[i]) {
                    return false;
                }
            }
            return true;
        }
    }

    private static boolean contains(ArrayList<int[]> arr, int[] ele) {
        for (int[] comp : arr) {
            if (intArrEquals(comp, ele)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws FileNotFoundException{
        String[] input = new Scanner(new File("../inputs/input1.txt")).nextLine().split(", ");
        int[][] directions = {{0, 1}, {-1, 0}, {0, -1}, {1, 0}};
        int curDir = 0;
        int[] pos = {0, 0};
        ArrayList<int[]> visited = new ArrayList<int[]>();
        boolean found = false;
        for (String dir : input) {
            if (dir.contains("L")) {
                curDir = (curDir + 1) % 4;
            } else {
                curDir = (curDir + 3) % 4;
            }
            int mult = Integer.parseInt(dir.substring(1));
            int[] dirStep = directions[curDir];
            int[] delta = {dirStep[0] * mult, dirStep[1] * mult};
            if (!found) {
                for (int i = 1; i < (delta[0] != 0? Math.abs(delta[0]):Math.abs(delta[1])) + 1; i++) {
                    int[] step = {pos[0] + dirStep[0] * i, pos[1] + dirStep[1] * i};
                    if (!contains(visited, step)) {
                        visited.add(step);
                    } else {
                        //part two
                        System.out.println(Math.abs(step[0]) + Math.abs(step[1]));
                        found = true;
                    }
                }
            }
            pos[0] += delta[0];
            pos[1] += delta[1];
        };

        //part one
        System.out.println(Math.abs(pos[0]) + Math.abs(pos[1]));
    }
}