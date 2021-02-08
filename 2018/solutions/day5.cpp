#include <iostream>
#include <fstream>
#include <algorithm>

std::ifstream input("../inputs/input5.txt");
std::string line;

bool react(std::string& polymer) {
    bool reacted = false;
    std::string product;
    for (int i = 0; i < polymer.size(); i++) {
        if (i < polymer.size() - 1 && abs(polymer[i] - polymer[i + 1]) == 32) {
            reacted = true;
            i++;
        }
        else product += polymer[i];
    }
    polymer = product;
    return reacted;
}

int main(void) {
    getline(input, line);
    std::string copy = line;
    while (react(copy));

    //part one
    std::cout << copy.size() << std::endl;

    int lengths[26];
    for (int i = 0; i < 26; i++) {
        copy = line;
        copy.erase(std::remove(copy.begin(), copy.end(), 'a' + i), copy.end());
        copy.erase(std::remove(copy.begin(), copy.end(), 'A:wq' + i), copy.end());
        while (react(copy));
        lengths[i] = copy.size();
    }

    //part two
    std::cout << *std::min_element(lengths, lengths + 26) << std::endl;
}