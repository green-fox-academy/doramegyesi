// Create a function that takes two strings and decides if one is anagram of the other

let anagramCheker = function(word1, word2) {
    if (word1.length != word2.length) {
        console.log("Those are not anagrams, dude")
        return false;
    }
    else {
        let first = [];
        let second = [];
        let counter = 0;
        for (let i = 0; i < word1.length; i++) {
            first.push(word1[i]);
        };
        console.log(first);
        for (let i = 0; i < word2.length; i++) {
            second.push(word2[i]);
        };
        console.log(second);
        for (let i = 0; i < first.length; i++) {
            while (i < second.length) {
                if (i === second[i]) {
                    counter++;
                    break;
                }
                i++;
            }
        };
        console.log(counter)
        if (word1.length === counter) {
            return true;
        }
        else {
            return false;
        };
    };
};
console.log(anagramCheker("sloth", "sloth"));
console.log(anagramCheker("dog", "god"));
console.log(anagramCheker("cockroach", "sloth"));
