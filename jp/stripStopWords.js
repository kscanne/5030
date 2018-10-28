module.exports={
	strip_stopwords: function(languageCode, inputText){
		var fileSystem = require('fs');
		var validLanguageCodes = fileSystem.readFileSync('../data/list.txt').toString().split('\n');
		var languageCodeValid = validLanguageCodes.indexOf(languageCode);

		if (languageCodeValid === -1){
			return "Error: Not a valid language code"
		}

		var stopWords = fileSystem.readFileSync('../data/' + languageCode + '.txt').toString().split('\n');
		var splitInput = inputText.toString().split(" ");
		var finalString= "";

		for (word in splitInput){
			var found = stopWords.indexOf(splitInput[word].toLowerCase());
			if (found == -1){
				finalString = finalString + splitInput[word]+" ";
			}
		}

		return finalString.trim();
	}
};


