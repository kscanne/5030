package com.company.util;

import java.util.*;
import java.io.*;
import java.util.stream.Collectors;

public class Stripper {

    private String dataDir;
    private Map<String, Set<String>> loadedLanguages;
    private Set<String> providedLanguages;

    /**
     * Stripper constructor
     *
     * @param dataDir   - the directory in which there is the list ("list.txt") with all the
     *                    language codes and all the stopwords lists (<languageCode>.txt)
     */
    public Stripper(String dataDir) throws IOException {

        this.dataDir = dataDir;
        this.loadedLanguages = new HashMap<>();
        this.providedLanguages = readProvidedLanguages();

    }

    /**
     * This is the main method
     *
     * @param languageCode  - the language code
     * @param str           - the string we want to strip
     * @return              - the previous string without stopwords
     */
    public String stripStopwords(String languageCode, String str) throws IOException, StripperException {

        Set<String> StopwordsSet = this.getStopwords(languageCode);

        return Collections.list(new StringTokenizer(str, " ")).stream()
                    .map(Object::toString)
                    .filter( (w) -> {
                        return !StopwordsSet.contains(w.toLowerCase());
                    })
                    .collect( Collectors.joining( " " ) );


    }

    /**
     * Method to load all the stopwords of a certain language
     *
     * @param languageCode  - the language code
     * @return              - a set of stopwords related to that language
     *
     */
    private Set<String> getStopwords(String languageCode) throws IOException, StripperException {

        if(!providedLanguages.contains(languageCode)) {
            throw new StripperException("language code is incorrect!");
        }

        if(loadedLanguages.containsKey(languageCode)) {
            return loadedLanguages.get(languageCode);
        }

        HashSet<String> newLanguage = new HashSet<>();

        File file = new File(this.dataDir + "//" + languageCode + ".txt");

        BufferedReader br = new BufferedReader(new FileReader(file));

        String stopword;
        while ((stopword = br.readLine()) != null){
            newLanguage.add(stopword);
        }

        loadedLanguages.put(languageCode, newLanguage);

        return newLanguage;

    }

    /**
     * Method to load all the available languages
     *
     * @return  - a set of all the available language codes
     *
     */
    private Set<String> readProvidedLanguages() throws IOException {

        Set<String> languageCodes = new HashSet<>();

        File file = new File(this.dataDir + "//list.txt");

        BufferedReader br = new BufferedReader(new FileReader(file));

        String languageCode;
        while ((languageCode = br.readLine()) != null){
            languageCodes.add(languageCode);
        }

        return languageCodes;

    }



}
