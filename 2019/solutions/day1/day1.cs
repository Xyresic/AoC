class Day1 {
    static void Main(string[] args) {
        string[] lines = System.IO.File.ReadAllLines("../../inputs/input1.txt");
        int sum = 0;
        int fuel = 0;
        foreach (string line in lines) {
            int mass = int.Parse(line) / 3 - 2;
            sum += mass;
            while (mass > 0) {
                fuel += mass;
                mass = mass / 3 - 2;
            }
        }

        //part one
        System.Console.WriteLine(sum);

        //part two
        System.Console.WriteLine(fuel);
    }
}