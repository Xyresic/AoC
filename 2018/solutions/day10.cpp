#include <iostream>
#include <fstream>
#include <vector>
#include <regex>
#include <algorithm>

std::ifstream input("../inputs/input10.txt");
std::string line;
std::regex num("-*\\d+");

struct Particle {
    int x, y, vx, vy;

    Particle(int vy, int vx , int y, int x) {
        this->x = x;
        this->y = y;
        this->vx = vx;
        this->vy = vy;
    }
};

int main(void) {
    std::vector <Particle> particles;
    while (getline(input, line)) {
        std::regex_iterator <std::string::iterator> rit(line.begin(), line.end(), num);
        particles.emplace_back(stoi((++rit)->str()), stoi((++rit)->str()), stoi((++rit)->str()), stoi(rit->str()));
    }

    int bound_x, bound_y, min_x, max_x, min_y, max_y, seconds = 0;
    do {
        seconds++;
        for (Particle &particle : particles) {
            particle.x += particle.vx;
            particle.y += particle.vy;
        }
        min_x = std::min_element(particles.begin(), particles.end(),[](auto a, auto b){return a.x < b.x;})->x;
        max_x = std::max_element(particles.begin(), particles.end(),[](auto a, auto b){return a.x < b.x;})->x;
        min_y = std::min_element(particles.begin(), particles.end(),[](auto a, auto b){return a.y < b.y;})->y;
        max_y = std::max_element(particles.begin(), particles.end(),[](auto a, auto b){return a.y < b.y;})->y;
        bound_x = max_x - min_x;
        bound_y = max_y - min_y;
    } while (bound_y > 10);

    //part one
    std::vector<std::vector<bool>> sky;
    for (int i = 0; i < bound_y + 1; i++) sky.emplace_back(bound_x + 1);
    for (Particle& particle : particles) sky[particle.y - min_y][particle.x - min_x] = true;
    for (auto &row : sky) {
        for (bool c : row) {
            if (c) std::cout << '#';
            else std::cout << ' ';
        }
        std::cout << std::endl;
    }

    //part two
    std::cout << seconds << std::endl;
}