public enum Direction {
	North,
	East,
	South,
	West;

	private static Direction[] vals = values();

	public Direction right() {
		return vals[(this.ordinal() + 1) % vals.length];
	}

	public Direction left() {
		return vals[Math.floorMod(this.ordinal() - 1, vals.length)];
	}
}
