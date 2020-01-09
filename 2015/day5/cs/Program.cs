using System;

namespace cs
{
    class Program
    {
        static void Main(string[] args)
        {
			string[] tests = {"jcaqyaqvsefwtaya", "usquiquspcdppqeq"};
			string[] lines = System.IO.File.ReadAllLines("5.in");
			int count = 0;
			foreach(string line in lines) {
				// Console.WriteLine("Double Letter Pairs: {0}", doubleLetterPairs(test));
				// Console.WriteLine("Separated Match: {0}", separatedMatch(test));
				if (isNice(line)) {
					count++;
				}
			}
			Console.WriteLine(count);
        }

		static bool doubleLetterPairs(string word) {
			for (int i = 0; i < word.Length - 3; i++) {
				string pair = word.Substring(i, 2);
				for (int j = i + 2; j < word.Length - 1; j++) {
					if (word.Substring(j, 2) == pair) return true;
				}
			}
			return false;
		}

		static bool separatedMatch(string word) {
			for (int i = 0; i < word.Length - 2; i++) {
				if (word[i] == word[i+2]) return true;
			}
			return false;
		}

		static bool isNice(string word) {
		//	return (threeVowels(word) && blacklistString(word) && doubleLetter(word));
			return (doubleLetterPairs(word) && separatedMatch(word));
		}

		static bool threeVowels(string line) {
			int count = 0;
			foreach (char c in line) {
				if ("aeiou".Contains(c)) count++;
				if (count == 3) return true;
			}
			return false;
		}

		static bool doubleLetter(string line) {
			for (int i = 0; i < line.Length - 1; i++) {
				if (line[i] == line[i+1]) return true;
			}
			return false;
		}

		static bool blacklistString(string line) {
			string[] blacklistWords = {"ab", "cd", "pq", "xy"};
			foreach (string word in blacklistWords) {
				if (line.Contains(word)) return false;
			}
			return true;
		}
    }
}
