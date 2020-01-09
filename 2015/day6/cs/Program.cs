using System;
using System.Collections.Generic;

namespace cs
{
    class Program
    {
		static int[,] lights = new int[1000,1000];

        static void Main(string[] args)
        {
			// read all lines into list of instructions
			// foreach line in lines
			// line.Split(" ");
			// if line[0] == "toggle"
			// 		toggle(line[1], line[3])
			// else
			// 		turn(line[1], line[2], line[4])
			
			string[] lines = System.IO.File.ReadAllLines("6.in");

			for (int i = 0; i < 1000; i++) {
				for (int j = 0; j < 1000; j++) {
					Program.lights[i,j] = 0;
				}
			}

			foreach(string line in lines) {
				string[] sections = line.Split(" ");
				switch (sections[0]) {
					case "turn":
						if (sections[1] == "on") turnOn(sections[2], sections[4]);
						else turnOff(sections[2], sections[4]);
						break;
					case "toggle":
						toggle(sections[1], sections[3]);
						break;
				}
			}

			int count = 0;
			for (int x = 0; x < 1000; x++) {
				for (int y = 0; y < 1000; y++) {
					count += lights[x, y];
				}
			}

			Console.WriteLine(count);
        }

		static void turnOn(string p1, string p2) {
			// TODO: Implement this.
			string[] p1s = p1.Split(",");
			Console.WriteLine(p1);
			Console.WriteLine(p1s);
			int x1 = Int32.Parse(p1s[0]);
			int y1 = Int32.Parse(p1s[1]);

			string[] p2s = p2.Split(",");
			int x2 = Int32.Parse(p2s[0]);
			int y2 = Int32.Parse(p2s[1]);

			if (x1 > x2) {
				int tmp = x1;
				x1 = x2;
				x2 = tmp;
			}

			if (y1 > y2) {
				int tmp = y1;
				y1 = y2;
				y2 = tmp;
			}

			for (int x = x1; x <= x2; x++) {
				for (int y = y1; y <= y2; y++) {
					lights[x, y] += 1;
				}
			}
		}

		static void turnOff(string p1, string p2) {
			// TODO: Implement this.
			string[] p1s = p1.Split(",");
			int x1 = Int32.Parse(p1s[0]);
			int y1 = Int32.Parse(p1s[1]);

			string[] p2s = p2.Split(",");
			int x2 = Int32.Parse(p2s[0]);
			int y2 = Int32.Parse(p2s[1]);

			if (x1 > x2) {
				int tmp = x1;
				x1 = x2;
				x2 = tmp;
			}

			if (y1 > y2) {
				int tmp = y1;
				y1 = y2;
				y2 = tmp;
			}

			for (int x = x1; x <= x2; x++) {
				for (int y = y1; y <= y2; y++) {
					lights[x, y] -= 1;
					if (lights[x, y] < 0) lights[x, y] = 0;
				}
			}
		}

		static void toggle(string p1, string p2) {
			// TODO: Implement this.
			string[] p1s = p1.Split(",");
			int x1 = Int32.Parse(p1s[0]);
			int y1 = Int32.Parse(p1s[1]);

			string[] p2s = p2.Split(",");
			int x2 = Int32.Parse(p2s[0]);
			int y2 = Int32.Parse(p2s[1]);

			if (x1 > x2) {
				int tmp = x1;
				x1 = x2;
				x2 = tmp;
			}

			if (y1 > y2) {
				int tmp = y1;
				y1 = y2;
				y2 = tmp;
			}

			for (int x = x1; x <= x2; x++) {
				for (int y = y1; y <= y2; y++) {
					lights[x, y] += 2;
				}
			}
		}
    }
}
