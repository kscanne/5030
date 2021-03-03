package diana;

import org.junit.Test;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import static org.junit.Assert.*;

public class WordToLowerCaseTest {

    @Test
    public void changeWordToLowerCase() throws IOException {
        List<String[]> wordsToProcess = openTSV();
        for(String[] wordData:wordsToProcess){
            String wordForLowerCase = wordData[0];
            String language = wordData[1];
            String correctWordInLowerCase = wordData[2];

            System.out.println("Word for lowercase: " + wordForLowerCase);

            String wordInLowerCase = WordToLowerCase.changeWordToLowerCase(wordForLowerCase, language);
            assertEquals(correctWordInLowerCase, wordInLowerCase);
        }
    }

    public static List<String[]> openTSV () throws IOException {
        List<String[]> wordsToProcess = new ArrayList<>();

        StringTokenizer st;
        BufferedReader TSVFile = new BufferedReader(new FileReader(System.getProperty("user.dir") + "\\tests\\resources\\tests.tsv"));
        String dataRow = TSVFile.readLine(); // Read first line.

        int iteration = 1;
        String[] array = new String[3];
        while (dataRow != null){
            st = new StringTokenizer(dataRow,"\t");
            List<String> dataArray = new ArrayList<String>() ;
            while(st.hasMoreElements()){
                dataArray.add(st.nextElement().toString());
            }

            for (String item:dataArray) {
                array[iteration - 1] = item;
                if (iteration % 3 == 0) {
                    wordsToProcess.add(array);
                    iteration = 1;
                    array = new String[3];
                }else {
                    iteration++;
                }
            }
            dataRow = TSVFile.readLine(); // Read next line of data.
        }
        // Close the file once all data has been read.
        TSVFile.close();
        return wordsToProcess;
    }
}