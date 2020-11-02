public class Day16 {
    public static String dragon(String a) {
        StringBuilder b = new StringBuilder();
        for (int i = a.length() - 1; i > -1; i--) b.append(a.charAt(i) == '1'? 0:1);
        return a + "0" + b.toString();
    }

    public static String checksum(String data) {
        StringBuilder checksum = new StringBuilder();
        for (int i = 0; i < data.length(); i += 2) checksum.append(data.charAt(i) == data.charAt(i + 1)? 1:0);
        return checksum.toString();
    }

    public static String odd_checksum(int size, String data) {
        while (data.length() < size) data = dragon(data);
        data = data.substring(0, size);
        String checksum = checksum(data);
        while (checksum.length() % 2 == 0) checksum =  checksum(checksum);
        return checksum;
    }

    public static void main(String[] args) {
        //part one
        System.out.println(odd_checksum(272, "10111100110001111"));

        //part two
        System.out.println(odd_checksum(35651584, "10111100110001111"));
    }
}
