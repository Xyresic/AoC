#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>

std::ifstream input("../inputs/input2.txt");
std::string line;
std::vector<std::string> ids;
int double_count = 0, triple_count = 0;

int main(void) {
    while (getline(input, line)) {
        ids.push_back(line);
        if (std::any_of(line.begin(), line.end(), [](char c){return std::count(line.begin(), line.end(), c) == 2;})) double_count++;
        if (std::any_of(line.begin(), line.end(), [](char c){return std::count(line.begin(), line.end(), c) == 3;})) triple_count++;
    }

    //part one
    std::cout << double_count * triple_count << std::endl;

    bool found = false;
    for (int i = 0; i < ids.size() - 1; i++) {
        for (int j = i + 1; j < ids.size(); j++) {
            int count = 0, index;
            for (int k = 0; k < ids[i].size(); k++) {
                if (ids[i][k] != ids[j][k]) {
                    index = k;
                    count++;
                }
                if (k == ids[i].size() - 1 && count == 1) {
                    found = true;
                    std::vector<char> id(ids[i].begin(), ids[i].end());
                    id.erase(id.begin() + index);
                    for (char c : id) std::cout << c;
                    std::cout << std::endl;
                }
            }
            if (found) break;
        }
        if (found) break;
    }
}