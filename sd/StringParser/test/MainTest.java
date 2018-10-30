import com.company.FileAdapter;
import com.company.Main;
import com.company.StringFilter;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.File;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.HashSet;
import java.util.Scanner;

import static org.junit.Assert.*;

/**
 * Created by SLU on 10/29/2018.
 */
public class MainTest {
    @Before
    public void setUp() throws Exception {
    }

    @After
    public void tearDown() throws Exception {
    }

    @Test
    public void mainTest() throws Exception {
        File file = Paths.get("test\\tests\\cases.tsv").toFile();
        Scanner scanner = new Scanner(file);


        while(scanner.hasNextLine()) {
            String test = scanner.nextLine();
            Scanner testScanner = new Scanner(test);
            testScanner.useDelimiter("\\t");
            String result = Main.parseString(testScanner.next(),testScanner.next());
            assertEquals(result,testScanner.next());
        }
    }
}