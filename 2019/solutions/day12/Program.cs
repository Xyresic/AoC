using System;
using System.Linq;
using System.Collections.Generic;

namespace day12
{
    class Moon
    {
        public int x, y, z, dx = 0, dy = 0, dz = 0;

        public Moon(int x, int y, int z)
        {
            this.x = x;
            this.y = y;
            this.z = z;
        }

        static int Signum(int num)
        {
            return num switch
            {
                > 0 => 1,
                < 0 => -1,
                _ => 0
            };
        }

        public void ApplyGravity(List<Moon> moons)
        {
            foreach (Moon moon in moons)
            {
                if (moon != this)
                {
                    dx += Signum(moon.x - x);
                    dy += Signum(moon.y - y);
                    dz += Signum(moon.z - z);
                }
            }
        }

        public void ApplyVelocity()
        {
            x += dx;
            y += dy;
            z += dz;
        }

        public int Energy()
        {
            return (Math.Abs(x) + Math.Abs(y) + Math.Abs(z)) * (Math.Abs(dx) + Math.Abs(dy) + Math.Abs(dz));
        }

        public string ToString(char axis)
        {
            switch (axis)
            {
                case 'x':
                    return $"{x},{dx}";
                case 'y':
                    return $"{y},{dy}";
                default:
                    return $"{z},{dz}";
            }
        }
    }
    
    class Driver
    {
        static void Step(List<Moon> moons)
        {
            foreach (Moon moon in moons)
            {
                moon.ApplyGravity(moons);
            }
            foreach (Moon moon in moons)
            {
                moon.ApplyVelocity();
            }
        }

        static string Hash(List<Moon> moons, char axis)
        {
            return string.Join(',', moons.ConvertAll(m => m.ToString(axis)));
        }

        static long GCD(long a, long b)
        {
            while (b != 0)
            {
                long t = b;
                b = a % b;
                a = t;
            }
            return a;
        }
        
        static long LCM(long a, long b)
        {
            return a / GCD(a, b) * b;
        }
        
        static void Main(string[] args)
        {
            List<Moon> moons = new List<Moon>
            {
                new(-7, -8, 9),
                new(-12, -3, -4),
                new(6, -17, -9),
                new(4, -10, -6)
            };
            Dictionary<string, long> xStates = new(), yStates = new(), zStates = new();
            long xCycle = 0, yCycle = 0, zCycle = 0, xStart = 0, yStart = 0, zStart = 0;
            long step = 0;

            void CheckStates()
            {
                if (xStart == 0)
                {
                    string xHash = Hash(moons, 'x');
                    try
                    {
                        xStates.Add(xHash, step);
                    }
                    catch (ArgumentException)
                    {
                        xStart = xStates[xHash];
                        xCycle = step - xStart;
                    }
                }
                if (yStart == 0)
                {
                    string yHash = Hash(moons, 'y');
                    try
                    {
                        yStates.Add(yHash, step);
                    }
                    catch (ArgumentException)
                    {
                        yStart = yStates[yHash];
                        yCycle = step - yStart;
                    }
                }
                if (zStart == 0)
                {
                    string zHash = Hash(moons, 'z');
                    try
                    {
                        zStates.Add(zHash, step);
                    }
                    catch (ArgumentException)
                    {
                        zStart = zStates[zHash];
                        zCycle = step - zStart;
                    }
                }
            }

            //part one
            for (int _ = 0; _ < 1000; _++)
            {
                CheckStates();
                Step(moons);
                step++;
            }
            Console.WriteLine(moons.Sum(m => m.Energy()));
            
            //part two
            while (xStart == 0 || yStart == 0 || zStart == 0)
            {
                CheckStates();
                Step(moons);
                step++;
            }
            Console.WriteLine(new[]{xStart, yStart, zStart}.Max() + LCM(LCM(xCycle, yCycle), zCycle) - 1);
        }
    }
}