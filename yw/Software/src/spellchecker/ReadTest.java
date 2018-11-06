package spellchecker;
import java.io.IOException;
import java.util.List;
import java.util.Scanner;

import org.junit.Test;

import spellchecker.Read;

public class ReadTest {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	   
		   Read1 i = new Read1();
		   List<String> list = null;
		   
		try {
			String str = sc.nextLine();
			list = i.read1(str);
			System.out.println(list);
			//System.out.println(list);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		
	}

}
