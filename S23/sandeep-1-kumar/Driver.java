import java.util.Scanner;


public class Driver {

    public static void main(String[] args)
    {
        try(Scanner scannerObject = new Scanner(System.in);)
        {     
            System.out.println("Please Enter the Language");
            String language = scannerObject.nextLine();
            System.out.println("Please Enter the word");
            String word = scannerObject.nextLine();
            LowerCasing lowerCasing = new LowerCasing();
            System.out.println(lowerCasing.lowerCaseConversion(language, word));
        }
        catch(Exception e)
        {
            System.out.println(e.getMessage());
        }
        
    }
    
}
