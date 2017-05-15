var test = require('tape');
var countLetters = require('./05-countletters.js');

test('count the letters', function(t) {
  t.deepEqual(countLetters('pope'), {p:2, o:1, e:1});
  t.end();
});

test('count the letters', function(t) {
  t.throws(function() {countLetters(8)}, 'input must be a string!');
  t.end();
});
