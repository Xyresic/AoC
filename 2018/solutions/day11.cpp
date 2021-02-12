//possibly the worst solution I've ever written - O(n^5)

#include <iostream>
#include <vector>

int main(void) {

    std::vector<std::vector<int>> cells(300);
    for (int x = 1; x < 301; x++) {
        for (int y = 1; y < 301; y++) {
            if (y - 1 >= cells.size()) cells.emplace_back(std::vector<int>(300));
            cells[y - 1].push_back(((x + 10) * y + 6878) * (x + 10) / 100 % 10 - 5);
        }
    }

    int max = 0, max_x, max_y, max_size, part1_max = 0, part1_x, part1_y;
    for (int size = 1; size < 301; size++) {
        for (int x = 1; x < 302 - size; x++) {
            for (int y = 1; y < 302 - size; y++) {
                int power = 0;
                for (int dx = 0; dx < size; dx++) {
                    for (int dy = 0; dy < size; dy++) {
                        power += cells[y + dy - 1][x + dx - 1];
                    }
                }
                if (size == 3 && power > part1_max) {
                    part1_max = power;
                    part1_x = x;
                    part1_y = y;
                }
                if (power > max) {
                    max = power;
                    max_x = x;
                    max_y = y;
                    max_size = size;
                }
            }
        }
    }


    //part one
    std::cout << part1_x << ',' << part1_y << std::endl;

    //part two
    std::cout << max_x << ',' << max_y << ',' << max_size << std::endl;
}