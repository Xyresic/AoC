import java.io.*;
import java.math.*;
import java.security.*;

public class Day5 {
    public static String toHex(byte[] bytes) {
        BigInteger bi = new BigInteger(1, bytes);
        return String.format("%0" + (bytes.length << 1) + "x", bi);
    }

    public static boolean isFull(String[] arr) {
        for (String s : arr) {
            if (s == null) return false;
        }
        return true;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        String input = "uqwqemis";
        MessageDigest md = MessageDigest.getInstance("MD5");
        StringBuilder code = new StringBuilder();
        String[] code2 = new String[8];
        int index = 1;

        while (code.length() < 8) {
            md.update((input + index).getBytes());
            String hashed = toHex(md.digest());
            if (hashed.startsWith("00000")) {
                char pos6 = hashed.charAt(5);
                code.append(pos6);
                if (Character.isDigit(pos6)) {
                    int ind = Character.getNumericValue(pos6);
                    if (ind < 8 && code2[ind] == null) {
                        code2[ind] = "" + hashed.charAt(6);
                    }
                }
            }
            index++;
        }

        while (!isFull(code2)) {
            md.update((input + index).getBytes());
            String hashed = toHex(md.digest());
            if (hashed.startsWith("00000")) {
                char pos6 = hashed.charAt(5);
                if (Character.isDigit(pos6)){
                    int ind = Character.getNumericValue(pos6);
                    if (ind < 8 && code2[ind] == null) {
                        code2[ind] = "" + hashed.charAt(6);
                    }
                }
            }
            index++;
        }

        //part one
        System.out.println(code.toString());

        //part two
        for (String c : code2) {
            System.out.print(c);
        }
    }
}
