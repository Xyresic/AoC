#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
#include <algorithm>
#include <numeric>

struct Voronoi {
    int x, y, size;
    bool infinite;

    Voronoi(int x, int y) {
        this->x = x;
        this->y = y;
        this->size = 0;
        this->infinite = false;
    }
};

std::ifstream input("../inputs/input6.txt");
std::string line;
int bound_x = 0, bound_y = 0;

int main(void) {
    std::vector<Voronoi> areas;
    int safe_size = 0;
    std::regex num("\\d+");
    while(getline(input, line)) {
        std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), num);
        int x = stoi(rit->str()), y = stoi((++rit)->str());
        areas.emplace_back(x, y);
        if (x > bound_x) bound_x = x;
        if (y > bound_y) bound_y = y;
    }


    for (int x = 0; x < bound_x + 1; x++) {
        for (int y = 0; y < bound_y + 1; y++) {
            std::vector<int> dists(areas.size());
            std::transform(areas.begin(), areas.end(), dists.begin(), [x, y](Voronoi a){return abs(a.x - x) + abs(a.y - y);});
            auto min = std::min_element(dists.begin(), dists.end());
            if (std::count(dists.begin(), dists.end(), *min) == 1) {
                areas[min - dists.begin()].size++;
                if (x == 0 || x == bound_x || y == 0 || y == bound_y) areas[min - dists.begin()].infinite = true;
            }
            if (std::accumulate(dists.begin(), dists.end(), 0) < 10000) safe_size++;
        }
    }

    //part one
    std::cout << std::max_element(areas.begin(), std::remove_if(areas.begin(), areas.end(), [](auto a){
        return a.infinite;
    }), [](auto a, auto b){
        return a.size < b.size;
    })->size << std::endl;

    //part two
    std::cout << safe_size << std::endl;
}