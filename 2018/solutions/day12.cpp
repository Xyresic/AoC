#include <iostream>
#include <fstream>
#include <unordered_map>
#include <regex>

std::ifstream input("../inputs/input12.txt");
std::string line;
std::regex match("[.#]+");
std::regex period("\\.");

std::string reproduce(std::string pots, std::unordered_map<std::string, char>& rules) {
    std::string next(pots.size(), '.');
    for (auto& pair : rules) {
        std::regex rule(pair.first);
        std::regex_iterator<std::string::iterator> it(pots.begin(), pots.end(), rule), end;
        while (it != end) next.replace((it++)->position() + 2, 1, 1, pair.second);
    }
    return next;
}

int main(void) {
    std::string pots;
    std::unordered_map<std::string, char> rules;
    getline(input, line);
    std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), match);
    //based on rules, it is not possible for there to be a plant at a pot p < -n  or p > n + last plant after generation n
    //thus, a finite buffer is sufficient
    pots = std::string(100, '.') + rit->str() + std::string(100, '.');
    getline(input, line);
    while (getline(input, line)) {
        rit = std::regex_iterator<std::string::iterator>(line.begin(), line.end(), match);
        std::string regex = rit->str();
        regex += ')';
        regex.insert(1, "(?=");
        regex = std::regex_replace(regex, period, "\\.");
        rules.insert({{regex, (++rit)->str()[0]}});
    }

    //part one
    long long sum = 0;
    for (int i = 0; i < 20; i++) pots = reproduce(pots, rules);
    for (int i = 0; i < pots.size(); i++) if (pots[i] == '#') sum += i - 100;
    std::cout << sum << std::endl;

    //part two
    //after the 95th generation, the sum increases linearly by 91 per generation
    sum = 0;
    for (int j = 0; j < 75; j++) pots = reproduce(pots, rules);
    for (int i = 0; i < pots.size(); i++) if (pots[i] == '#') sum += i - 100;
    sum += 91 * (50000000000 - 95);
    std::cout << sum << std::endl;
}