import java.io.*;
import java.util.*;

public class Main {

    private static String stripStopWords(String lang, String query) {
        ArrayList<String> list = null;
        try (BufferedReader file = new BufferedReader(new FileReader("../data/" + lang + ".txt"))) {
            String stopWord = file.readLine().toLowerCase();
            String[] queryArray = query.trim().toLowerCase().split("\\s+"); //using "\s+" regex for a white space character one or more times
            list = new ArrayList<>(Arrays.asList(queryArray));

            while (stopWord != null) {
                list.remove(stopWord);
                stopWord = file.readLine();
            }

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }

        assert list != null;
        return listToSentence(list);
    }

    private static String listToSentence(ArrayList<String> list) {
        StringBuilder sentence = new StringBuilder();
        for (Object object : list) {
            sentence.append(object).append(" ");
        }

        return sentence.toString().trim();
    }

    private static void testStripStopWord() {
        //String fileName = "../tests/" + "cases_BKP.tsv";
        String fileName = "../tests/" + "cases.tsv";
        try (BufferedReader file = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = file.readLine()) != null) {
                String[] token = line.split("\t"); //.tsv files are delimited by tabs, hence the "\t" regex
                List<String> dataArray = Arrays.asList(token);

                String lang = dataArray.get(0);
                String query = dataArray.get(1);
                String expectedResult = dataArray.get(2);

                String result = stripStopWords(lang, query);

                assert expectedResult.equals(result): "Test failed; expected \""+expectedResult+"\", got \""+result+"\"";
            }
            file.close();
            System.out.println();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        testStripStopWord();
    }
}
