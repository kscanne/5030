package spellchecker;



public class Checker1 {

	
  public  String check(String a, String b) {
		
		if("en".equals(a)) {
			b = b.replaceAll("the |The | the", "");
			b = b.replaceAll(" the ", " ");
			
		}else if("ga".equals(a)) {
			b = b.replaceAll("Na | na|na ", "");
			b = b.replaceAll(" na ", " ");
			
		}else if("fr".equals(a)) {
			b = b.replaceAll(" la|la |La ", "");
			b = b.replaceAll(" la ", " ");
			
		}else {
			b = "Still working on it..";
		}
		return b;
		
	}
		
		
		//source sentences
		//String en = "the walking dead";
		//String ga = "Na daoine maithe";
		//String fr = "plus ça change, plus c'est la même chose";
		
//		String s = null;
//		String c = null;
//		while(true) {
//		System.out.println("Please input the language type:");
//		//input 
//		Scanner sc = new Scanner(System.in);
//		
//		s = sc.nextLine();
//		if("close".equals(s)) {
//		    System.out.println("System has been terminated!");
//		    sc.close();
//			return;
//		}
//		
//		if("en".equals(s)) {
//			System.out.println("Please input the santence:");
//			Scanner en = new Scanner(System.in);
//			c = en.nextLine();
//			c = c.replaceAll("the |The | the", "");
//			c = c.replaceAll(" the ", " ");
//		}else if("ga".equals(s)) {
//			System.out.println("Please input the santence:");
//			Scanner ga = new Scanner(System.in);
//			c = ga.nextLine();
//			c = c.replaceAll("Na | na|na ", "");
//			c = c.replaceAll(" na ", " ");
//
//		}else if("fr".equals(s)) {
//			System.out.println("Please input the santence:");
//			Scanner fr = new Scanner(System.in);
//			c = fr.nextLine();
//			c = c.replaceAll(" la|la |La ", "");
//			c = c.replaceAll(" la ", " ");
//
//		}else {
//			System.out.println("Input language typedoes not match!");
//			return;
//		}
//		//String e = "the ";
//		//String g = "Na ";
//		//String f = "la ";
//		
//		//String sub = s.replaceAll( "the |The | the |Na | na | na| la | la|la ","");
//        System.out.println("After checking: \n" + c);
//        //sc.close();
//		}
		
		
	

}
