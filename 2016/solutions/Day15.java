public class Day15 {
    public static void main(String[] args) {
        int time = 0;
        boolean part_one = false;

        while (true) {
            if ((16 + time) % 17 == 0 &&
                (1 + time) % 3 == 0 &&
                (7 + time) % 19 == 0 &&
                (6 + time) % 13 == 0 &&
                time % 7 == 0 &&
                (1 + time) % 5 == 0) {
                if (!part_one) {
                    //part one
                    System.out.println(time);
                    part_one = true;
                }

                if ((7 + time) % 11 == 0) {
                    //part two
                    System.out.println(time);
                    break;
                }
            }
            time++;
        }
    }
}