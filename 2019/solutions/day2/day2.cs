using System;
using System.IO;

namespace day2
{
    class Driver
    {
        static int RunIntcode(int[] code, int noun, int verb)
        {
            int[] intcode = (int[]) code.Clone();
            int index = 0;
            intcode[1] = noun;
            intcode[2] = verb;

            while (index >= 0 && index < intcode.Length)
            {
                switch (intcode[index])
                {
                    case 1:
                        intcode[intcode[index + 3]] = intcode[intcode[index + 1]] + intcode[intcode[index + 2]];
                        index += 4;
                        break;
                    case 2:
                        intcode[intcode[index + 3]] = intcode[intcode[index + 1]] * intcode[intcode[index + 2]];
                        index += 4;
                        break;
                    case 99:
                        index = -1;
                        break;
                    default:
                        index = -1;
                        Console.WriteLine("Error");
                        break;
                }
            }

            return intcode[0];
        }

        static void Main(string[] args)
        {
            string lines = File.ReadAllText("../../inputs/input2.txt");
            int[] intcode = Array.ConvertAll(lines.Split(','), s => int.Parse(s));

            //part one
            Console.WriteLine(RunIntcode(intcode, 12, 2));

            //part two
            for (int noun = 0; noun < 100; noun++)
            {
                for (int verb = 0; verb < 100; verb++)
                {
                    if (RunIntcode(intcode, noun, verb) == 19690720)
                    {
                        Console.WriteLine(noun * 100 + verb);
                    }
                }
            }
        }
    }
}
