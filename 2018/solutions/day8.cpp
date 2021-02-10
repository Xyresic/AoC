#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
#include <numeric>

std::ifstream input("../inputs/input8.txt");
std::string line;
std::regex num("\\d+");

int process(std::vector<int>& nums, std::vector<int>::iterator& start, bool part_two=false) {
    int children = *start, metadata = *++start, sum = 0;
    std::vector<int> vals(children);
    if (children != 0) for (int i = 0; i < children; i++) vals[i] = process(nums, ++start, part_two);
    for (int i = 0; i < metadata; i++) {
        int val = *++start;
        if (part_two && children != 0) {
            if (val > 0 && val <= children) sum += vals[val - 1];
        } else sum += val;
    }
    return sum + (part_two? 0:std::accumulate(vals.begin(), vals.end(), 0));
}

int main(void) {
    getline(input, line);
    std::vector<int> nums;
    std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), num), rend;
    while (rit != rend) nums.push_back(stoi(rit++->str()));
    std::vector<int>::iterator start = nums.begin();

    //part one
    std::cout << process(nums, start) << std::endl;

    //part two
    start = nums.begin();
    std::cout << process(nums, start, true) << std::endl;
}