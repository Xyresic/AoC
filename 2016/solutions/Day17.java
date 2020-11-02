import java.util.*;
import java.math.*;
import java.security.*;

public class Day17 {
    static boolean found = false;

    static class Node {
        public int x, y;
        public String path;

        public Node(int x, int y, String path) {
            this.x = x;
            this.y = y;
            this.path = path;
        }
    }

    static String toHex(byte[] bytes) {
        BigInteger bi = new BigInteger(1, bytes);
        return String.format("%0" + (bytes.length << 1) + "x", bi);
    }

    static boolean is_open(char c) {
        return c - 97 > 0 && c - 97 < 6;
    }

    static boolean goal_check(Node node) {
        if (node.x == 3 && node.y == 3) {
            if (!found) {
                //part one
                System.out.println(node.path);
                found = true;
            }
            return true;
        }
        return false;
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        Node start = new Node(0, 0, "");
        Node end = new Node(3, 3, "");
        List<Node> level = new ArrayList<>(Collections.singletonList(start));
        List<Node> next_level = new ArrayList<>();
        MessageDigest md = MessageDigest.getInstance("MD5");
        String input = "awrkjxxr";

        while (true) {
            for (Node node : level) {
                md.update((input + node.path).getBytes());
                String directions = toHex(md.digest()).substring(0, 4);
                if (node.y > 0 && is_open(directions.charAt(0))) {
                    Node up = new Node(node.x, node.y - 1, node.path + "U");
                    if (goal_check(up)) {
                        if (up.path.length() > end.path.length()) end = up;
                    } else next_level.add(up);
                }
                if (node.y < 3 && is_open(directions.charAt(1))) {
                    Node down = new Node(node.x, node.y + 1, node.path + "D");
                    if (goal_check(down)) {
                        if (down.path.length() > end.path.length()) end = down;
                    } else next_level.add(down);
                }
                if (node.x > 0 && is_open(directions.charAt(2))) {
                    Node left = new Node(node.x - 1, node.y, node.path + "L");
                    if (goal_check(left)) {
                        if (left.path.length() > end.path.length()) end = left;
                    } else next_level.add(left);
                }
                if (node.x < 3 && is_open(directions.charAt(3))) {
                    Node right = new Node(node.x + 1, node.y, node.path + "R");
                    if (goal_check(right)) {
                        if (right.path.length() > end.path.length()) end = right;
                    } else next_level.add(right);
                }
            }
            if (next_level.isEmpty()) break;
            level = new ArrayList<>(next_level);
            next_level.clear();
        }

        //part two
        System.out.println(end.path.length());
    }
}
