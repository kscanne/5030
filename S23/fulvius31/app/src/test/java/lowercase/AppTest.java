package lowercase;

import org.junit.Test;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.text.Normalizer;

import static org.junit.Assert.assertEquals;


public class AppTest {

    @Test
    public void testLowercaser() throws IOException {
        File projectDir = new File(System.getProperty("user.dir"));
        File file = new File(projectDir, "../tests.tsv");

        BufferedReader reader =
                new BufferedReader(new FileReader(file));
        String line;
        while ((line = reader.readLine()) != null) {
            String[] values = line.split("\t");
            byte[] utf8Bytes = values[0].getBytes(StandardCharsets.UTF_8);

            String upper =  new String(utf8Bytes, StandardCharsets.UTF_8);
            String lang = values[1];
            String expected = values[2];

            Lowercaser lowercaser = new Lowercaser(upper,lang);
            String result = lowercaser.getLowerCase();
            String normalizedExpected = Normalizer.normalize(expected, Normalizer.Form.NFC);
            System.out.println(upper+ " " + expected + " "+ result + " " + lang);
            assertEquals(normalizedExpected, result);
        }
        reader.close();

    }
}
