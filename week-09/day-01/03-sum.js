/*Create a sum method in your class which has a list of integers as parameter
It should return the sum of the elements in the list
Follow these steps:
Add a new test case
Instantiate your class
create a list of integers
use the t.equal to test the result of the created sum method
Run it
Create different tests where you
test your method with an empyt list
with a list with one element in it
with multiple elements in it
with a null
with a string
Run them
Fix your code if needed*/

function summarize() {
    this.sum = function(arr) {
        if (Array.isArray(arr) === false) {
            throw new Error('input must be an array')
        } else {
            var total = 0;
            arr.forEach(function(element) {
                total += element;
        })};
        return total;
    }
};

module.exports = summarize;

try {
    var dog = new summarize();
    var cat = dog.sum('sloth');
    console.log('macska ', cat);
} catch (err) {
    console.log('catching error: ');
    console.log(err.message)
};
