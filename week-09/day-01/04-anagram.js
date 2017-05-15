/*Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
Create a test for that.*/

function compare (a, b) {
    var firstWord = a.split("").sort().join("");
    var secondWord = b.split("").sort().join("");
    return firstWord === secondWord;
};

console.log(compare('dog', 'god'));
console.log(compare('dog', 'cat'));

module.exports = compare;
