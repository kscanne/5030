var util = require('./util.js');

var getStopWords = function (languageCode) {
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