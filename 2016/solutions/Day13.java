import javax.sound.midi.Soundbank;
import java.util.*;

public class Day13 {
    public static Map<Integer, Map<Integer, Integer>> g_map = new HashMap<>();

    public static class Node implements Comparable<Node> {
        public static final int input = 1352;
        public static final int[] goal = {31, 39};
        public boolean is_open;
        public int x, y, f, h;

        public Node(int x, int y, int g) {
            this.x = x;
            this.y = y;
            is_open = is_open(x, y);
            if (is_open) {
                if (!g_map.containsKey(x)) g_map.put(x, new HashMap<>());
                if (!g_map.get(x).containsKey(y) || g_map.get(x).get(y) > g) g_map.get(x).put(y, g);
                h = (int)(Math.pow(goal[0] - x, 2) + Math.pow(goal[1] - y, 2));
                f = get_g() + h;
            }
        }

        public int get_g() {
            return g_map.get(x).get(y);
        }

        public static boolean is_open(int x, int y) {
            int count = 0;
            int num = x * (x + 2 * y + 3) + y * (y + 1) + input;
            while (num > 0) {
                if (num % 2 == 1) count++;
                num = num >> 1;
            }
            return count % 2 == 0;
        }

        public boolean equals(Object other) {
            if (other instanceof Node) {
                Node other_n = (Node) other;
                return other_n.x == x && other_n.y == y;
            }
            return false;
        }

        public int compareTo(Node other) {
            return f - other.f;
        }
    }

    public static void main(String[] args) {
        Node start = new Node(1, 1, 0);
        PriorityQueue<Node> nodes = new PriorityQueue<>(Collections.singletonList(start));

        while (!nodes.isEmpty()) {
            Node current = nodes.poll();
            if (current.x == Node.goal[0] && current.y == Node.goal[1]) {
                //part one
                System.out.println(current.get_g());
                break;
            }

            for (int delta = -1; delta < 2; delta += 2) {
                Node neighbor_x = new Node(current.x + delta, current.y, current.get_g() + 1);
                Node neighbor_y = new Node(current.x, current.y + delta, current.get_g() + 1);
                if (neighbor_x.is_open) {
                    nodes.remove(neighbor_x);
                    nodes.add(neighbor_x);
                }
                if (neighbor_y.is_open) {
                    nodes.remove(neighbor_y);
                    nodes.add(neighbor_y);
                }
            }

            g_map.get(current.x).put(current.y, Integer.MAX_VALUE);
        }

        List<Node> visited = new ArrayList<>(Collections.singletonList(start));
        List<Node> walking = new ArrayList<>(visited);
        List<Node> to_walk = new ArrayList<>();
        for (int i = 0; i < 50; i++) {
            for (Node node: walking) {
                for (int delta = -1; delta < 2; delta += 2) {
                    if (node.x + delta > -1) {
                        Node neighbor_x = new Node(node.x + delta, node.y, 0);
                        if (neighbor_x.is_open && !visited.contains(neighbor_x)) {
                            visited.add(neighbor_x);
                            to_walk.add(neighbor_x);
                        }
                    }
                    if (node.y + delta > -1) {
                        Node neighbor_y = new Node(node.x, node.y + delta, 0);
                        if (neighbor_y.is_open && !visited.contains(neighbor_y)) {
                            visited.add(neighbor_y);
                            to_walk.add(neighbor_y);
                        }
                    }
                }
            }
            walking = new ArrayList<>(to_walk);
            to_walk.clear();
        }

        //part two
        System.out.println(visited.size());
    }
}