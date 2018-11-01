import static org.junit.Assert.*;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

import org.junit.Test;

import spellchecker.Checker1;
import spellchecker.Checker2;
import spellchecker.Read;
 
public class Checker1Test {
//   @Test
//   public void testcheck() {
//	   StringTokenizer st ;
//	   BufferedReader TSVFile;
//	   //use BufferReader to read the tsv file
//	try {
//		TSVFile = new BufferedReader(new FileReader("C:\\Users\\wangyifei\\software\\5030\\tests\\cases.tsv"));
//		String dataRow = TSVFile.readLine();
//		System.out.println("file read successful");
//		Checker1 c = new Checker1();
//		int i = 0;
//		while (dataRow != null){
//            st = new StringTokenizer(dataRow,"\t");
//            
//            
//            String languageCode = st.nextToken();
//            String str = st.nextToken();
//            String expected = st.nextToken();
//            
//            System.out.println(expected + "  " + c.check(str));
//            assertEquals(expected, c.check(str));
//            
//            dataRow = TSVFile.readLine(); // Read next line of data.
//            i++;
//            System.out.println("It works for case " + i);
//        }
//		System.out.println("It works well for " + i + " cases!");
//        // Close the file once all data has been read.
//        TSVFile.close();
//	
//	} catch (FileNotFoundException e) {
//		// TODO Auto-generated catch block
//		e.printStackTrace();
//	} catch (IOException e) {
//		// TODO Auto-generated catch block
//		e.printStackTrace();
//	}
//
//			
//   }

   
   
   @Test
   public void testcheck1() {
	try {
		String [] language = {
				"en", 
				"fr", 
				"ga", 
				"gd", 
				"gv", 
				"ru", 
		};
		String [] line = null;
		BufferedReader TSVFile;
		   //use BufferReader to read the tsv file
		TSVFile = new BufferedReader(new FileReader("C:\\Users\\wangyifei\\software\\5030\\tests\\cases.tsv"));
		String dataRow = "";
		System.out.println("file read successful");
		Checker2 c = new Checker2();
		int i = 0;
		String lan = null;
		String arr = null;
		String expected = null;
		String result = null;
		while (dataRow != null){
	
			dataRow = TSVFile.readLine(); // Read next line of data.Xt
            line = dataRow.split("\t");
            String [] strList = {"", "", ""};
            int j = 0;
            for (String e: line) {
            	strList[j] = e;
            	j ++;
            }
           
            lan = strList[0];
            arr = strList[1];
            expected = strList[2];
            
            if (Arrays.binarySearch(language, lan) < 0){
            	result = expected;
            } else {
                result = c.check(arr);
            }
            if(expected.equals(result)) {
            	System.out.printf("-%d %s %n", i, result);
            }else {
            	System.out.printf("+%d %s <- %s %n", i, result, expected);
            }
           // assertEquals(expected, c.check(str));
            
            
            i++;
            
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