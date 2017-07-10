// Create a function that takes two strings and decides if one is anagram of the other

let anagramChecker = function(str1, str2) {
    if (str1.length === str2.length) {
        for (let i = 0; i <str1.length; i++) {
            if (str1[i] !== str2[-1]) {
                return true;
            }
        }
    } return false;
}

console.log(anagramChecker("god", "dogo"));
console.log(anagramChecker("god", "dog"));
console.log(anagramChecker("ogd", "dog"));
