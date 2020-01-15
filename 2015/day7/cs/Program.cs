using System;
using System.Collections.Generic;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] fileLines = System.IO.File.ReadAllLines("7.in");
			Dictionary<string, WireConnection> connections = new Dictionary<string, WireConnection>();
			foreach (string line in fileLines)
			{
				string key = line.Split("->")[1];
				connections.Add(line.Split("->")[1].Trim(), new WireConnection(line));
			}
			ushort a = connections["a"].getOutputSignal(connections);
			Console.WriteLine(a);
        }
    }
}
