/*
 *
 * This program requires a working boost installation and the proper c++ 11 or greater compiler
 * author: Jakob Horner
 *
 * */

#include <algorithm>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <boost/algorithm/string.hpp>

#include "strip_stopwords.h"

int main() {
	//Main method used to run the test cases
	std::ifstream testFile ("../tests/cases.tsv");
	if(testFile.is_open()){
		std::string line = "";
		std::vector<std::string> lineVector = { "" };
		std::string strippedLine = "";
		while(getline(testFile, line)){
			boost::algorithm::split(lineVector, line, boost::is_any_of("\t"));
			strippedLine = strip_stopwords(lineVector[0], lineVector[1]);
			if(strippedLine.compare(lineVector[2])){
				std::cout << "Failed Test Case: " << lineVector[1] << "\n";
				std::cout << "Expected Output: " << lineVector[2] << "\n";
				std::cout << "Actual Output: " << strippedLine << "\n";
			}
		}
	}
	else{
		std::cout << "Unable to open Test Case File\n";
	}
	return 0;
}

std::string strip_stopwords(std::string langCode, std::string stripString) {
	std::vector<std::string> wordsToStrip = { "" };
	
	//Format strings for easier comparison
	std::string strippedString = " "+ stripString + " ";
	boost::algorithm::to_lower(strippedString);
	
	wordsToStrip = read_from_datafile("../data/" + langCode + ".txt"); 
	
	for(const auto& stopword : wordsToStrip){
		//loop over all instances of the stopword in the string
		while(strippedString.find(" " + stopword + " ") != std::string::npos ){
			size_t sindex = strippedString.find(" " + stopword + " ");
			strippedString.replace(sindex, stopword.length()+2, " ");
		}
	}
	
	//Format string for correct output - remove spaces added for comparison convenience
	strippedString.replace(0, 1, "");
	strippedString.replace(strippedString.length()-1, 1, "");

	return strippedString;
}

std::vector<std::string> read_from_datafile(std::string fileName){
	std::vector<std::string> wordsToStrip = { "" };
	
	std::ifstream stopwordsFile (fileName);

	if(stopwordsFile.is_open()) {
		std::string line;
		while(getline(stopwordsFile, line)) {
			wordsToStrip.push_back(line);
		}
		stopwordsFile.close();
	}
	else { 
		std::cout << "Unable to open file\n";
		wordsToStrip = { "" };
	}

	return wordsToStrip;
}
