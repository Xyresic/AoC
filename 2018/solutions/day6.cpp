#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
#include <algorithm>

struct Voronoi {
    int x, y, size;
    bool infinite;
    std::vector<std::vector<int>> edge;

    Voronoi(int x, int y) {
        this->x = x;
        this->y = y;
        this->size = 1;
        this->infinite = false;
        this->edge.emplace_back(std::vector<int>{x,y});
    }

    bool operator !=(Voronoi& other) {
        return this->x != other.x || this->y != other.y;
    }
};

std::ifstream input("../inputs/input6.txt");
std::string line;
int bound_x = 0, bound_y = 0;

bool contained(int x, int y, std::vector<std::vector<int>>& container) {
    for (auto cell : container) if (cell[0] == x && cell[1] == y) return true;
    return false;
}

int main(void) {
    std::vector<Voronoi> areas;
    std::vector<std::vector<int>> visited;
    std::regex num("\\d+");
    while(getline(input, line)) {
        std::regex_iterator<std::string::iterator> rit(line.begin(), line.end(), num);
        int x = stoi(rit->str()), y = stoi((++rit)->str());
        areas.emplace_back(x, y);
        visited.emplace_back(std::vector<int>{x, y});
        if (x > bound_x) bound_x = x;
        if (y > bound_y) bound_y = y;
    }

    bool incomplete = true;
    while (incomplete) {
        incomplete = false;
        for (Voronoi& area : areas) {
            std::cout << "" << area.x << "," << area.y << " | ";
            int edge_length = area.edge.size();
            if (!area.infinite) {
                for (int i = 0; i < edge_length; i++) {
                    std::vector<int> cell = area.edge[i];
                    for (int dx = -1; dx < 2; dx++) {
                        for (int dy = dx == 0? -1:0; dy < 2; dy += 2) {
                            int new_x = cell[0] + dx, new_y = cell[1] + dy;
                            if (!contained(new_x, new_y, visited)) {
                                visited.emplace_back(std::vector<int>{new_x, new_y});
                                int dist = abs(area.x - new_x) + abs(area.y - new_y);
                                bool min = true;
                                for (Voronoi& other : areas) {
                                    if (other != area && dist >= abs(other.x - new_x) + abs(other.y - new_y)) {
                                        min = false;
                                        break;
                                    }
                                }
                                if (min) {
                                    if (new_x <= 0 || new_x >= bound_x || new_y <= 0 || new_y >= bound_y) area.infinite = true;
                                    area.size++;
                                    area.edge.emplace_back(std::vector<int>{new_x, new_y});
                                    incomplete = true;
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    //part one
    std::cout << std::max_element(areas.begin(), areas.end(), [](auto a, auto b){return a.infinite || a.size < b.size;})->size << std::endl;
}