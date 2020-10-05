import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Day9 {
    public static long decompress(String compressed, boolean recursive) {
        if (compressed.contains("(")) {
            Pattern marker = Pattern.compile("\\([^\\(]*\\)");
            long length = 0;
            Matcher m = marker.matcher(compressed);
            for (int i = 0; i < compressed.length(); i++) {
                if (compressed.charAt(i) == '(') {
                    m.find(i);
                    int[] instr = Arrays.stream(compressed.substring(i+1, m.end()-1).split("x")).mapToInt(Integer::parseInt).toArray();
                    if (recursive) {
                        length += decompress(compressed.substring(m.end(), m.end() + instr[0]).repeat(instr[1]), true);
                    } else {
                        length += instr[0] * instr[1];
                    }
                    i += m.end() + instr[0] - i - 1;
                } else {
                    length++;
                }
            }
            return length;
        } else {
            return compressed.length();
        }
    }

    public static void main(String[] args) throws FileNotFoundException{
        Scanner s = new Scanner(new File("../inputs/input9.txt"));
        String line = s.nextLine().strip();

        //part one
        System.out.println(decompress(line, false));

        //part two
        System.out.println(decompress(line, true));
    }
}
