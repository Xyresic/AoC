public class Day18 {
    public static String next_row(String row) {
        StringBuilder next_row = new StringBuilder();
        row = '.' + row + '.';
        for (int i = 1; i < row.length() - 1; i++) next_row.append(row.charAt(i - 1) == row.charAt(i + 1)? '.':'^');
        return next_row.toString();
    }

    public static int count_safe(String row) {
        return (int)row.chars().filter(c -> c == '.').count();
    }

    public static void main(String[] args) {
        String row = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^";
        int count = count_safe(row);

        for (int i = 0; i < 39; i++) {
            row = next_row(row);
            count += count_safe(row);
        }

        //part one
        System.out.println(count);

        for (int i = 0; i < 399960; i++) {
            row = next_row(row);
            count += count_safe(row);
        }

        //part two
        System.out.println(count);
    }
}
