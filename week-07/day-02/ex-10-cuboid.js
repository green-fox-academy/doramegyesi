'use strict';

// Write a program that stores 3 sides of a cuboid as variables (floats)
// The program should write the surface area and volume of the cuboid like:
//
// Surface Area: 600
// Volume: 1000

var cuboidLength = 11;
var cuboidWidth = 8;
var cuboidHeight = 17;

console.log('Surface Area: ', 2 * (cuboidLength * cuboidWidth + cuboidLength * cuboidHeight + cuboidWidth * cuboidHeight));
console.log('Volume: ', cuboidWidth * cuboidLength * cuboidHeight);
