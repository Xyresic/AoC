import java.util.*;
import java.util.stream.*;

public class Day19 {
    public static void main(String[] args) {
        int size = 3018458;
        List<Integer> elves = IntStream.range(1, size + 1).boxed().collect(Collectors.toList());
        boolean evens = true;

        while (elves.size() > 1) {
            final boolean final_evens = evens;
            final List<Integer> final_elves = elves;
            evens = evens ^ elves.size() % 2 == 1;
            elves = IntStream.range(0, elves.size())
                             .filter(i -> i % 2 == (final_evens ? 0:1))
                             .mapToObj(i -> final_elves.get(i))
                             .collect(Collectors.toList());
        }

        //part one
        System.out.println(elves.toArray()[0]);

        Deque<Integer> left = IntStream.range(1, size / 2 + 1).boxed().collect(Collectors.toCollection(ArrayDeque::new));
        Queue<Integer> right = IntStream.range(size / 2 + 1, size + 1).boxed().collect(Collectors.toCollection(ArrayDeque::new));

        while (right.size() > 0) {
            if (left.size() > right.size()) left.pollLast();
            else right.poll();
            right.add(left.poll());
            left.add(right.poll());
        }

        //part two
        System.out.println(left.peek());
    }
}
