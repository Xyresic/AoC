#include <iostream>
#include <fstream>
#include <vector>
#include <regex>

std::ifstream input("../inputs/input3.txt");
std::string line;

struct Patch {
    int id, x, y, x_max, y_max;
};

int main(void) {
    static int fabric[1000][1000];
    int count = 0;
    std::vector<Patch> no_overlaps;
    while (getline(input, line)) {
        std::vector<int> vals;
        std::regex num("\\d+");
        std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), num);
        std::regex_iterator<std::string::iterator> rend;
        while (rit != rend) {
            vals.push_back(stoi(rit->str()));
            rit++;
        }
        Patch patch = {vals[0], vals[1], vals[2], vals[1] + vals[3], vals[2] + vals[4]};
        bool no_overlap = true;
        for (int i = patch.x; i < patch.x_max; i++) {
            for (int j = patch.y; j < patch.y_max; j++) {
                if (fabric[i][j] == 1) count++;
                if (fabric[i][j] > 0) {
                    no_overlap = false;
                    for (int k = 0; k < no_overlaps.size(); k++) {
                        Patch p = no_overlaps[k];
                        if (i >= p.x && i < p.x_max && j >= p.y && j < p.y_max) {
                            no_overlaps.erase(no_overlaps.begin() + k);
                            k--;
                        }
                    }
                }
                fabric[i][j]++;
            }
        }
        if (no_overlap) no_overlaps.push_back(patch);
    }

    //part one
    std::cout << count << std::endl;

    //part two
    std::cout << no_overlaps[0].id << std::endl;
}