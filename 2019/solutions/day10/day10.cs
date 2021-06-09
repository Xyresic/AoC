using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;

namespace day10
{
    class Driver
    {
        static string Hash(int[] coord)
        {
            return $"{coord[0]},{coord[1]}";
        }

        static int[] Normalize(int[] origin, int[] point)
        {
            return new[]{point[0] - origin[0], point[1] - origin[1]};
        }

        static double Distance(int[] point1, int[] point2)
        {
            int[] diff = Normalize(point1, point2);
            return Math.Sqrt(Math.Pow(diff[0], 2) + Math.Pow(diff[1], 2));
        }
        
        static bool OnRay(int[] origin, int[] point1, int[] point2)
        {
            int[] normal1 = Normalize(origin, point1), normal2 = Normalize(origin, point2);
            return Math.Atan2(normal1[0], normal1[1]) == Math.Atan2(normal2[0], normal2[1]);
        }

        static int[] ClosestToAngle(List<int[]> asteroids, double angle)
        {
            List<double> angleDiffs = asteroids.ConvertAll(c => Math.Atan2(-c[1], c[0]) - angle);
            double best;
            if (angleDiffs.Any(d => d < 0)) best = angleDiffs.FindAll(d => d < 0).Max();
            else best = angleDiffs.Max();
            
            double minDist = Double.MaxValue;
            int[] asteroid = new int[2];
            for (int i = 0; i < asteroids.Count; i++)
            {
                double dist = Distance(asteroids[i], new[]{0, 0});
                if (angleDiffs[i] == best && dist < minDist)
                {
                    minDist = dist;
                    asteroid = asteroids[i];
                }
            }
            return asteroid;
        }
        
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("../../inputs/input10.txt");
            Dictionary<int[], HashSet<string>> obstructed = new Dictionary<int[], HashSet<string>>();
            List<int[]> asteroids = new List<int[]>();
            for (int y = 0; y < lines.Length; y++)
            {
                for (int x = 0; x < lines[y].Length; x++)
                {
                    if (lines[y][x] == '#')
                    {
                        int[] coord = {x, y};
                        asteroids.Add(coord);
                        obstructed.Add(coord, new HashSet<string>(new[]{Hash(coord)}));
                    }
                }
            }

            //part one
            for (int i = 0; i < asteroids.Count - 1; i++)
            {
                for (int j = i + 1; j < asteroids.Count; j++)
                {
                    int[] station = asteroids[i], asteroid = asteroids[j];
                    if (!obstructed[station].Contains(Hash(asteroid)))
                    {
                        foreach (int[] obstruction in asteroids)
                        {
                            if (!obstruction.SequenceEqual(station) && !obstruction.SequenceEqual(asteroid) && 
                                OnRay(station, asteroid, obstruction))
                            {
                                if (Distance(station, asteroid) > Distance(station, obstruction))
                                {
                                    obstructed[station].Add(Hash(asteroid));
                                    obstructed[asteroid].Add(Hash(station));
                                }
                                else
                                {
                                    obstructed[station].Add(Hash(obstruction));
                                    obstructed[obstruction].Add(Hash(station));
                                }
                            }
                        }
                    }
                }
            }
            int maxCount = 0;
            int[] origin = new int[2];
            foreach (int[] asteroid in asteroids)
            {
                int detectable = asteroids.Count - obstructed[asteroid].Count;
                if (detectable > maxCount)
                {
                    maxCount = detectable;
                    origin = asteroid;
                }
            }
            Console.WriteLine(maxCount);
            
            //part two
            double angle = Math.PI / 2 + 0.000001;
            asteroids.Remove(origin);
            asteroids = asteroids.ConvertAll(c => Normalize(origin, c));
            for (int i = 0; i < 199; i++)
            {
                int[] next = ClosestToAngle(asteroids, angle);
                angle = Math.Atan2(-next[1], next[0]);
                asteroids.Remove(next);
            }
            int[] last = ClosestToAngle(asteroids, angle);
            Console.WriteLine((last[0] + origin[0]) * 100 + last[1] + origin[1]);
        }
    }
}