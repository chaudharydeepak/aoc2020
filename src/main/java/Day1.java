import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day1 {

    // TODO - optimize.
    public static void main(String[] args) throws IOException {
        Set<String> inputSet;
        try (Stream<String> lines = Files.lines(Paths.get((Objects.requireNonNull(Day1.class.getClassLoader().getResource("input.txt"))).getPath()))) {
            inputSet = lines.collect(Collectors.toSet());
        }

        Set<Integer> answerSet1 = find(2020, inputSet);
        System.out.println("1st answer --> " + answerSet1 + " : " + answerSet1.stream().reduce(1, (a, b) -> a * b));

        inputSet.forEach(curItem -> {
            int curItemInt = Integer.parseInt(curItem);
            int sumToFind = 2020 - curItemInt;
            Set<Integer> answerSet2 = find(sumToFind, inputSet);
            if (!answerSet2.isEmpty()) {
                answerSet2.add(curItemInt);
                System.out.println("2nd answer --> " + answerSet2 + " : " + answerSet2.stream().reduce(1, (a, b) -> a * b));
                throw new RuntimeException("**** result already derived. stop processing ****");
            }
        });
    }

    static Set<Integer> find(int sumToFind, Set<String> inputParams) {
        Set<Integer> answerList = new HashSet<>();
        inputParams.forEach(x -> {
            int xInt = Integer.parseInt(x);
            int remInt = sumToFind - xInt;
            if (inputParams.contains(String.valueOf(remInt))) {
                answerList.add(xInt);
                answerList.add(remInt);
            }
        });
        return answerList;
    }
}
