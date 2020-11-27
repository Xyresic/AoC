import java.io.*;
import java.util.*;

public class Day24 {
    static List<Integer> path_costs = new ArrayList<>();
    static int[][] costs = new int[8][8];

    static class Node implements Comparable<Node>{
        int x, y, f, g;

        public Node(int x, int y, int g, int[] goal) {
            this.x = x;
            this.y = y;
            this.g = g;
            this.f = g + Math.abs(goal[1] - x) + Math.abs(goal[0] - y);
        }

        public boolean equals(Object other) {
            if (other instanceof Node) {
                Node other_n = (Node) other;
                return x == other_n.x && y == other_n.y;
            }
            return false;
        }

        public int compareTo(Node other) {
            return f - other.f;
        }
    }

    static int astar(int[] start, int[] end, boolean[][] maze) {
        PriorityQueue<Node> nodes = new PriorityQueue<>();
        nodes.add(new Node(start[1], start[0], 0, end));
        while (!nodes.isEmpty()) {
            Node current = nodes.poll();
            if (current.x == end[1] && current.y == end[0]) return current.g;
            for (int i = -1; i < 2; i += 2) {
                Node d_x = new Node(current.x + i, current.y, current.g + 1, end);
                Node d_y = new Node(current.x, current.y + i, current.g + 1, end);
                if (maze[d_x.y][d_x.x] && !nodes.contains(d_x)) nodes.add(d_x);
                if (maze[d_y.y][d_y.x] && !nodes.contains(d_y)) nodes.add(d_y);
            }
        }
        return -1;
    }

    static void swap(int i1, int i2, int[] arr) {
        int val = arr[i1];
        arr[i1] = arr[i2];
        arr[i2] = val;
    }

    static void permute(int k, int[] arr) {
        if (k == 1) {
            int cost = costs[0][arr[0]];
            for (int i = 0; i < arr.length - 1; i++) cost += costs[arr[i]][arr[i + 1]];
            path_costs.add(cost);
        } else {
            permute(k - 1, arr);
            for (int i = 0; i < k - 1; i++) {
                if (k % 2 == 0) swap(i, k - 1, arr);
                else swap(0, k - 1, arr);
                permute(k - 1, arr);
            }
        }
    }

    public static void main(String[] args) throws FileNotFoundException {
        boolean[][] maze = new boolean[37][179];
        int[][] pos = new int[8][2];

        Scanner s = new Scanner(new File("../inputs/input24.txt"));

        for (int i = 0; i < 37; i++) {
            String line = s.nextLine();
            for (int j = 0; j < 179; j++) {
                char c = line.charAt(j);
                switch (c) {
                    case '#':
                        maze[i][j] = false;
                        break;
                    case '.':
                        maze[i][j] = true;
                        break;
                    default:
                        maze[i][j] = true;
                        int num = Character.getNumericValue(c);
                        pos[num][0] = i;
                        pos[num][1] = j;
                }
            }
        }

        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                costs[i][j] = j < i? costs[j][i]:astar(pos[i], pos[j], maze);
            }
        }

        permute(7, new int[]{1, 2, 3, 4, 5, 6, 7});
        //part one
        System.out.println(Collections.min(path_costs));
    }
}
