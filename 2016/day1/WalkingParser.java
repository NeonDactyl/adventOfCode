import java.io.File;
import java.util.Scanner;
import java.util.ArrayList;

public class WalkingParser {
	public ArrayList<WalkingInstruction> instructions = new ArrayList<WalkingInstruction>();

	public WalkingParser(String fileName) throws Exception {
		String fileContents = new Scanner(new File(fileName)).useDelimiter("\\Z").next();
		for (String i: fileContents.split(", ")) {
			instructions.add(new WalkingInstruction(i));
		}
	}
}
