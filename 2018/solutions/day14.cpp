#include <iostream>

int main(void) {
    std::string input = "681901";
    std::string recipes = "3710101";
    int elf1 = 1, elf2 = 1, ind1 = 6, ind2 = 4;
    while (input.compare(recipes.substr(recipes.size() - 7, 6)) != 0) {
        recipes += std::to_string(elf1 + elf2);
        ind1 = (ind1 + 1 + elf1) % recipes.size();
        ind2 = (ind2 + 1 + elf2) % recipes.size();
        elf1 = recipes[ind1] - '0';
        elf2 = recipes[ind2] - '0';
        if (recipes.size() == 681901 + 10) {
            //part one
            for (int i = 0; i < 10; i++) std::cout << recipes[recipes.size() - 10 + i]- '0';
            std::cout << std::endl;
        }
    }

    //part two
    std::cout << recipes.size() - 7 << std::endl;
}