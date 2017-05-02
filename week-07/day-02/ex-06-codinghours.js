'use strict';

// An average Green Fox attendee codes 6 hours daily
// The semester is 17 weeks long
//
// Print how many hours is spent with coding in a semester by an attendee,
// if the attendee only codes on workdays.
//
// Print the percentage of the coding hours in the semester if the average
// work hours weekly is 52

var semester = 17
var workdaysPerWeek = 5
var dailyCodingHours = 6
var averageWorkingHours = 52
var totalCodingHours = semester * workdaysPerWeek * dailyCodingHours

console.log('Hours spent with coding: ', totalCodingHours)
console.log('Average: ', (dailyCodingHours * workdaysPerWeek / 52) * 100, '%')

// without variables

console.log('Hours spent with coding: ', 17 * 5 * 6)
console.log('Average: ', (6 * 5 / 52) * 100, '%')
