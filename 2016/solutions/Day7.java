import java.io.*;
import java.util.*;
import java.util.regex.*;

public class Day7 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input7.txt"));
        int abba_count = 0;
        int aba_count = 0;
        Pattern invalid = Pattern.compile("\\[[^\\]]*(\\w)(?!\\1)(\\w)\\2\\1");
        Pattern valid = Pattern.compile("(\\w)(?!\\1)(\\w)\\2\\1");
        Pattern aba = Pattern.compile("(?=(?:(\\w)(?!\\1)(\\w)\\1(?!\\w*\\])))");

        while (s.hasNext()) {
            String ip = s.nextLine();
            Matcher invalid_matcher = invalid.matcher(ip);
            Matcher valid_matcher = valid.matcher(ip);
            if (!invalid_matcher.find() && valid_matcher.find()) {
                abba_count++;
            }
            Matcher aba_matcher = aba.matcher(ip);
            while (aba_matcher.find()) {
                Pattern bab = Pattern.compile(String.format("\\[[^\\]]*(%s)%s\\1", ip.charAt(aba_matcher.start() + 1), ip.charAt(aba_matcher.start())));
                if (bab.matcher(ip).find()) {
                    aba_count++;
                    break;
                }
            }
        }

        //part one
        System.out.println(abba_count);

        //part two
        System.out.println(aba_count);
    }
}
