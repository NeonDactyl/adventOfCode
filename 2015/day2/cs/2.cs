using System;
using System.Collections.Generic;
using System.Linq;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
			string[] text = System.IO.File.ReadAllText("2.in").Trim().Split("\n");
			List<int> dimensions;
			int totalWrappingPaper = 0;
			int totalRibbon = 0;
			int[] areas =  new int[3];
			int[] perimeters = new int[3];

			foreach (var line in text) {
				dimensions = line.Split("x").Select(x => Int32.Parse(x)).ToList();

				int x = dimensions[0];
				int y = dimensions[1];
				int z = dimensions[2];

				areas[0] = x * y;
				areas[1] = y * z;
				areas[2] = z * x;

				perimeters[0] = 2 * (x + y);
				perimeters[1] = 2 * (y + z);
				perimeters[2] = 2 * (z + x);

				totalWrappingPaper += areas.Sum() * 2 + areas.Min();
				totalRibbon += perimeters.Min() + x * y * z;
			}

			Console.WriteLine($"Wrapping Paper: {totalWrappingPaper}\nRibbon: {totalRibbon}");
        }
    }
}
