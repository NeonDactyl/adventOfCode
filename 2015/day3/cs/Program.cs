using System;
using System.Collections.Generic;
using System.Linq;

namespace day3
{
    class Program
    {
        static void Main(string[] args)
        {
			var instructions = System.IO.File.ReadAllText("3.in").Trim();
			List<Position> positionsVisited = new List<Position>();
			DeliveryUnit santa = new DeliveryUnit("Santa");
			DeliveryUnit robosanta = new DeliveryUnit("Santa");
			List<DeliveryUnit> deliverers = new List<DeliveryUnit>();
			deliverers.Add(santa);
			deliverers.Add(robosanta);
			var delivererIndex = 0;
			positionsVisited.Add(new Position(0, 0));

			foreach (var instruction in instructions) {
				Position p = new Position(0, 0);
				p = deliverers[delivererIndex].Move(parseInput(instruction));
				if (! positionsVisited.Any(i => i.Equals(p)))
				{
					positionsVisited.Add(p);
				}
				delivererIndex = (delivererIndex + 1) % deliverers.Count();
			}

			Console.WriteLine($"{positionsVisited.Count()} houses visited");
		}

		static Direction parseInput(char c) {
			switch (c) {
				case '^':
					return Direction.North;
					break;
				case '>':
					return Direction.East;
					break;
				case 'v':
					return Direction.South;
					break;
				case '<':
					return Direction.West;
					break;
				default:
					return Direction.Null;
			}
		}
    }

	enum Direction
	{
		North,
		East,
		South,
		West,
		Null
	}

	class DeliveryUnit
	{
		public string name;
		private int x;
		private int y;

		public DeliveryUnit(string name) {
			this.name = name;
			this.x = 0;
			this.y = 0;
		}

		public Position getPosition() {
			return new Position(x, y);
		}

		public Position Move(Direction direction) {
			switch (direction)
			{
				case Direction.North:
					y++;
					break;
				case Direction.East:
					x++;
					break;
				case Direction.South:
					y--;
					break;
				case Direction.West:
					x--;
					break;
				case Direction.Null:
					break;
			}
			return new Position(x, y);
		}
	}

	class Position
	{
		public int x, y;

		public Position(int x, int y)
		{
			this.x = x;
			this.y = y;
		}

		public override bool Equals(Object obj) {
			//Check for null and compare run-time types.
			if ((obj == null) || ! this.GetType().Equals(obj.GetType())) {
				return false;
			}

			else {
				Position p = (Position) obj;
				return (x == p.x) && (y == p.y);
			}
		}


		public override int GetHashCode() {
			int hash = 13;
			hash = (hash * 7) + x.GetHashCode();
			hash = (hash * 7) + y.GetHashCode();
			return hash;
		}
	}
}
