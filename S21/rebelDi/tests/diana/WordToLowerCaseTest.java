package diana;

import org.junit.Test;
import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;
import static org.junit.Assert.*;

public class WordToLowerCaseTest {

    /**
     * This is the test method for WordToLowerCase class,
     * that tests the result of changeWordToLowerCase()
     */
    @Test
    public void changeWordToLowerCase() throws IOException {
        List<String[]> wordsToProcess = openTSV();
        for(String[] wordData:wordsToProcess){
            String wordForLowerCase = wordData[0];
            String language = wordData[1];
            String correctWordInLowerCase = wordData[2];

            System.out.println("Word for lowercase: " + wordForLowerCase);

            String wordInLowerCase = WordToLowerCase.changeWordToLowerCase(wordForLowerCase, language);
            assertEquals("The word was processed correctly", correctWordInLowerCase, wordInLowerCase);
        }
    }

    /**
     * This is the function for opening the tsv file with examples of words to convert
     *
     * @return all the data from file
     */
    public static List<String[]> openTSV () throws IOException {
        List<String[]> listOfDataFromFile = new ArrayList<>();

        StringTokenizer stringTokenizer; // used to get data from row for each column
        BufferedReader tsvFile = new BufferedReader(new FileReader
                (System.getProperty("user.dir") + "\\tests\\resources\\tests.tsv"));
        String dataRow = tsvFile.readLine(); // Read first line

        int iteration = 1;
        String[] row = new String[3]; // used to get one line of data to the list
        while (dataRow != null){
            stringTokenizer = new StringTokenizer(dataRow,"\t");
            List<String> dataArray = new ArrayList<>() ;
            while(stringTokenizer.hasMoreElements()){
                dataArray.add(stringTokenizer.nextElement().toString());
            }


            for (String item:dataArray) {
                row[iteration - 1] = item; // fill in the array with an item from file
                // each line in file has 3 items, when the last item added
                // insert the row into the list of data and empty the row array
                if (iteration % 3 == 0) {
                    listOfDataFromFile.add(row);
                    iteration = 1;
                    row = new String[3];
                }else {
                    iteration++;
                }
            }
            dataRow = tsvFile.readLine(); // Read next line of data
        }
        // Close the file once all data has been read
        tsvFile.close();
        return listOfDataFromFile;
    }
}