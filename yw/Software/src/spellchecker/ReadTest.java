package spellchecker;
import java.io.IOException;
import java.util.List;

import org.junit.Test;

import spellchecker.Read;

public class ReadTest {

	public static void main(String[] args) {
	   
		   Read i = new Read();
		   List<String> list = null;
		try {
			list = i.read();
			//System.out.println(list);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}

}
