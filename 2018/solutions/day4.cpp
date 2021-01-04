#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <regex>
#include <unordered_map>

struct Guard {
    int id;
    int minutes[60];
    int asleep;

    Guard(int id) {
        this->id = id;
        for (int i = 0; i < 60; i++) minutes[i] = 0;
    }

    int sum_minutes() {
        int sum = 0;
        for (int i = 0; i < 60; i++) sum += minutes[i];
        return sum;
    }

    int max_minute() {
        int max = 0;
        for (int i = 0; i < 60; i++) if (minutes[i] > max) max = minutes[i];
        return max;
    }
};

struct Log {
    int month, day, hour, min, id = -1;
    bool awake = true;

    Log(int month, int day, int hour, int min) {
        this->month = month;
        this->day = day;
        this->hour = hour;
        this->min = min;
    }
};

bool chronological (Log& a, Log& b) {
    return a.month < b.month || (a.month == b.month && (a.day < b.day || (a.day == b.day && (a.hour < b.hour || (a.hour == b.hour && a.min < b.min)))));
}

std::ifstream input("../inputs/input4.txt");
std::string line;
std::unordered_map<int, Guard> guards;
std::vector<Log> logs;
int cur_guard_id;

int main(void) {
    while (getline(input, line)) {
        std::vector<int> vals;
        std::regex num("\\d+");
        std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), num), rend;
        while (rit != rend) {
            vals.push_back(stoi(rit->str()));
            rit++;
        }
        Log log(vals[1], vals[2], vals[3], vals[4]);
        if (vals.size() == 5) log.awake = line.find("falls asleep") == -1;
        else log.id = vals[5];
        logs.push_back(log);
    }
    std::sort(logs.begin(), logs.end(), chronological);
    for (int i = 0; i < logs.size(); i++) {
        Log log = logs[i];
        if (log.id != -1) {
            if (i != 0 && !logs[i - 1].awake) {
                for (int i = guards.at(cur_guard_id).asleep; i < 60; i++) {
                    guards.at(cur_guard_id).minutes[i]++;
                }
            }
            if (guards.find(log.id) == guards.end()) {
                Guard guard(log.id);
                guards.emplace(log.id, guard);
            }
            cur_guard_id = log.id;
        } else if (log.awake) {
            for (int i = guards.at(cur_guard_id).asleep; i < log.min; i++) {
                guards.at(cur_guard_id).minutes[i]++;
            }
        } else guards.at(cur_guard_id).asleep = log.min;
    }
    auto max = std::max_element(guards.begin(), guards.end(), [](auto a, auto b){return a.second.sum_minutes() < b.second.sum_minutes();});
    int min = 0;
    int times_asleep = 0;
    for (int i = 0; i < 60; i++) {
        if (max->second.minutes[i] > times_asleep) {
            times_asleep = max->second.minutes[i];
            min = i;
        }
    }

    //part one
    std::cout << max->first * min << std::endl;

    //part two
    max =  std::max_element(guards.begin(), guards.end(), [](auto a, auto b){return a.second.max_minute() < b.second.max_minute();});
    int max_min = max->second.max_minute();
    for (int i = 0; i < 60; i++) {
        if (max->second.minutes[i] == max_min) {
            min = i;
            break;
        }
    }

    //part two
    std::cout << max->first * min << std::endl;
}