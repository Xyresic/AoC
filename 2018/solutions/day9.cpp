#include <iostream>
#include <list>
#include <algorithm>

long long marbles(int last) {
    long long players[432] = {};
    int ind = 1;
    std::list<int> marbles = {0, 1};
    std::list<int>::iterator it = ++marbles.begin();
    for (int i = 2; i < last; i++) {
        if (i % 23 == 0) {
            ind -= 7;
            if (ind < 0) {
                ind += marbles.size();
                it = marbles.begin();
                advance(it, ind);
            } else advance(it, -7);
            players[(i - 1) % 432] += i + *it;
            it = marbles.erase(it);
        } else {
            ind += 2;
            if (ind >= marbles.size()) {
                ind %= marbles.size();
                it = marbles.begin();
                advance(it, ind);
            } else advance(it, 2);
            it = marbles.insert(it, i);
        }
    }

    return *std::max_element(players, players + 432);
}

int main(void) {
    //part one
    std::cout << marbles(71020) << std::endl;

    //part two
    std::cout << marbles(7101901) << std::endl;
}