public class DayOne {
	
	public static void main(String[] args) throws Exception {
		String fileName = args[0];
		WalkingParser wp = new WalkingParser(fileName);
		Walker walker = new Walker();

		for (WalkingInstruction i: wp.instructions) {
			walker.performMovement(i);
		}

		int distance = Math.abs(walker.x) + Math.abs(walker.y);
	}
}
