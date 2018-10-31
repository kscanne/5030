var util = require('./util.js');

var getAvailableLanguages = function () {
    var availableLanguageList = util.readTextFileToArray('../data/list.txt');
    if (availableLanguageList.indexOf(languageCode) === -1) {
        // console.error(`Language '${languageCode}' is not supported.`);
        throw new Error("Not a valid language code");
    }
}

var getStopWords = function (languageCode) {
    return util.readTextFileToArray(`../data/${languageCode}.txt`);
}

exports.stripStopWords = function (languageCode, stringToStrip) {
    try {
        getAvailableLanguages(languageCode);
        var stopWordList = getStopWords(languageCode);
        var inputWordList = (stringToStrip || "").trim().split(new RegExp(/\s+/));

        stopWordList.forEach(function (stopWord) {
            inputWordList = inputWordList.filter(word => stopWord.toLowerCase() !== word.toLowerCase());
        });

        return inputWordList.join(" ");

    } catch (e) {
        return e.toString();
    }
}