#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

std::ifstream input("../inputs/input13.txt");
std::string line;

struct Cart {
    int x, y, dx, dy, turn = 0;
    bool moved = false;
    bool crashed = false;

    Cart(int x, int y, int dx, int dy) {
        this->x = x;
        this->y = y;
        this->dx = dx;
        this->dy = dy;
    }

    bool operator<(Cart& other) {
        if (this->moved) {
            if (other.moved) {
                if (this->y == other.y) return this->x > other.x;
                else return this->y > other.y;
            } else return true;
        } else {
            if (other.moved) return false;
            else {
                if (this->y == other.y) return this->x > other.x;
                else return this->y > other.y;
            }
        }
    }
};

void switch_dir_back(Cart& cart) {
    int old_dx = cart.dx;
    cart.dx = cart.dy;
    cart.dy = old_dx;
}

void switch_dir_fwrd(Cart& cart) {
    int old_dx = cart.dx;
    cart.dx = -cart.dy;
    cart.dy = -old_dx;
}

int main(void) {
    std::vector<Cart> carts;
    std::vector<std::vector<char>> tracks;
    int y = 0;
    while(getline(input, line)) {
        std::vector<char> track;
        for (int x = 0; x < line.size(); x++) {
            switch (line[x]) {
                case 'v':
                    carts.emplace_back(x, y, 0, 1);
                    track.push_back('|');
                    break;
                case '^':
                    carts.emplace_back(x, y, 0, -1);
                    track.push_back('|');
                    break;
                case '>':
                    carts.emplace_back(x, y, 1, 0);
                    track.push_back('-');
                    break;
                case '<':
                    carts.emplace_back(x, y, -1, 0);
                    track.push_back('-');
                    break;
                default:
                    track.push_back(line[x]);
            }
        }
        tracks.push_back(track);
        y++;
    }

    //part one
    std::make_heap(carts.begin(), carts.end());
    bool collided = false;
    while (carts.size() > 1) {
        for (int i = 0; i < carts.size(); i++) {
            Cart top = carts.front();
            std::pop_heap(carts.begin(), carts.end());
            top.moved = true;
            top.x += top.dx;
            top.y += top.dy;
            switch (tracks[top.y][top.x]) {
                case '\\':
                    switch_dir_back(top);
                    break;
                case '/':
                    switch_dir_fwrd(top);
                    break;
                case '+':
                    switch (top.turn % 3) {
                        case 0:
                            if (abs(top.dx) == 1) switch_dir_fwrd(top);
                            else switch_dir_back(top);
                            break;
                        case 2:
                            if (abs(top.dx) == 1) switch_dir_back(top);
                            else switch_dir_fwrd(top);
                    }
                    top.turn = ++top.turn % 3;
            }
            for (int i = 0; i < carts.size() - 1; i++) {
                if (carts[i].x == top.x && carts[i].y == top.y) {
                    if (!collided) std::cout << top.x << ',' << top.y << std::endl;
                    collided = true;
                    top.crashed = true;
                    carts[i].crashed = true;
                }
            }
            carts[carts.size() - 1] = top;
        }
        for (int i = 0; i < carts.size(); i++) {
            if (carts[i].crashed) {
                carts.erase(carts.begin() + i);
                i--;
            } else carts[i].moved = false;
        }
        std::make_heap(carts.begin(), carts.end());
    }

    //part two
    std::cout << carts[0].x << ',' << carts[0].y << std::endl;
}