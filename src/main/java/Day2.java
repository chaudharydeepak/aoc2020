import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.Objects;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day2 {

    public static void main(String[] args) throws IOException {

        List<String> inputSet;
        try (Stream<String> lines = Files.lines(Paths.get((Objects.requireNonNull(Day1.class.getClassLoader().getResource("day2.txt"))).getPath()))) {
            inputSet = lines.collect(Collectors.toList());
        }
        AtomicInteger validCount = new AtomicInteger(0);
        inputSet.forEach(currLine -> {
                    if (isValidPswd(currLine))
                        validCount.getAndIncrement();
                }
        );
        System.out.println(" --> answer: " + validCount.get());
    }

    private static boolean isValidPswd(String currLine) {

        String[] inpAry = currLine.split(":");
        String[] leftAry = inpAry[0].split("\\s");
        String[] countPolicy = leftAry[0].split("-");
        char charToFind = leftAry[1].charAt(0);
        long count = inpAry[1].trim().chars().filter(ch -> ch == charToFind).count();
        return Integer.parseInt(countPolicy[1]) >= count && count >= Integer.parseInt(countPolicy[0]);
    }
}
