import java.util.*;

public class Day11 {
    public static class Node implements Comparable<Node>{
        public int elevator;
        public List<List<Integer>> floors = new ArrayList<>();
        public int f, g, h;

        public Node(int elevator, List<Integer> f1, List<Integer> f2, List<Integer> f3, List<Integer> f4, int g) {
            this.elevator = elevator;
            floors.add(new ArrayList<>(f1));
            floors.add(new ArrayList<>(f2));
            floors.add(new ArrayList<>(f3));
            floors.add(new ArrayList<>(f4));
            this.g = g;
            h = 2*f3.size() + 4*f2.size() + 6*f1.size();
            f = this.g + h;
        }

        public List<int[]> get_moves() {
            List<int[]> moves = new ArrayList<>();
            int size = floors.get(elevator).size();
            for (int i = 0; i < size - 1; i++) {
                for (int j = i + 1; j < size; j++) {
                    moves.add(new int[]{j, i});
                }
            }
            for (int i = 0; i < size; i++) moves.add(new int[]{i});
            return moves;
        }

        public boolean equals(Object other) {
            if (other instanceof Node) {
                Node other_n = (Node) other;
                if (elevator != other_n.elevator) return false;
                for (int i = 0; i < 4; i++) {
                    if (!(floors.get(i).size() == other_n.floors.get(i).size())) {
                        return false;
                    }
                }
                List<int[]> this_unpaired = get_unpaired(this);
                List<int[]> other_unpaired = get_unpaired(other_n);
                return Arrays.deepEquals(this_unpaired.toArray(), other_unpaired.toArray());
            }
            return false;
        }

        public int compareTo(Node other) {
            return f - other.f;
        }
    }

    public static int find_floor(Node state, int obj) {
        for (int i = 0; i < 4; i++) {
            if (state.floors.get(i).contains(obj)) return i;
        }
        return -1;
    }

    public static List<int[]> get_unpaired(Node state) {
        List<int[]> unpaired = new ArrayList<>();
        for (int i = 0; i < 4; i++) {
            for (int obj : state.floors.get(i)) {
                int pair_floor = find_floor(state, -obj);
                if (pair_floor != i) {
                    unpaired.add(new int[]{i, pair_floor});
                }
            }
        }
        return unpaired;
    }

    public static boolean is_valid(List<Integer> floor) {
        return floor.stream().allMatch(a -> a > 0) || floor.stream().allMatch(a -> a < 0 || floor.contains(-a));
    }

    public static int search(Node start, int goal) {
        PriorityQueue<Node> nodes = new PriorityQueue<>(Collections.singletonList(start));
        while (!nodes.isEmpty()) {
            Node current = nodes.poll();
            List<List<Integer>> floors = current.floors;
            if (floors.get(3).size() == goal) {
                return current.g;
            }
            int elev = current.elevator;
            List<int[]> moves = current.get_moves();
            for (int i = 0; i < moves.size(); i++) {
                if (elev != 3) {
                    List<Integer> cur_floor = new ArrayList<>(floors.get(elev));
                    List<Integer> above = new ArrayList<>(floors.get(elev + 1));
                    for (int j : moves.get(i)) above.add(cur_floor.remove(j));
                    if (is_valid(cur_floor) && is_valid(above)) {
                        Node next;
                        switch (elev) {
                            case 0:
                                next = new Node(1, cur_floor, above, floors.get(2), floors.get(3), current.g + 1);
                                break;
                            case 1:
                                next = new Node(2, floors.get(0), cur_floor, above, floors.get(3), current.g + 1);
                                break;
                            default:
                                next = new Node(3, floors.get(0), floors.get(1), cur_floor, above, current.g + 1);
                        }
                        if (!nodes.contains(next)) {
                            nodes.add(next);
                        }
                    }
                }
                boolean skip = true;
                for (int j = 0; j < elev; j++) {
                    if (floors.get(j).size() != 0) {
                        skip = false;
                        break;
                    }
                }
                if (skip) continue;
                List<Integer> cur_floor = new ArrayList<>(floors.get(elev));
                List<Integer> below = new ArrayList<>(floors.get(elev - 1));
                for (int j : moves.get(moves.size() - 1 - i)) below.add(cur_floor.remove(j));
                if (is_valid(cur_floor) && is_valid(below)) {
                    Node next;
                    switch (elev) {
                        case 1:
                            next = new Node(0, below, cur_floor, floors.get(2), floors.get(3), current.g + 1);
                            break;
                        case 2:
                            next = new Node(1, floors.get(0), below, cur_floor, floors.get(3), current.g + 1);
                            break;
                        default:
                            next = new Node(2, floors.get(0), floors.get(1), below, cur_floor, current.g + 1);
                    }
                    if (!nodes.contains(next)) {
                        nodes.add(next);
                    }
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        List<Integer> f1 = new ArrayList<>(Arrays.asList(1, -1, -2, -3));
        List<Integer> f2 = new ArrayList<>(Arrays.asList(2, 3));
        List<Integer> f3 = new ArrayList<>(Arrays.asList(4, -4, 5, -5));
        List<Integer> f4 = new ArrayList<>();

        //part one
        Node start = new Node(0, f1, f2, f3, f4, 0);
        System.out.println(search(start, 10));

        //part two
        f1.addAll(Arrays.asList(6, -6, 7, -7));
        start = new Node(0, f1, f2, f3, f4, 0);
        System.out.println(search(start, 14));
    }
}
