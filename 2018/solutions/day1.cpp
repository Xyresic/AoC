#include <iostream>
#include <fstream>
#include <set>

std::ifstream input("../inputs/input1.txt");
std::string line;
int freq = 0, prev_size = 1, dup;
std::set<int> freqs = {0};
bool found = false, first_iter = true;

int main(void) {
    while (!found) {
        while (getline(input, line)) {
            freq += stoi(line);
            freqs.insert(freq);
            if (freqs.size() == prev_size) {
                found = true;
                dup = freq;
                break;
            }
            prev_size = freqs.size();
        }
        input.clear();
        input.seekg(0);

        //part one
        if (first_iter) {
            first_iter = false;
            std::cout << freq << std::endl;
        }
    }

    //part two
    std::cout << dup << std::endl;
}