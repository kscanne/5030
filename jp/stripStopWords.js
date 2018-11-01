module.exports={
	strip_stopwords: function(languageCode, inputText){
		var fileSystem = require('fs');
		var validLanguageCodes = fileSystem.readFileSync('../data/list.txt').toString().split('\n');
		var languageCodeValid = validLanguageCodes.indexOf(languageCode);

		if (languageCodeValid === -1){
			return "Error: Not a valid language code"
		}

		var stopWords;
		try {
			stopWords = fileSystem.readFileSync('../data/' + languageCode + '.txt').toString().split('\n');
			stopWords.map(x => {
				x.toLowerCase(),
				x.normalize('NFC')}
				);
		} catch (err){
			if (err.code === 'ENOENT'){
				return "Error: List of Root Words not found";
			}
			else{
				throw err;
			}
		} 
		var splitInput = inputText.toString().split(" ");
		var finalString= "";

		for (index in splitInput){
			var found = stopWords.indexOf(splitInput[index].toLowerCase().normalize('NFC'));
			if (found == -1){
				finalString = finalString + splitInput[index]+" ";
			}
		}

		return finalString.trim();
	}
};


