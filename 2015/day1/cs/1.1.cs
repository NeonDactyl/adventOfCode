using System;
using System.Collections.Generic;

public class Hello {
	public static void Main() {
		string text = System.IO.File.ReadAllText("1.in").Trim();
		int current_floor = 0;
		int current_step = 1;

		foreach (char c in text) {
			if (c == '(') current_floor++;
			else current_floor--;

			if (current_floor < 0) {
				Console.WriteLine(current_step);
				return;
			}

			current_step++;
		}

		Console.WriteLine(current_floor);
	}
}
