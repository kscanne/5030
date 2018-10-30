/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import static org.junit.Assert.assertEquals;
import org.junit.Test;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import static assignment.Assignment.*;
import java.io.FileNotFoundException;
import java.util.logging.Level;
import java.util.logging.Logger;
/**
 *
 * @author waqar
 */
public class AssignmentTest {

    @Test
    public void test_strip_stopWord() {
        String fileName = "/home/waqar/Git-Repo/5030/tests/cases.tsv";
        try (BufferedReader file = new BufferedReader(new FileReader(fileName))) {
            String line = file.readLine();
            while (line != null) {
                String[] token = line.split("\t"); 
                List<String> dataArray = Arrays.asList(token);
                String[] data = dataArray.get(1).split(" ");
                String lang_symbol = dataArray.get(0);
                String expected_out = dataArray.get(2);
                String actual_out = filter_stop_words(data, lang_symbol);

                assertEquals(expected_out, actual_out);

                line = file.readLine();
            }
            file.close();
            System.out.println();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        } catch (Exception ex) {
            System.out.println(ex.getMessage());
     }
    }
    
    @Test
    public void test_read_file(){
        
     try {
         assertEquals(new FileNotFoundException(), read_file("abcc.txt"));
         assertEquals(new FileNotFoundException(), read_file("/home/waqar/abcc.txt"));
     } catch (FileNotFoundException ex) {
         Logger.getLogger(AssignmentTest.class.getName()).log(Level.SEVERE, null, ex);
     }
    }
    
    @Test
    public void test_get_stop_words(){
        try {
            assertEquals(new Exception("Stop Words not found"), get_stop_words("it"));
            assertEquals(new Exception("Stop Words not found"), get_stop_words("we"));
            assertEquals(new Exception("Stop Words not found"), get_stop_words("kr"));
            assertEquals(new Exception("Stop Words not found"), get_stop_words("ih"));
        } catch (Exception ex) {
            Logger.getLogger(AssignmentTest.class.getName()).log(Level.SEVERE, null, ex);
        }
        
    }
    
}
