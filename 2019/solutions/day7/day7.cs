using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Text.RegularExpressions;

namespace day7
{
    class Computer
    {
        delegate void Operation(int[] intcode, List<int> parameters);
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

        int[] intcode;
        int codeIndex, inputIndex;
        public List<int> inputs, outputs;
        public bool terminated = false;
        Dictionary<char, Operation> operations;

        public Computer(int[] intcode, List<int> inputs, List<int> outputs)
        {
            this.intcode = (int[]) intcode.Clone();
            this.inputs = inputs;
            this.outputs = outputs;
            codeIndex = 0;
            inputIndex = 0;
            operations = new()
            {
                {'1', (c, p) => 
                    {
                        c[p[2]] = p[1] + p[0];
                        codeIndex += 4;
                    }
                },
                {'2', (c, p) =>
                    {
                        c[p[2]] = p[1] * p[0];
                        codeIndex += 4;
                    }
                },
                {'3', GetInput},
                {'4', WriteOutput},
                {'5', (c, p) => 
                    {
                        if (p[0] != 0) codeIndex = p[1];
                        else codeIndex += 3; 
                    }
                },
                {'6', (c, p) =>
                    {
                        if (p[0] == 0) codeIndex = p[1];
                        else codeIndex += 3;
                    }
                },
                {'7', (c, p) =>
                    {
                        if (p[0] < p[1]) c[p[2]] = 1;
                        else c[p[2]] = 0;
                        codeIndex += 4;
                    }
                },
                {'8', (c, p) =>
                    {
                        if (p[0] == p[1]) c[p[2]] = 1;
                        else c[p[2]] = 0;
                        codeIndex += 4;
                    }
                }
            };
        }

        void GetInput(int[] code, List<int> parameters)
        {
            code[parameters[0]] = inputs[inputIndex];
            codeIndex += 2;
            inputIndex++;
        }

        void WriteOutput(int[] code, List<int> parameters)
        {
            outputs.Add(parameters[0]);
            codeIndex += 2;
        }
        
        public void RunIntcode()
        {
            while (!terminated)
            {
                string val = intcode[codeIndex].ToString();
                if (opCode.IsMatch(val))
                {
                    bool[] pTypes = paramTypes[val[^1]];
                    int numParams = pTypes.Length;
                    val = new string('0', numParams - val.Length + 2) + val;
                    List<int> parameters = new List<int>();
                    for (int i = 0; i < numParams; i++)
                    {
                        int ind = codeIndex + numParams - i;
                        if (pTypes[numParams - i - 1] || val[i] == '1') parameters.Insert(0, intcode[ind]);
                        else parameters.Insert(0, intcode[intcode[ind]]);
                    }
                    operations[val[^1]](intcode, parameters);
                    if (codeIndex < 0 || codeIndex >= intcode.Length) terminated = true;
                    continue;
                }
                if (val != "99") Console.WriteLine("Error");
                terminated = true;
            }
        }
    }
    
    class Driver
    {
        static void Swap(int[] array, int pos1, int pos2)
        {
            int temp = array[pos1];
            array[pos1] = array[pos2];
            array[pos2] = temp;
        }
        
        static List<int[]> HeapsAlg(int[] array, int k)
        {
            List<int[]> perms = new List<int[]>();
            if (k == 1)
            {
                perms.Add((int[])array.Clone());
                return perms;
            }
            perms.AddRange(HeapsAlg(array, k - 1));
            for (int i = 0; i < k - 1; i++)
            {
                if (k % 2 == 0) Swap(array, i, k - 1);
                else Swap(array, 0, k - 1);
                perms.AddRange(HeapsAlg(array, k - 1));
            }
            return perms;
        }

        static int RunCircuit(int[] intcode, int[] settings, bool feedback = false)
        {
            Computer[] comps = new Computer[5];
            for (int i = 0; i < 5; i++)
            {
                comps[i] = new Computer(intcode, new List<int>(new int[]{settings[i]}), new List<int>());
                if (i > 0) comps[i - 1].outputs = comps[i].inputs;
            }
            comps[0].inputs.Add(0);
            if (feedback)
            {
                comps[4].outputs = comps[0].inputs;
                int currentComp = 0;
                while (comps.Any(c => !c.terminated))
                {
                    try
                    {
                        comps[currentComp].RunIntcode();
                    }
                    catch (ArgumentOutOfRangeException) {}
                    currentComp = (currentComp + 1) % 5;
                }
            }
            else for (int i = 0; i < 5; i++) comps[i].RunIntcode();
            return comps[4].outputs[^1];
        }
        
        static void Main(string[] args)
        {
            string line = File.ReadAllText("../../inputs/input7.txt");
            int[] intcode = Array.ConvertAll(line.Split(','), s => int.Parse(s));

            //part one
            List<int> outputs = new List<int>();
            foreach (int[] setting in HeapsAlg(new[]{0, 1, 2, 3, 4}, 5))
            {
                outputs.Add(RunCircuit(intcode, setting));
            }
            Console.WriteLine(outputs.Max());
            
            //part two
            outputs = new List<int>();
            foreach (int[] setting in HeapsAlg(new[]{5, 6, 7, 8, 9}, 5))
            {
                outputs.Add(RunCircuit(intcode, setting, true));
            }
            Console.WriteLine(outputs.Max());
        }
    }
}