using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text.Json;
using System.Text.RegularExpressions;

namespace day14
{
    class Reaction
    {
        public int amt;
        public Dictionary<string, int> reactants;
        public bool primary;

        public Reaction(int amt, MatchCollection reactants, MatchCollection amounts)
        {
            this.amt = amt;
            this.reactants = new Dictionary<string, int>();
            for (int i = 0; i < reactants.Count - 1; i++)
            {
                this.reactants.Add(reactants[i].Value, Int32.Parse(amounts[i].Value));
            }
            primary = this.reactants.Count == 1 && this.reactants.ContainsKey("ORE");
        }

    }
    
    class Driver
    {
        static void Main(string[] args)
        {
            string[] lines = File.ReadAllLines("../../inputs/input14.txt");
            Dictionary<string, int> available = new Dictionary<string, int>();
            Dictionary<string, Reaction> reactions = new Dictionary<string, Reaction>();
            Regex num = new Regex(@"\d+");
            Regex alph = new Regex(@"[A-Z]+");
            foreach (string line in lines)
            {
                MatchCollection numMatches = num.Matches(line);
                MatchCollection alphMatches = alph.Matches(line);
                string product = alphMatches[^1].Value; 
                reactions[product] = new Reaction(Int32.Parse(numMatches[^1].Value), alphMatches, numMatches);
            }

            void TryIncrement(Dictionary<string, int> dict, string key, int inc)
            {
                if (dict.ContainsKey(key))
                {
                    dict[key] += inc;
                }
                else
                {
                    dict[key] = inc;
                }
            }
            
            void ToPrimaries(string product, int amt, Dictionary<string, int> primaries)
            {
                if (amt > 0)
                {
                    available.TryGetValue(product, out var made);
                    if (made > 0)
                    {
                        available[product] = Math.Max(0, made - amt);
                        ToPrimaries(product, amt - made, primaries);
                        return;
                    }
                    Reaction reaction = reactions[product];
                    if (reaction.primary)
                    {
                        TryIncrement(primaries, product, amt);
                        return;
                    }
                    int mult = (int) Math.Ceiling((double) amt / reaction.amt);
                    foreach (KeyValuePair<string, int> pair in reaction.reactants)
                    {
                        ToPrimaries(pair.Key, pair.Value * mult, primaries);
                    }
                    TryIncrement(available, product, mult * reaction.amt - amt);
                }
            }
            
            int MinOre(string product, int amt)
            {
                int ore = 0;
                Dictionary<string, int> primes = new Dictionary<string, int>();
                ToPrimaries(product, amt, primes);
                foreach (KeyValuePair<string, int> pair in primes)
                {
                    Reaction reaction = reactions[pair.Key];
                    int mult = (int) Math.Ceiling((double) pair.Value / reaction.amt);
                    ore += reaction.reactants["ORE"] * mult;
                    TryIncrement(available, pair.Key, mult * reaction.amt - pair.Value);
                }
                return ore;
            }
            
            //part one
            int minOre = MinOre("FUEL", 1);
            Console.WriteLine(minOre);
            
            //part two
            long fuel = 1, ore = 1000000000000 - minOre;
            while (ore > 0)
            {
                minOre = MinOre("FUEL", 1);
                if (ore >= minOre)
                {
                    fuel++;
                    ore -= minOre;
                }
                else break;
            }
            Console.WriteLine(fuel);
        }
    }
}