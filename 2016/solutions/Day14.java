import java.util.*;
import java.math.*;
import java.security.*;
import java.util.regex.*;

public class Day14 {
    public static String input = "zpqevtbw";

    public static String toHex(byte[] bytes) {
        BigInteger bi = new BigInteger(1, bytes);
        return String.format("%0" + (bytes.length << 1) + "x", bi);
    }

    public static String find_create(List<String> hashes, int index, MessageDigest md, boolean part_one) {
        if (index >= hashes.size()) {
            String hash = input + index;
            for (int i = 0; i < (part_one? 1:2017); i++) {
                md.update(hash.getBytes());
                hash = toHex(md.digest());
            }
            hashes.add(hash);
            return hash;
        } else {
            return hashes.get(index);
        }
    }

    public static int search(boolean part_one) throws NoSuchAlgorithmException {
        MessageDigest md = MessageDigest.getInstance("MD5");
        List<String> hashes = new ArrayList<>();
        Pattern triplet = Pattern.compile("(.)\\1{2}");
        int index = -1;
        int count = 0;

        while (count < 64) {
            index++;
            String hash = find_create(hashes, index, md, part_one);
            Matcher m = triplet.matcher(hash);
            if (m.find()) {
                Pattern quintuplet = Pattern.compile(String.format("%s{5}", hash.charAt(m.start())));
                for (int i = 1; i < 1001; i++) {
                    Matcher matcher = quintuplet.matcher(find_create(hashes, index + i, md, part_one));
                    if (matcher.find()) {
                        count++;
                        break;
                    }
                }
            }
        }

        return index;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        //part one
        System.out.println(search(true));

        //part two
        System.out.println(search(false));
    }
}