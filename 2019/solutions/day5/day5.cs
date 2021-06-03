using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace day5
{
    class Driver
    {
        delegate void Operation(int[] intcode, List<int> parameters, List<int> outputs);
        static int index = 0;
        static Regex opCode = new(@"^1*0*[1-8]$");
        static Dictionary<char, bool[]> paramTypes = new()
        {
            {'1', new[]{false, false, true}},
            {'2', new[]{false, false, true}},
            {'3', new[]{true}},
            {'4', new[]{false}},
            {'5', new[]{false, false}},
            {'6', new[]{false, false}},
            {'7', new[]{false, false, true}},
            {'8', new[]{false, false, true}}
        };
        private static Dictionary<char, Operation> operations = new()
        {
            {'1', (c, p, o) => 
                {
                    c[p[2]] = p[1] + p[0];
                    index += 4;
                }
            },
            {'2', (c, p, o) =>
                {
                    c[p[2]] = p[1] * p[0];
                    index += 4;
                }
            },
            {'4', (c, p, o) =>
                {
                    o.Add(p[0]);
                    index += 2;
                }
            },
            {'5', (c, p, o) => 
                {
                    if (p[0] != 0) index = p[1];
                    else index += 3; 
                }
            },
            {'6', (c, p, o) =>
                {
                    if (p[0] == 0) index = p[1];
                    else index += 3;
                }
            },
            {'7', (c, p, o) =>
                {
                    if (p[0] < p[1]) c[p[2]] = 1;
                    else c[p[2]] = 0;
                    index += 4;
                }
            },
            {'8', (c, p, o) =>
                {
                    if (p[0] == p[1]) c[p[2]] = 1;
                    else c[p[2]] = 0;
                    index += 4;
                }
            }
        };

        static int[] RunIntcode(int[] code, int input)
        {
            int[] intcode = (int[]) code.Clone();
            index = 0;
            List<int> outputs = new List<int>();
            operations['3'] = (c, p, o) => 
            {
                c[p[0]] = input;
                index += 2;
            };

            while (index >= 0 && index < intcode.Length)
            {
                string val = intcode[index].ToString();
                if (opCode.IsMatch(val))
                {
                    bool[] pTypes = paramTypes[val[^1]];
                    int numParams = pTypes.Length;
                    val = new string('0', numParams - val.Length + 2) + val;
                    List<int> parameters = new List<int>();
                    for (int i = 0; i < numParams; i++)
                    {
                        int ind = index + numParams - i;
                        if (pTypes[numParams - i - 1] || val[i] == '1') parameters.Insert(0, intcode[ind]);
                        else parameters.Insert(0, intcode[intcode[ind]]);
                    }
                    operations[val[^1]](intcode, parameters, outputs);
                    continue;
                }
                if (val != "99") Console.WriteLine("Error");
                break;
            }
            
            return outputs.ToArray();
        }

        static void VerifyOutput(int[] intcode, int input)
        {
            int[] outputs = RunIntcode(intcode, input);
            if (outputs.Length > 0 && outputs[..^1].All(i => i == 0)) Console.WriteLine(outputs[^1]);
            else Console.WriteLine(string.Join(',', outputs));
        }
        
        static void Main(string[] args)
        {
            string line = File.ReadAllText("../../inputs/input5.txt");
            int[] intcode = Array.ConvertAll(line.Split(','), s => int.Parse(s));

            //part one
            VerifyOutput(intcode, 1);
            
            //part two
            VerifyOutput(intcode, 5);
        }
    }
}