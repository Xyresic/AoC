import java.io.*;
import java.util.*;
import java.util.stream.Collectors;

public class Day3 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input3.txt"));
        int count1 = 0;
        int count2 = 0;
        List<Integer> l1 = new ArrayList<>();
        List<Integer> l2 = new ArrayList<>();
        List<Integer> l3 = new ArrayList<>();

        while (s.hasNext()) {
            String[] sides_str = s.nextLine().trim().split("\\s+");
            int[] sides = Arrays.stream(sides_str).mapToInt(Integer::parseInt).toArray();
            l1.add(sides[0]);
            l2.add(sides[1]);
            l3.add(sides[2]);
            if (sides[0] + sides[1] <= sides[2]) continue;
            if (sides[1] + sides[2] <= sides[0]) continue;
            if (sides[0] + sides[2] <= sides[1]) continue;
            count1++;
        }

        for (int i = 0; i < l1.size(); i += 3) {
            int a = l1.get(i);
            int b = l1.get(i+1);
            int c = l1.get(i+2);
            if (a + b > c && b + c > a && a + c > b) count2++;
            a = l2.get(i);
            b = l2.get(i+1);
            c = l2.get(i+2);
            if (a + b > c && b + c > a && a + c > b) count2++;
            a = l3.get(i);
            b = l3.get(i+1);
            c = l3.get(i+2);
            if (a + b > c && b + c > a && a + c > b) count2++;
        }

        //part one
        System.out.println(count1);

        //part two
        System.out.println(count2);
    }
}
