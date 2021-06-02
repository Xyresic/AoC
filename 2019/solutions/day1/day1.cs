using System;
using System.IO;

namespace day1
{
    class Driver
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("../../inputs/input1.txt");
            int sum = 0;
            int fuel = 0;
            foreach (string line in lines)
            {
                int mass = int.Parse(line) / 3 - 2;
                sum += mass;
                while (mass > 0)
                {
                    fuel += mass;
                    mass = mass / 3 - 2;
                }
            }

            //part one
            Console.WriteLine(sum);

            //part two
            Console.WriteLine(fuel);
        }
    }    
}
