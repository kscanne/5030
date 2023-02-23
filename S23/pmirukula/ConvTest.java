import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ConvTest {
    @Test
    public void turkishcheck() {
        Conv ex = new Conversion();
        String s = "KASIM";
        String l = "tr";
        Boolean m;
        String out = ex.trazConv(s, l);
        if (out.equals("kasım")) {
            m = true;
        } else {
            m = false;
        }
        assertEquals(m, true);
    }

    @Test
    public void azcheck() {
        Conv ex1 = new Conversion();
        String s1 = "KASIM";
        String l1 = "az";
        Boolean m;
        String out = ex1.trazConv(s1, l1);
        if (out.equals("kasım")) {
            m1 = true;
        } else {
            m1 = false;
        }
        assertEquals(m1, true);
    }

    @Test
    public void gacheck() {
        Conv ex2 = new Conv();
        String s2 = "nATHAIR";
        String l2 = "ga";
        Boolean m2;
        String out = ex2.trazConv(s2, l2);
        if (out.equals("n-athair")) {
            m2 = true;
        } else {
            m2 = false;
        }
        assertEquals(m2, true);
    }

    @Test
    public void nochangeincasecheck() {
        Conv ex3 = new Conversion();
        String s3 = "ภาษาไทย";
        String l3 = "th";
        Boolean m3;
        String out = ex3.allConv(s3, l3);
        if (out.equals("ภาษาไทย")) {
            m3 = true;
        } else {
            m3 = false;
        }
        assertEquals(m3, true);
    }

    @Test
    public void elcheck() {
        Conv ex4 = new Conversion();
        String s4 = "Σ";
        String l4 = "el";
        Boolean m4;
        String out = ex3.allConv(s3, l3);
        if (out.equals("σ")) {
            m4 = true;
        } else {
            m4 = false;
        }
        assertEquals(m4, true);
    }

}
