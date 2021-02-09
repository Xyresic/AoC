#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
#include <algorithm>

std::ifstream input("../inputs/input7.txt");
std::string line;
std::regex alph("[A-Z](?= )");

struct Step {
    char name;
    bool processed;
    std::vector<char> prereqs;

    Step(char name) {
        this->name = name;
    }
};

struct Worker {
    int timer = 0;
    Step step = Step(' ');
};

int main(void) {
    std::vector<Step> steps, steps_copy;
    std::string order;
    int seconds = -1;
    for (int i = 0; i < 26; i++) {
        steps.emplace_back('A' + i);
        steps_copy.emplace_back('A' + i);
    }
    while (getline(input, line)) {
        std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), alph);
        char prereq = rit->str()[0];
        steps[(++rit)->str()[0] - 'A'].prereqs.push_back(prereq);
        steps_copy[rit->str()[0] - 'A'].prereqs.push_back(prereq);
    }

    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            if (!steps[j].processed && steps[j].prereqs.size() == 0) {
                steps[j].processed = true;
                order += steps[j].name;
                for (Step& step : steps) {
                    auto ind = std::find(step.prereqs.begin(), step.prereqs.end(), steps[j].name);
                    if (ind != step.prereqs.end()) step.prereqs.erase(ind);
                }
                break;
            }
        }
    }

    //part one
    std::cout << order << std::endl;

    order = "";
    std::vector<Worker> workers(5);
    while (order.size() < 26) {
        for (Worker& worker: workers) {
            if (worker.timer == 0) {
                if (worker.step.name != ' ') {
                    order += worker.step.name;
                    for (Step& step : steps_copy) {
                        auto ind = std::find(step.prereqs.begin(), step.prereqs.end(), worker.step.name);
                        if (ind != step.prereqs.end()) step.prereqs.erase(ind);
                    }
                }
                worker.step = Step(' ');
                for (Step& step : steps_copy) {
                    if (!step.processed && step.prereqs.size() == 0) {
                        step.processed = true;
                        worker.timer = 60 + step.name + 1 - 'A';
                        worker.step = step;
                        break;
                    }
                }
            }
            if (worker.timer != 0) worker.timer--;
        }
        seconds++;
    }

    //part two
    std::cout << seconds << std::endl;
}