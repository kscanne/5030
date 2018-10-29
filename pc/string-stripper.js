var util = require('./util.js');

var getAvailableLanguages = function () {
    return util.readTextFileToArray('../data/list.txt');
}

var getStopWords = function (languageCode) {
    var availableLanguageList = getAvailableLanguages();
    if (availableLanguageList.indexOf(languageCode) === -1) {
        console.error(`Language '${languageCode}' is supported.`);
        return [];
    }
    return util.readTextFileToArray(`../data/${languageCode}.txt`);
}

exports.stripStopWords = function (languageCode, stringToStrip) {
    var stopWordList = getStopWords(languageCode);
    var inputWordList = (stringToStrip || "").trim().split(' ');

    stopWordList.forEach(function (stopWord, stopWordIndex) {
        inputWordList.forEach(function (word, wordIndex) {
            if (stopWord.toLowerCase() === word.toLowerCase()) {
                inputWordList.splice(wordIndex, 1);
            }
        });
    });

    return inputWordList.join(" ");
}