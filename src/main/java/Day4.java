import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day4 {

    public static void main(String[] args) throws IOException {
        List<String> inputSet;
        String[] allPassports;
        try (Stream<String> lines = Files.lines(Paths.get((Objects.requireNonNull(Day1.class.getClassLoader().getResource("day4.txt"))).getPath()))) {
            allPassports = lines.toArray(String[]::new);
        }

        int validPassport = 0;
        String individualPassport = "";
        for (String allPassport : allPassports) {
            if (allPassport.trim().length() == 0) {
                Map<String, String> passportMap = Arrays.stream(individualPassport.trim().split(" ")).map(s -> s.split(":")).collect(Collectors.toMap(s -> s[0], s -> s[1]));
                if (isValidByr(passportMap.get("byr")) && isValidIyr(passportMap.get("iyr")) && isValidEyr(passportMap.get("eyr")) &&
                        isValidHgt(passportMap.get("hgt")) && isValidHcl(passportMap.get("hcl")) && isValidEcl(passportMap.get("ecl")) &&
                        isValidPid(passportMap.get("pid"))
                ) {
                    validPassport = validPassport + 1;
                }
                System.out.println(" encountered new passport start , adjucted: " + individualPassport + " " + validPassport);
                individualPassport = "";
            }
            individualPassport = allPassport.trim() + " " + individualPassport;
        }

        System.out.println("answer --> " + validPassport);
    }

    static boolean isValidByr(String byr) {
        return null != byr && (Integer.parseInt(byr) >= 1920 && Integer.parseInt(byr) <= 2002);
    }

    static boolean isValidIyr(String byr) {
        return null != byr && (Integer.parseInt(byr) >= 2010 && Integer.parseInt(byr) <= 2020);
    }

    static boolean isValidEyr(String byr) {
        return null != byr && (Integer.parseInt(byr) >= 2020 && Integer.parseInt(byr) <= 2030);
    }

    static boolean isValidHgt(String hgt) {
        if ( null!= hgt ) {
            if (hgt.contains("cm")) {
                int hgtInt = Integer.parseInt(hgt.replace("cm", ""));
                return hgtInt >= 150 && hgtInt <= 193;
            } else {
                int hgtIntCm = Integer.parseInt(hgt.replace("in", ""));
                return hgtIntCm >= 59 && hgtIntCm <= 76;
            }
        }
        return false;
    }

    static boolean isValidHcl(String byr) {
        return null!= byr && Pattern.compile("^#[0-9a-f]{6}$").matcher(byr).find();
    }

    static boolean isValidEcl(String byr) {
        return null != byr && Pattern.compile("amb|blu|brn|gry|grn|hzl|oth").matcher(byr).find();
    }

    static boolean isValidPid(String byr) {
        return null != byr && Pattern.compile("^[0-9]{9}$").matcher(byr).find();
    }
}
