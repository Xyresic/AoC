using System;
using System.IO;
using System.Collections.Generic;

namespace Day3
{
    class Driver
    {
        delegate void Action(string hash, int steps);
        static void Traverse(string[] moves, Action f)
        {
            int x = 0, y = 0, steps = 0;
            foreach (string move in moves)
            {
                int amount = int.Parse(move.Substring(1));
                for (int i = 0; i < amount; i++)
                {
                    steps++;
                    switch (move[0])
                    {
                        case 'U':
                            y++;
                            break;
                        case 'D':
                            y--;
                            break;
                        case 'L':
                            x--;
                            break;
                        default:
                            x++;
                            break;
                    }
                    
                    f($"{x},{y}", steps);
                }
            }
        }
        
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("../../inputs/input3.txt");
            Dictionary<string, int> intersections = new Dictionary<string, int>();
            Dictionary<string, int> firstWire = new Dictionary<string, int>();

            void Add(string hash, int steps)
            {
                firstWire.TryAdd(hash, steps);
            }
            Traverse(lines[0].Split(','), Add);

            void Intersect(string hash, int steps)
            {
                if (firstWire.ContainsKey(hash)) intersections.TryAdd(hash, firstWire[hash] + steps);
            }
            Traverse(lines[1].Split(','), Intersect);
            
            int minDist = Int32.MaxValue, minDelay = Int32.MaxValue;
            foreach (KeyValuePair<string, int> intersection in intersections)
            {
                string hash = intersection.Key;
                int delimIndex = hash.IndexOf(',');
                int manDist = Math.Abs(int.Parse(hash.Substring(0, delimIndex))) + 
                              Math.Abs(int.Parse(hash.Substring(delimIndex + 1)));
                if (manDist < minDist) minDist = manDist;
                if (intersection.Value < minDelay) minDelay = intersection.Value;
            }
            
            //part one
            Console.WriteLine(minDist);
            //part two
            Console.WriteLine(minDelay);
        }
    }
}
