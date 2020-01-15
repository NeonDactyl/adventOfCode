using System;
using System.Collections.Generic;

namespace cs
{
	class WireConnection
	{
		string outputKey;
		public Instruction inst;
		private ushort signal;
		bool signalSet;

		public WireConnection(string init)
		{
			string[] splitUp = init.Split("->");
			outputKey = splitUp[1].Trim();
			inst = new Instruction(splitUp[0]);
			signalSet = false;
		}

		public ushort getOutputSignal(Dictionary<string, WireConnection> connections)
		{
			if (signalSet)
				return signal;
			switch(inst.operation)
			{
				case Operation.AND:
					if (inst.useVal) return (ushort) (inst.val & connections[inst.secondKey].getOutputSignal(connections));
					signal = (ushort) (connections[inst.firstKey].getOutputSignal(connections) & connections[inst.secondKey].getOutputSignal(connections));
					signalSet = true;
					return signal;
				case Operation.OR:
					signal = (ushort) (connections[inst.firstKey].getOutputSignal(connections) | connections[inst.secondKey].getOutputSignal(connections));
					signalSet = true;
					return signal;
				case Operation.LSHIFT:
					signal = (ushort) (connections[inst.firstKey].getOutputSignal(connections) << inst.val);
					signalSet = true;
					return signal;
				case Operation.RSHIFT:
					signal = (ushort) (connections[inst.firstKey].getOutputSignal(connections) >> inst.val);
					signalSet = true;
					return signal;
				case Operation.NOT:
					signal = (ushort) (~ connections[inst.firstKey].getOutputSignal(connections));
					signalSet = true;
					return signal;
				case Operation.NONE:
					if (inst.useVal) signal = inst.val;
					else signal = connections[inst.firstKey].getOutputSignal(connections);
					signalSet = true;
					return signal;
				default:
					return 0;
			}
		}
	}
}
