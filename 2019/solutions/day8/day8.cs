using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace day8
{
    class Driver
    {
        static void Main(string[] args)
        {
            string input = File.ReadAllText("../../inputs/input8.txt").Trim();
            List<string> layers = new List<string>();
            int minCount = Int32.MaxValue;
            string bestLayer = "";
            for (int i = 0; i < input.Length; i += 150)
            {
                string thisLayer = input[i..(i + 150)];
                layers.Add(thisLayer);
                int count = thisLayer.Count(c => c == '0');
                if (count < minCount)
                {
                    minCount = count;
                    bestLayer = thisLayer;
                }
            }
            
            //part one
            Console.WriteLine(bestLayer.Count(c => c == '1') * bestLayer.Count(c => c == '2'));
            
            //part two
            char[] result = new char[150];
            for (int i = 0; i < 150; i++)
            {
                for (int j = 0; j < layers.Count; j++)
                {
                    if (layers[j][i] != '2')
                    {
                        result[i] = layers[j][i];
                        break;
                    }
                }
            }
            for (int i = 0; i < 6; i++)
            {
                for (int j = i * 25; j < (i + 1) * 25; j++) Console.Write(result[j] == '1'? "@@":"  ");
                Console.WriteLine();
            }
        }
    }
}