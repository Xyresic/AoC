using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

namespace day9
{
    class Computer
    {
        delegate void Operation(List<long> parameters);
        static Regex opCode = new(@"^[1-9]$|^[0-2]*0[1-9]$");
        static Dictionary<char, bool[]> paramTypes = new()
        {
            {'1', new[]{false, false, true}},
            {'2', new[]{false, false, true}},
            {'3', new[]{true}},
            {'4', new[]{false}},
            {'5', new[]{false, false}},
            {'6', new[]{false, false}},
            {'7', new[]{false, false, true}},
            {'8', new[]{false, false, true}},
            {'9', new[]{false}}
        };

        Dictionary<long, long> intcode;
        long relativeBase;
        int codeIndex, inputIndex;
        public List<long> inputs, outputs;
        public bool terminated;
        Dictionary<char, Operation> operations;

        void EnsureNonnegative(int index)
        {
            if (index < 0)
            {
                terminated = true;
                throw new ArgumentOutOfRangeException();
            }
        }

        public long Get(dynamic index)
        {
            int ind = (int)index;
            EnsureNonnegative(ind);
            intcode.TryGetValue(ind, out var value);
            return value;
        }

        public void Set(dynamic index, long value)
        {
            int ind = (int)index;
            EnsureNonnegative(ind);
            intcode[ind] = value;
        }

        public Computer(long[] intcode, List<long> inputs, List<long> outputs)
        {
            this.inputs = inputs;
            this.outputs = outputs;
            codeIndex = 0;
            inputIndex = 0;
            relativeBase = 0;
            
            this.intcode = new Dictionary<long, long>();
            for (int i = 0; i < intcode.Length; i++) this.intcode[i] = intcode[i];

            operations = new()
            {
                {'1', p => 
                    {
                        Set(p[2], p[1] + p[0]);
                        codeIndex += 4;
                    }
                },
                {'2', p =>
                    {
                        Set(p[2], p[1] * p[0]);
                        codeIndex += 4;
                    }
                },
                {'3', GetInput},
                {'4', WriteOutput},
                {'5', p => 
                    {
                        if (p[0] != 0) codeIndex = (int)p[1];
                        else codeIndex += 3; 
                    }
                },
                {'6', p =>
                    {
                        if (p[0] == 0) codeIndex = (int)p[1];
                        else codeIndex += 3;
                    }
                },
                {'7', p =>
                    {
                        if (p[0] < p[1]) Set(p[2], 1);
                        else Set(p[2], 0);
                        codeIndex += 4;
                    }
                },
                {'8', p =>
                    {
                        if (p[0] == p[1]) Set(p[2], 1);
                        else Set(p[2], 0);
                        codeIndex += 4;
                    }
                },
                {'9', p =>
                    {
                        relativeBase += p[0];
                        codeIndex += 2;
                    }
                }
            };
        }

        void GetInput(List<long> parameters)
        {
            Set(parameters[0], inputs[inputIndex]);
            codeIndex += 2;
            inputIndex++;
        }

        void WriteOutput(List<long> parameters)
        {
            outputs.Add(parameters[0]);
            codeIndex += 2;
        }
        
        public void RunIntcode()
        {
            while (!terminated)
            {
                try
                {
                    string val = Get(codeIndex).ToString();
                    if (opCode.IsMatch(val))
                    {
                        bool[] pTypes = paramTypes[val[^1]];
                        int numParams = pTypes.Length;
                        val = new string('0', numParams - val.Length + 2) + val;
                        List<long> parameters = new List<long>();
                        for (int i = 0; i < numParams; i++)
                        {
                            int ind = codeIndex + numParams - i;
                            bool isWrite = pTypes[numParams - i - 1];
                            if (!isWrite && val[i] == '0') parameters.Insert(0, Get(Get(ind)));
                            else if (val[i] == '2')
                            {
                                if (isWrite) parameters.Insert(0, Get(ind) + relativeBase);
                                else parameters.Insert(0, Get(Get(ind) + relativeBase));
                            }
                            else parameters.Insert(0, Get(ind));
                        }
                        operations[val[^1]](parameters);
                        continue;
                    }
                    if (val != "99") Console.WriteLine("Error");
                    terminated = true;
                }
                catch (ArgumentOutOfRangeException) {}
            }
        }
    }
    
    class Driver
    {
        static void Main(string[] args)
        {
            string line = File.ReadAllText("../../inputs/input9.txt");
            long[] intcode = Array.ConvertAll(line.Split(','), s => long.Parse(s));
            List<long> output = new List<long>();
            Computer comp = new Computer(intcode, new List<long>(new long[]{1}), output);
            
            //part one
            comp.RunIntcode();
            if (output.Count == 1) Console.WriteLine(output[0]);
            
            //part two
            comp = new Computer(intcode, new List<long>(new long[]{2}), output);
            comp.RunIntcode();
            if (output.Count == 2) Console.WriteLine(output[1]);
        }
    }
}