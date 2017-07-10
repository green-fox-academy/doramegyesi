// Create a function that takes two strings and decides if one is anagram of the other

let anagramCheker = function(word1, word2) {
    if (word1.length != word2.length) {
        console.log("Those are not anagrams, dude")
    }
    else {
        let first = [];
        let second = [];
        for (let i = 0; i < word1.length; i++) {
            first.push(word1[i]);
        };
        console.log(first);
        for (let i = 0; i < word2.length; i++) {
            second.push(word2[i]);
        };
        console.log(second);
    };
}

anagramCheker("sloth", "sloth");
