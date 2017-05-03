'use strict';
// - Create a function called `printer`
//   which logs to the console the input parameters
//   (can have multiple number of arguments)

function printer(inputs) {
    var output = '';
    for (var p = 0; p < arguments.length; p++) {
        output += arguments[p]
    }
    return output;
}

console.log(printer('ice', 'ice', 'baby'))
