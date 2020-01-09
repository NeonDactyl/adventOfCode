public class WalkingInstruction {
	public int count;
	public Turn turn;

	public WalkingInstruction(String inputInstruction) {
		String[] inputInstructionArray = inputInstruction.split("", 2);

		if (inputInstructionArray[0].equals("L")) {
			turn = Turn.Left;
		} else if (inputInstructionArray[0].equals("R")) {
			turn = Turn.Right;
		}

		count = Integer.parseInt(inputInstructionArray[1]);
	}

}
