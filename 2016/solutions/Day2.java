import java.io.*;
import java.util.*;

public class Day2 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner s = new Scanner(new File("../inputs/input2.txt"));
        String code1 = "";
        String code2 = "";
        int button1 = 5;
        int button2 = 10;
        String[] keypad = {"", "", "1", "", "", "", "2", "3", "4", "", "5", "6", "7", "8", "9", "", "A", "B", "C", "", "", "", "D", "", ""};

        while (s.hasNext()) {
            String instructions = s.nextLine();
            for (int i = 0; i < instructions.length(); i++) {
                switch (instructions.charAt(i)) {
                    case 'U':
                        if (button1 != 1 && button1 != 2 && button1 != 3) {
                            button1 -= 3;
                        }
                        if (button2 - 5 > 1 && !keypad[button2 - 5].isEmpty()) {
                            button2 -= 5;
                        }
                        break;
                    case 'D':
                        if (button1 != 7 && button1 != 8 && button1 != 9) {
                            button1 += 3;
                        }
                        if (button2 + 5 < 23 && !keypad[button2 + 5].isEmpty()) {
                            button2 += 5;
                        }
                        break;
                    case 'L':
                        if (button1 != 1 && button1 != 4 && button1 != 7) {
                            button1 -= 1;
                        }
                        if (button2 - 1 > 1 && !keypad[button2 - 1].isEmpty()) {
                            button2 -= 1;
                        }
                        break;
                    default:
                        if (button1 != 3 && button1 != 6 && button1 != 9) {
                            button1 += 1;
                        }
                        if (button2 + 1 < 23 && !keypad[button2 + 1].isEmpty()) {
                            button2 += 1;
                        }
                }
            }
            code1 += button1;
            code2 += keypad[button2];
        }

        //part one
        System.out.println(code1);

        //part two
        System.out.println(code2);
    }
}
