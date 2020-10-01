import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Day4 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input4.txt"));
        Pattern p = Pattern.compile("\\d{3}");
        int sum = 0;
        int part2_ans = 0;

        while(s.hasNext()) {
            String encry = s.nextLine();
            Matcher m = p.matcher(encry);
            m.find();
            String name = encry.substring(0, m.start()).replaceAll("-", "");
            String checksum = encry.substring(m.end() + 1, m.end() + 6);
            int id = Integer.parseInt(encry.substring(m.start(), m.end()));
            int shift = id % 26;
            StringBuilder sb = new StringBuilder();
            int[][] counts = new int[26][2];

            for (int i = 97; i < 123; i++) {
                counts[i - 97][1] = i;
            }
            for (int i = 0; i < name.length(); i++) {
                counts[name.charAt(i) - 97][0]++;
                sb.append((char)((name.charAt(i)-97+shift)%26+97));
            }
            if (sb.toString().contains("north")) part2_ans = id;
            Arrays.sort(counts, (int[] a, int[] b) -> b[0] - a[0]);
            sb.setLength(0);
            for (int i = 0; i < 5; i++) {
                sb.append((char)counts[i][1]);
            }
            if (checksum.equals(sb.toString())) sum += id;
        }

        //part one
        System.out.println(sum);

        //part two
        System.out.println(part2_ans);
    }
}
