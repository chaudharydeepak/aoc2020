import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;
import java.util.stream.Stream;

public class Day8 {

    static int globalInt = 0;

    public static void main(String[] args) throws IOException {
        String[] allInstructions;
        List alreadyHitInsList = new ArrayList<>();
        try (Stream<String> lines = Files.lines(Paths.get((Objects.requireNonNull(Day1.class.getClassLoader().getResource("day8.txt"))).getPath()))) {
            allInstructions = lines.toArray(String[]::new);
        }

        int nextIns = 0;
        while( true)
        {
            System.out.println( nextIns );
            if(alreadyHitInsList.contains(nextIns))
            {
                System.out.println(" final answer --> " + globalInt);
                break;
            }
            alreadyHitInsList.add(nextIns);
            nextIns = nextIns + doNavigate(allInstructions, nextIns);
        }
    }

    static int doNavigate(String[] insArray, int insIndx)
    {
        String[] dataAry = insArray[insIndx].split(" ");
        if ( dataAry[0].contains("acc"))
        {
            globalInt = globalInt + Integer.parseInt(dataAry[1]);
            return  1;
        }
        if (dataAry[0].contains("nop") )
            return 1;

        return Integer.parseInt(dataAry[1]) == 0 ? 1 : Integer.parseInt(dataAry[1]);
    }
}
