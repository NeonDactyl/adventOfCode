import java.util.ArrayList;

public class Walker {
	public int x, y;
	Direction facing;
	private ArrayList<String> history = new ArrayList<String>();

	public Walker() {
		x = y = 0;
		facing = Direction.North;
	}

	public void performMovement(WalkingInstruction walkingInstruction) {
		turn(walkingInstruction.turn);
		move(walkingInstruction.count);
	}

	private void move(int count) {
		switch (facing) {
			case North:
				for (int i = 0; i < count; i++) {
					y += 1;
					if (history.contains(String.format("%d,%d", x, y))) {
						System.out.println(String.format("%d,%d", x, y));
						System.exit(0);
					} else {
						history.add(String.format("%d,%d", x, y));
					}
				}
				break;
			case East:
				for (int i = 0; i < count; i++) {
					x += 1;
					if (history.contains(String.format("%d,%d", x, y))) {
						System.out.println(String.format("%d,%d", x, y));
						System.exit(0);
					} else {
						history.add(String.format("%d,%d", x, y));
					}
				}
				break;
			case South:
				for (int i = 0; i < count; i++) {
					y -= 1;
					if (history.contains(String.format("%d,%d", x, y))) {
						System.out.println(String.format("%d,%d", x, y));
						System.exit(0);
					} else {
						history.add(String.format("%d,%d", x, y));
					}
				}
				break;
			case West:
				for (int i = 0; i < count; i++) {
					x -= 1;
					if (history.contains(String.format("%d,%d", x, y))) {
						System.out.println(String.format("%d,%d", x, y));
						System.exit(0);
					} else {
						history.add(String.format("%d,%d", x, y));
					}
				}
				break;
		}
	}

	private void turn(Turn turn) {
		if (turn == Turn.Left) {
			facing = facing.left();
		} else {
			facing = facing.right();
		}
	}

	public void printPosition() {
		System.out.println(String.format("%d, %d", x, y));
	}

	public void printDirection() {
		System.out.println(facing);
	}

}
