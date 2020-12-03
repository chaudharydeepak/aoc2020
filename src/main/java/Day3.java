import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Objects;
import java.util.stream.Stream;

public class Day3 {

    public static void main(String[] args) throws IOException {
        String[] forest;

        try (Stream<String> lines = Files.lines(Paths.get((Objects.requireNonNull(Day1.class.getClassLoader().getResource("day3.txt"))).getPath()))) {
            forest = lines.toArray(String[]::new);
        }

        int startIdx = 0, treeCount = 0;

        for (int row = 1; row < forest.length; row++) {
            startIdx = (startIdx + 3) % forest[row].length();
            if (forest[row].charAt(startIdx) == '#') {
                treeCount++;
            }
        }
        System.out.println("answer --> " + treeCount);
    }
}
