package com.cletus.app;

import org.junit.jupiter.api.Test;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

import static com.cletus.app.QueryProcessor.stripStopWords;
import static org.junit.jupiter.api.Assertions.assertEquals;


class QueryProcessorTest {

    @Test
    void testStripStopWord() {
        String fileName = "../tests/" + "cases.tsv";
        try (BufferedReader file = new BufferedReader(new FileReader(fileName))) {
            String line = file.readLine();
            while (line != null) {
                String[] token = line.split("\t"); //.tsv files are delimited by tabs, hence the "\t" regex
                List<String> dataArray = Arrays.asList(token);
                String processedQuery = stripStopWords(dataArray.get(0), dataArray.get(1));

                assertEquals(dataArray.get(2), processedQuery);

                line = file.readLine();
            }
            file.close();
            System.out.println();

        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}