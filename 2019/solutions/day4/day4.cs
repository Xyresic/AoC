using System;
using System.Runtime.InteropServices;

namespace Day4
{
    class Driver
    {
        static bool IsValid(string num, bool strict=false)
        {
            char currentGroup = '\0';
            bool dup = false;
            for (int i = 1; i < num.Length; i++)
            {
                int diff = num[i] - num[i - 1];
                if (diff < 0) return false;
                if (diff == 0 && (!dup || currentGroup != '\0'))
                {
                    if (currentGroup == '\0')
                    {
                        dup = true;
                        if (strict) currentGroup = num[i];
                    }
                    else dup = false;
                }
                else currentGroup = '\0';
            }
            return dup;
        }
        
        static void Main(string[] args)
        {
            int countOne = 0, countTwo = 0;
            for (int num = 197487; num < 673252; num++)
            {
                if (IsValid(num.ToString())) countOne++;
                if (IsValid(num.ToString(), true)) countTwo++;
            }
            
            //part one
            Console.WriteLine(countOne);
            //part two
            Console.WriteLine(countTwo);
        }
    }
}