'use strict';

// Write a program that prints the remaining seconds (as an integer) from a
// day if the current time is represented by these variables

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;
var secondsPerDay = 24 * 60 * 60;
var passedSeconds = 14 * 60 * 60 + 34 * 60 + 42;
var remainingSeconds = secondsPerDay - passedSeconds;
console.log(remainingSeconds);
