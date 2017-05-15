/*Write a function, that takes two strings and returns a boolean value based on if the two strings are Anagramms or not.
Create a test for that.*/

function compare (a, b) {
    if (typeof a !== 'string' || typeof b !== 'string') {
        throw new Error('inputs must be strings')
    } else {
        var firstWord = a.split("").sort().join("");
        var secondWord = b.split("").sort().join("");
        return firstWord === secondWord;
    }
};

try {
    compare(3, 'cat');
} catch (err) {
    console.log('catching error: ');
    console.log(err.message)
};

module.exports = compare;
