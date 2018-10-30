import static org.junit.Assert.*;


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

import java.util.StringTokenizer;

import org.junit.Test;

import spellchecker.Checker1;
 
public class Checker1Test {
   @Test
   public void testcheck() {
	   StringTokenizer st ;
	   BufferedReader TSVFile;
	   
	try {
		TSVFile = new BufferedReader(new FileReader("C:\\Users\\wangyifei\\5030\\tests\\cases2.tsv"));
		String dataRow = TSVFile.readLine();
		System.out.println("file read successful");
		Checker1 c = new Checker1();
		int i = 0;
		while (dataRow != null){
            st = new StringTokenizer(dataRow,"\t");
            
            
            String languageCode = st.nextToken();
            String str = st.nextToken();
            String expected = st.nextToken();
            
            
            assertEquals(expected, c.check(languageCode, str));
            
            dataRow = TSVFile.readLine(); // Read next line of data.
            i++;
            System.out.println("It works for case " + i);
        }
		System.out.println("It works well for " + i + " cases!");
        // Close the file once all data has been read.
        TSVFile.close();
	
	} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}

			
   }
   
   
   
   
   
  
}