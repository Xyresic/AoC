using System;
using System.IO;
using System.Collections.Generic;

namespace day6
{
    class Driver
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("../../inputs/input6.txt");
            Dictionary<string, List<string>> orbits = new Dictionary<string, List<string>>();
            Dictionary<string, string> orbited = new Dictionary<string, string>();

            foreach (string orbit in lines)
            {
                string center = orbit[..3];
                string satellite = orbit[4..];
                if (orbits.ContainsKey(center)) orbits[center].Add(satellite);
                else orbits.Add(center, new List<string>(new[]{satellite}));
                orbited.Add(satellite, center);
            }
            
            //part one
            int count = 0;
            int depth = 0;
            List<string> currentLayer = new List<string>(new[]{"COM"});
            while (currentLayer.Count != 0)
            {
                count += depth * currentLayer.Count;
                List<string> nextLayer = new List<string>();
                foreach (string center in currentLayer)
                {
                    try
                    {
                        nextLayer.AddRange(orbits[center]);
                    }
                    catch (KeyNotFoundException) {}
                }
                currentLayer = nextLayer;
                depth++;
            }
            Console.WriteLine(count);
            
            //part two
            depth = 0;
            HashSet<string> thisLayer = new HashSet<string>(new[]{orbited["YOU"]});
            HashSet<string> visited = new HashSet<string>(new[]{"YOU"});
            while (!thisLayer.Contains("SAN"))
            {
                visited.UnionWith(thisLayer);
                HashSet<string> nextLayer = new HashSet<string>();
                foreach (string location in thisLayer)
                {
                    try
                    {
                        string center = orbited[location];
                        if (!visited.Contains(center)) nextLayer.Add(center);
                        foreach (string neighbor in orbits[location])
                        {
                            if (!visited.Contains(neighbor)) nextLayer.Add(neighbor);
                        }
                    }
                    catch (KeyNotFoundException) {}
                }
                thisLayer = nextLayer;
                depth++;
            }
            Console.WriteLine(depth - 1);
        }
    }
}