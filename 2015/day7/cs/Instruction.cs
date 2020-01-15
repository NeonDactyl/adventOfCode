using System;

namespace cs
{
	class Instruction
	{
		public string firstKey;
		public string secondKey;
		public ushort val;
		public Operation operation;
		public bool useVal;
		
		public Instruction(string parsee)
		{
			string[] separated = parsee.Trim().Split();

			if (separated.Length == 1)
			{
				try {
					val = UInt16.Parse(separated[0]);
					operation = Operation.NONE;
					useVal = true;
				} catch {
					firstKey = separated[0];
					operation = Operation.NONE;
					useVal = false;
				}
			}
			else if (separated.Length == 2)
			{
				if (separated[0] == "NOT")
				{
					operation = Operation.NOT;
					firstKey = separated[1];
				}
			}
			else
			{
				switch (separated[1])
				{
					case "AND":
						operation = Operation.AND;
						try
						{
							val = UInt16.Parse(separated[0].Trim());
							useVal = true;
						} catch {
							firstKey = separated[0];
							useVal = false;
						}
						secondKey = separated[2];
						break;
					case "OR":
						operation = Operation.OR;
						firstKey = separated[0];
						secondKey = separated[2];
						break;
					case "LSHIFT":
						operation = Operation.LSHIFT;
						firstKey = separated[0];
						val = UInt16.Parse(separated[2]);
						break;
					case "RSHIFT":
						operation = Operation.RSHIFT;
						firstKey = separated[0];
						val = UInt16.Parse(separated[2]);
						break;
				}
			}
		}

	}
}
